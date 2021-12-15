from django.urls import path
from . import views

urlpatterns = [
    path("", views.index1, name="Home"),
    path("shop/about/", views.about, name="AboutUs"),
    path("shop/contact/", views.contact, name="ContactUs"),
    path("shop/tracker/", views.tracker, name="TrackingStatus"),
    path("shop/search/", views.search, name="Search"),
    path("shop/products/<int:myid>", views.productView, name="ProductView"),
    path("shop/checkout/", views.checkout, name="Checkout"),
]
