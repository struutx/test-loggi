from django.urls import path
from .views import UserDetails, ListUsers, UserCreate, UpdateUser, DeleteUser

urlpatterns = [
    path('users/list', ListUsers.as_view()),
    path('users/create', UserCreate.as_view()),
    path('users/<uuid:user_id>', UserDetails.as_view()),
    path('users/update/', UpdateUser.as_view()),
    path('users/delete/<uuid:user_id>', DeleteUser.as_view())

]