from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    # Qo'shimcha yo'laklar shu joyga qo'shiladi
]
