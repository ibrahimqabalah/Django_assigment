from django.urls import path 
from . import views
urlpatterns = [
    path('',views.method1),
    path('form',views.display_form),
    path('route1',views.handle_form),
] 