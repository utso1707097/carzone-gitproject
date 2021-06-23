from django.urls import path
from .  import views

urlpatterns = [
  	path('',views.cars,name='cars'),
  	path('<int:id>',views.car_detail,name='car_detail'),
  	path('search',views.search,name='search'),
	path('checkout',views.checkout,name='checkout'),
	path('payment',views.payment,name='payment'),
]