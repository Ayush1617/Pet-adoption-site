from django.urls import path
from . import views
app_name= 'pet_app'

urlpatterns = [
 path('pet_list/',views.pet_list, name = 'pet_list' ),
 path('create/',views.pet_avilability_create, name = 'pet_avilability_create' ),
 path('<int:pet_list_id>/edit/',views.pet_list_edit, name = 'pet_list_edit' ),
 path('<int:pet_list_id>/delete/',views.pet_list_delete, name = 'pet_list_delete' ),

]