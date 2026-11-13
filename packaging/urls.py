from django.urls import path
from . import views

urlpatterns = [
    path(
        'recommend/<int:order_id>/',
        views.box_recommendation,
        name='box_recommendation'
    ),
]