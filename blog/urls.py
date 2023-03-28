from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name = "blogHome"),
    path("about/",views.index,name = "blogHome"),
    path("contact/",views.index,name = "blogHome"),
    path("tracker/",views.index,name = "blogHome"),
    path("search/",views.index,name = "blogHome"),
    path("productview/",views.index,name = "blogHome"),
    path("checkout/",views.index,name = "blogHome")







]