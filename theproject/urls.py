"""theproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include
from django.urls import path
from Pannel import views as pannel
from blogapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home, name='home'),
    path('post/<int:pid>', views.postdetail, name='post'),
    path('addpost', views.addPost.as_view(), name='addPost'),
    path('updatePost/<int:pk>', views.updatePost.as_view(), name='updatePost'),
    path('deletePost/<int:pk>', views.deletePost.as_view(), name='deletePost'),
    path('category/<int:cid>', views.categoryPage, name='category'),
    path('like/<int:pk>', views.like, name='like'),
    path('', include('django.contrib.auth.urls')),
    path('', include('members.urls')),
    path('', include('Pannel.urls')),
    path('profile/<int:aid>', views.profile, name='profile'),
    path('vote/<int:question_id>', views.vote, name='vote'),
    path('postcomment/<int:cid>', views.postcomment, name='postcomment'),
    path('contact', views.contact, name='contact'),

] + static(settings.MEDIA_URL,
           document_root=settings.MEDIA_ROOT)
