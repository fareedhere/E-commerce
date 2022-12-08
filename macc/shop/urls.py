from django.urls import path
from . import views





urlpatterns = [
    path('',views.index,name='Shophome') ,
    path('about/',views.about,name='about'), 
    path('contact/',views.contact,name='contact') ,
    path('tracker/',views.tracker,name='TrackingStatus'), 
    path('search/',views.search,name='Search') ,
    path("products/<int:myid>", views.productView, name="ProductView"), 
    path('checkout/',views.checkout,name='checkout') ,
    path('handlerequest/',views.handlerequest,name='handleRequest') ,
    path('search/',views.search,name='search') ,
]
