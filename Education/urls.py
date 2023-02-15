from django.urls import path
from Education.views import Edu_response,new_edu_response,edit_edu_response,delete_edu_response,new_cou_response,edit_cou_response,delete_cou_response

urlpatterns = [
    path('', Edu_response,name="main_edcuation"),
    path('new_edu', new_edu_response, name="new_edu"),
    path('edit_edu/<int:id>', edit_edu_response, name="edit_edu"),
    path('delete_edu/<int:id>', delete_edu_response, name="delete_edu"),
    path('new_cou', new_cou_response, name="new_cou"),
    path('edit_cou/<int:id>', edit_cou_response, name="edit_cou"),
    path('delete_cou/<int:id>', delete_cou_response, name="delete_cou"),
]
