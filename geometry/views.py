from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from math import pi, pow

# Create your views here.

list_shapes = ['rectangle', 'square', 'circle']


def info_about_shape(request, shape):
    if shape in list_shapes:
        template_path = f'geometry/{shape}.html'
        return render(request, template_path)


def get_rectangle_area(request, width: int, height: int):
    if width is not str and height is not str:
        area = width * height
        return HttpResponse(f'Площадь прямоугодьника со сторономи {width} и {height} равна {area}')
    else:
        return HttpResponseNotFound(
            'Стороны прямоугольника должны быть числами! Попробуйте другие значения.')


def get_square_area(request, width: int):
    if width != 0 and width > 0:
        area = width * width
        return HttpResponse(f'Площадь квадрата со стороной {width} равна {area}')
    else:
        return HttpResponseNotFound(
            'Стороны квадрата должны быть положительми числами!\nПопробуйте другое значение.')


def get_circle_area(request, radius: int):
    if radius:
        area = pi * pow(radius, 2)
        return HttpResponse(f'Площадь круга с радиусом {radius} равна {area}')
    else:
        return HttpResponseNotFound(
            'Радиус кгуга быть числом! Попробуйте другое значение.')


# redirects

def re_get_rectangle_area(request, width: int, height: int):
    redirect_url = reverse('rectangle_name', args=(width, height))
    return HttpResponseRedirect(redirect_url)


def re_get_square_area(request, width: int):
    redirect_url = reverse('square_name', args=(width,))
    return HttpResponseRedirect(redirect_url)


def re_get_circle_area(request, radius: int):
    redirect_url = reverse('circle_name', args=(radius,))
    return HttpResponseRedirect(redirect_url)
