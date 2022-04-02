from django.urls import path
from . import views


urlpatterns = [
    path('<shape>/', views.info_about_shape),
    path('rectangle/<int:width>/<int:height>/', views.get_rectangle_area, name='rectangle_name'),
    path('square/<int:width>/', views.get_square_area, name='square_name'),
    path('circle/<int:radius>/', views.get_circle_area, name='circle_name'),
    path('get_rectangle_area/<int:width>/<int:height>/', views.re_get_rectangle_area),
    path('get_square_area/<int:width>/', views.re_get_square_area),
    path('get_circle_area/<int:radius>/', views.re_get_circle_area, ),
]
