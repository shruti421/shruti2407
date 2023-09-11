from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('index/',views.index),
    path('index2/<str:cat>',views.index2),
    path('view/<int:id>',views.view),
    path('base/',views.base),
    path('myBag/',views.my_bag),

]
