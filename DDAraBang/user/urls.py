from django.urls import path
from . import views
from config import views as config_views
app_name = "user"


urlpatterns = [
    path('', config_views.main_html , name='DDmainpage'), #community views의 main_html 함수 호출 
    path("login", views.LoginView.as_view(), name="login"),
    path("logout", views.log_out, name="logout"),
    path("sigup", views.SignUpView.as_view(), name="signup"),
]