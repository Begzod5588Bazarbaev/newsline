from django.urls import path
from .views import *

urlpatterns = [
    path('', newsline, name='newsline'),
    path('rubric/<int:rubric_id>/', rubric_list),
    path('news/<int:pk>/',detail),
    path('news/<int:pk>/edit/', edit),
    path('news/<int:pk>/delete/', deletes),
    path('news/create/',create)
]
