from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
  path(''       , views.index,  name='index'),
  path('tables/', views.tables, name='tables'),
  path('data-entry/', views.data_entry, name='data_entry'),
  path('submit_data/', views.submit_data, name='submit_data'),
  path('delete_data', views.delete_data, name='delete_data'),
  path('get_data/<str:table_name>/', views.get_table_data, name='get_table_data'),
  path('delete_interview/<int:interview_id>/', views.delete_interview, name='delete_interview'),
  path('delete_applicant/<int:applicant_id>/', views.delete_applicant, name='delete_applicant'),
  path('delete_job_posting/<int:job_id>/', views.delete_job_posting, name='delete_job_posting'),
  path('delete_placement/<int:placement_id>/', views.delete_placement, name='delete_placement'),
]
