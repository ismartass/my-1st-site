from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

days_dict = {
    'monday': 'Вот Ваш список дел на понедельник!!!',
    'tuesday': 'Вот Ваш список дел на вторник!!!',
    'wednesday': 'Вот Ваш список дел на среду!!!',
    'thursday': 'Вот Ваш список дел на четверг!!!',
    'friday': 'Вот Ваш список дел на пятницу!!!',
    'saturday': 'Вот Ваш список дел на субботу!!!',
    'sunday': 'Вот Ваш список дел на воскресенье!!!'
}

keanu_info_dict = {
    'year_born': 1964,
    'city_born': 'Бейрут',
    'movie_name': 'На гребне волны'
}


def index(request):
    days_list = list(days_dict)
    li_days = ''
    for day in days_list:
        redirect_path = reverse('week-name', args=(day,))
        li_days += f"<li> <a href='{redirect_path}'> {day.title()} </a> </li>"
    response = f'''<ol>
        {li_days}
        </ol>'''
    return HttpResponse(response)


def info_by_date(request, date):
    return HttpResponse(f'Вот Ваша дата!  > {date} <')


def keanu_reeves_info(request):
    return render(request, 'week/Keanu Reeves.html.', context=keanu_info_dict)


def get_guinness_world_records(request):
    context = {
        'power_man': 'Narve Laeret',
        'bar_name': 'Bob’s BBQ & Grill',
        'count_needle': 1790,
    }
    return render(request, 'week/guinnessworldrecords.html', context=context)


def to_do_info(request, week_day: str):
    day_case = days_dict.get(week_day, None)
    if day_case:
        return HttpResponse(day_case)
    else:
        return HttpResponseNotFound(f'Неизвестный день недели! - {week_day}')


def to_do_info_by_number(request, week_day: int):
    if week_day in range(1, 8):
        days_list = list(days_dict)
        day = days_list[week_day - 1]
        redirect_url = reverse('week-name', args=(day,))
        return HttpResponseRedirect(redirect_url)
    else:
        return HttpResponseNotFound(f'Неверный номер дня недели! - {week_day}')
