from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('add/',views.add,name='add'),
    path('add2/',views.add2,name='add2'),
    path('todo/',views.todo,name='todo'),
    path('complete/',views.complete,name='complete'),
    path('details/<pk>/',views.details,name='details'),
    path('delete/<pk>/',views.delete,name='delete'),
    path('update/<pk>/',views.update,name='update'),
    path('update2/<pk>/',views.update2,name='update2'),
    path('search/', views.search, name='search'),
    path('toggle_complete/<pk>', views.toggle_complete, name='toggle_complete'),
  
]
