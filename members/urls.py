from django.urls import path
from .views import createProfile, editProfile, register, authorRequest
urlpatterns = [
    path('register', register, name='register'),
    path('createProfile', createProfile.as_view(), name='createProfile'),
    path('editProfile/<int:pk>', editProfile.as_view(), name='editProfile'),
    path('authorRequest/<int:uid>', authorRequest, name='authorRequest'),

]
