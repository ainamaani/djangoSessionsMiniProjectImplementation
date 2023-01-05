from django.urls import path
from . import views

urlpatterns=[
    path('items/',views.Items,name='items'),
    path('item/<int:id>', views.SingleItem, name='single')
]