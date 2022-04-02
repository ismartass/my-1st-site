from django.urls import path, register_converter
from . import views, converters


register_converter(converters.MyDateConverter, 'dd-mm-yyyy')


urlpatterns = [
    path('', views.index, name='horoscope_index'),
    path('<dd-mm-yyyy:date>/', views.info_by_date),
    path('type/', views.get_type, name='horoscope_types'),
    path('type/<element>', views.get_signs_zodiac_by_type, name='horoscope_type'),
    path('<int:sign_zodiac>/', views.get_info_about_sign_zodiac_by_number),
    path('<str:sign_zodiac>/', views.get_info_about_sign_zodiac, name='horoscope_name'),
    path('<int:month>/<int:day>/', views.info_day),

]
