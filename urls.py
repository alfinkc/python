from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name='index'),
    path('register',views.register,name='register'),
    path('login1',views.login1,name='login1'),
    path('userhome',views.userhome,name='userhome'),
    path('profile',views.profile,name='profile'),
    path('update/<int:pk>',views.update,name='update'),
    path('updatedata/<int:pk>',views.updatedata,name='updatedata'),
    path('delete/<int:pk>',views.delete,name='delete'),
]
urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)