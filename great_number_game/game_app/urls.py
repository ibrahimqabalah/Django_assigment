from django.urls import path
from . import views

urlpatterns = [
    path('',views.index ),
    path('guess',views.guess_num),
    path('reset',views.play_again),
]


 