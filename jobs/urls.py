from django.urls import path
from . import views

urlpatterns = [
    path('', views.job_list, name='job_list'),  # Job list view
    path('<int:job_id>/', views.job_detail, name='job_detail'),  # Job detail view
    path('create/', views.job_create, name='job_create'),  # Job creation view
    path('<int:job_id>/edit/', views.job_edit, name='job_edit'),  # Edit job
    path('<int:job_id>/delete/', views.job_delete, name='job_delete'),  # Delete job
]