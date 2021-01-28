from Pannel import views
from django.urls import path
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('allPosts', views.all.as_view(), name='all'),
    path('localdetail/<int:pk>', views.localdetail.as_view(), name='localdetail'),
    path('addLocal', views.addLocal.as_view(), name='addLocal'),
    path('updateLocal/<int:pk>', views.updateLocal.as_view(), name='updateLocal'),
    path('deleteLocal/<int:pk>', views.deleteLocal.as_view(), name='deleteLocal'),
    path('local/<int:lid>', views.localdetail, name='local'),
    path('allCats', views.allCats.as_view(), name='allcats'),
    path('addCat', views.addCat.as_view(), name='addCat'),
    path('updateCat/<int:pk>', views.updateCat.as_view(), name='updateCat'),
    path('deleteCat/<int:pk>', views.deleteCat.as_view(), name='deleteCat'),
    path('user/<int:pk>', views.userDetail.as_view(), name='user'),
    path('allUsers', views.allUsers.as_view(), name='allusers'),
    path('allpolls', views.allPolls.as_view(), name='allpolls'),
    path('editSettings/<int:pk>', views.editSettings.as_view(), name='editSettings'),
    path('createSettings',
         views.createSettings.as_view(), name='createSettings'),

] + static(settings.MEDIA_URL,
           document_root=settings.MEDIA_ROOT)
