from django.urls import path, register_converter
from . import views, converters

register_converter(converters.MyDateConverter, 'dd-mm-yyyy')

urlpatterns = [
    path('', views.index),
    path('keanu reeves/', views.keanu_reeves_info),
    path('guinness/', views.get_guinness_world_records),
    path('<dd-mm-yyyy:date>/', views.info_by_date),
    path('<int:week_day>/', views.to_do_info_by_number),
    path('<str:week_day>/', views.to_do_info, name='week-name'),
]
