from django.urls import path
from . import views

urlpatterns = [
    # ... your other url patterns here ...
    path('register/', views.register, name='register'),
]