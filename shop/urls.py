from django.urls import path 
from . import views 

# Here are my views config
app_name = 'shop'
urlpatterns = [
     path('', views.index, name='home'),
     path('product/',views.product_list,name='product'),
     #path('register', views.register, name='register'),
     #path('login/', views.login_page, name='login'),
     path('logout/', views.logout_page, name='logout'),
     path('profile/', views.profile, name='profile'),
     path('update_profile/' , views.update_profile, name='update_profile')
    ]