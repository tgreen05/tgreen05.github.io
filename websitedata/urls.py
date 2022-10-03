
from django.contrib import admin
from django.urls import path
from tgreen import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	
	path('register_user/', views.registerUser, name='register_user'),
	path('login/', views.loginPage, name='login'),
	path('logout/', views.logOut, name='logout'),


    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('download/', views.download, name='download'),
    path('delete_file/<str:pk>', views.deleteFile, name='delete_file'),
    path('update_file/<str:pk>', views.updateFile, name='update_file'),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)