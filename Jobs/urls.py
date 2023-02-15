from django.urls import path
from Jobs.views import jobs_response, new_job_response,edit_job_response,delete_job_response
from Skills.views import new_skill_response,edit_skill_response,delete_skill_response

urlpatterns = [
    path('', jobs_response,name="main_job"),
    path('new', new_job_response,name="new_job"),
    path('edit/<int:id>', edit_job_response,name="edit_job"),
    path('delete/<int:id>', delete_job_response,name="delete_job"),
    path('newskill', new_skill_response, name="new_skill"),
    path('editskill/<int:id>', edit_skill_response, name="edit_skill"),
    path('deleteskill/<int:id>', delete_skill_response, name="delete_skill"),
]
