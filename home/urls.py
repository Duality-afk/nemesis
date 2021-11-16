
from django.urls import path,include
from home import views

urlpatterns = [
 
  path('', views.dashboard, name='dashboard'),
  path('login/',views.loginpage,name="loginpage"),
  path('logout/', views.handlelogout,name="logout"),
  path('register',views.registerpage,name="registerpage"),
  path('delete', views.delete,name="delete"),
  path('update', views.update, name="updatepage")

  

    
]
