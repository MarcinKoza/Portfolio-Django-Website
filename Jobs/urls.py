from django.urls import path
from Jobs.views import jobs_response, new_job_response,edit_job_response,delete_job_response

urlpatterns = [
    path('', jobs_response,name="main_job"),
    path('new', new_job_response,name="new_job"),
    path('edit/<int:id>', edit_job_response,name="edit_job"),
    path('delete/<int:id>', delete_job_response,name="delete_job"),
]
