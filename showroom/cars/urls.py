from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views

urlpatterns = [

    path('', login_required(views.cars_home), name='cars_home'),
    path('cars_create/', login_required(views.cars_create), name='cars_create'),
    path('update/', login_required(views.cars_update), name='cars_update'),
    path('cars_del/<car_id>/', login_required(views.cars_del), name='cars_del'),
    path('category_filter/', login_required(views.category_filter), name='category_filter'),

    # api response
    path('get_cars_data/', views.get_cars_data, name='get_cars_data'),
]
