from django.urls import path
from .views import Home

app_name = 'mainapp'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    # path('', views.home, name='home'),
    # path('signin/', views.signin, name='signin'),
    # path('signup/', views.signup, name='signup'),
    # path('accounts/logout/', views.logout, name='logout'),
]
