
from django.urls import path

from goods import views


app_name = 'goods'

urlpatterns = [
    path('<slug:category_slug>', views.catalog, name='index'),
<<<<<<< HEAD
    path('<slug:category_slug>/<int:page>/', views.catalog, name='index'),
=======
>>>>>>> 1b16c7b (Normal pagination is added)
    path('product/<slug:product_slug>/', views.product, name='product'),

]
