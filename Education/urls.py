from django.urls import path
from Education.views import Edu_response

urlpatterns = [
    path('', Edu_response,name="main_edcuation"),
]
