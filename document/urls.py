from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",views.index,name="index"),
    path("login/",views.login,name="login"),
    path("signup/",views.signup,name="signup"),
    path("signup1/",views.Signup1.as_view(),name="signup1"),
    path("login1/",views.Login1.as_view(),name="login1"),
    path("logout/",views.logout,name="logout"),
    path("upload/",views.upload,name="upload"),
    path('imge/',views.img,name="image"),
    path('img1/',views.Img1.as_view(),name="img1"),
    path('pdf/',views.pdf,name="pdf"),
  	path('ppt/',views.ppt,name="ppt"),
  	path('ppt1/',views.Ppt1.as_view(),name="ppt1"),
  	path('show/',views.show,name="show"),
    path('sendmail/',views.sendmail,name="mail"),
    path('mail1/',views.Mail1.as_view(),name="mail1"),
    path('verify/',views.verify.as_view(),name="verify"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
