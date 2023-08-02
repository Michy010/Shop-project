from django.urls import path 
from . import views 

# Here are my views config
app_name ='shop'
urlpatterns = [
    path('', views.index, name='home'),
    path('product/',views.product_list,name='Product'),
    ]