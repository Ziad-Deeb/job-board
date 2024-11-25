from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator
from .models import Job
from .forms import *
from django.db.models import Q


def job_list(request):
    query = request.GET.get('q')  # Search query
    location_filter = request.GET.get('location')  # Location filter
    company_filter = request.GET.get('company')  # Company filter
    min_salary = request.GET.get('min_salary')  # Minimum salary
    max_salary = request.GET.get('max_salary')  # Maximum salary
    sort_by = request.GET.get('sort', 'title')  # Sorting parameter, default to 'title'

    jobs = Job.objects.all()

    # Apply search filter
    if query:
        jobs = jobs.filter(title__icontains=query)

    # Apply location filter
    if location_filter:
        jobs = jobs.filter(location__icontains=location_filter)

    # Apply company filter
    if company_filter:
        jobs = jobs.filter(company__icontains=company_filter)

    # Apply salary range filter
    if min_salary and max_salary:
        jobs = jobs.filter(salary__gte=min_salary, salary__lte=max_salary)

    # Apply sorting
    if sort_by in ['title', 'company', 'location', 'salary', 'application_deadline']:
        jobs = jobs.order_by(sort_by)

    # Add pagination
    paginator = Paginator(jobs, 5)  # 5 jobs per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'jobs/job_list.html', {
        'page_obj': page_obj,
        'query': query,
        'location_filter': location_filter,
        'company_filter': company_filter,
        'min_salary': min_salary,
        'max_salary': max_salary,
    })

def job_detail(request, job_id):
    job = get_object_or_404(Job, id=job_id)  # Retrieve the job or return a 404 error
    return render(request, 'jobs/job_detail.html', {'job': job})

@login_required
@permission_required('jobs.add_job', raise_exception=True)
def job_create(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.creator = request.user  # Associate job with the logged-in user
            job.save()
            return redirect('job_list')
    else:
        form = JobForm()

    return render(request, 'jobs/job_create.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login after successful registration
    else:
        form = RegistrationForm()

    return render(request, 'registration/register.html', {'form': form})

@login_required
@permission_required('jobs.change_job', raise_exception=True)
def job_edit(request, job_id):
    job = get_object_or_404(Job, id=job_id, creator=request.user)
    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('job_detail', job_id=job.id)
    else:
        form = JobForm(instance=job)

    return render(request, 'jobs/job_edit.html', {'form': form})

@login_required
@permission_required('jobs.delete_job', raise_exception=True)
def job_delete(request, job_id):
    job = get_object_or_404(Job, id=job_id, creator=request.user)
    if request.method == 'POST':
        job.delete()
        return redirect('job_list')

    return render(request, 'jobs/job_confirm_delete.html', {'job': job})