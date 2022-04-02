from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.


zodiac_dict = {
    'aries': 'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).',
    'taurus': 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).',
    'gemini': 'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).',
    'cancer': 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).',
    'leo': 'Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).',
    'virgo': 'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).',
    'libra': 'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
    'scorpio': 'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).',
    'sagittarius': 'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).',
    'capricorn': 'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).',
    'aquarius': 'Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля)',
    'pisces': 'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).'
}

zodiac_dict_date = {
    "aries": [(21, 3), (20, 4)],
    "taurus": [(21, 4), (21, 5)],
    "gemini": [(22, 5), (21, 6)],
    "cancer": [(22, 6), (22, 7)],
    "leo": [(23, 7), (21, 8)],
    "virgo": [(22, 8), (23, 9)],
    "libra": [(24, 9), (23, 10)],
    "scorpio": [(24, 10), (22, 11)],
    "sagittarius": [(23, 11), (22, 12)],
    "capricorn": [(23, 12), (20, 1)],
    "aquarius": [(21, 1), (19, 2)],
    "pisces": [(20, 2), (20, 3)]
}

zodiac_type_dict = {
    'fire': ['aries', 'leo', 'sagittarius'],
    'earth': ['taurus', 'virgo', 'capricorn'],
    'air': ['gemini', 'libra', 'aquarius'],
    'water': ['cancer', 'scorpio', 'pisces']
}

zodiac_type_dict_2 = {
    'aries': 'fire',
    'leo': 'fire',
    'sagittarius': 'fire',
    'taurus': 'earth',
    'virgo': 'earth',
    'capricorn': 'earth',
    'gemini': 'air',
    'libra': 'air',
    'aquarius': 'air',
    'cancer': 'water',
    'scorpio': 'water',
    'pisces': 'water',

}

# redirect_path = reverse('horoscope_name', args=(sign,))
# li_elements += f"<li> <a href={redirect_path}> {sign.title()} </a> </li>"
# response = f''' <h2><ol>
#     {li_elements}
#     </ol></h2>'''


def index(request):
    zodiac_list = list(zodiac_dict)
    context = {
        'zodiac_list': zodiac_list
    }
    return render(request, 'horoscope/index.html', context=context)


def get_type(request):
    list_zodiac_type = list(zodiac_type_dict)
    context = {
        'list_zodiac_type': list_zodiac_type
    }
    return render(request, 'horoscope/zodiac_type.html', context=context)


def get_signs_zodiac_by_type(request, element):
    list_sign_type = zodiac_type_dict.get(element)
    context = {
        'title': element,
        'list_sign_type': list_sign_type
    }
    return render(request, 'horoscope/zodiac_sign_by_type.html', context=context)


def get_info_about_sign_zodiac(request, sign_zodiac: str):
    zodiac_data = {
        'title': sign_zodiac,
        'description': zodiac_dict.get(sign_zodiac, None),
        'sign_type': zodiac_type_dict_2.get(sign_zodiac),
    }
    return render(request, 'horoscope/zodiac_info.html', context=zodiac_data)


def get_info_about_sign_zodiac_by_number(request, sign_zodiac: int):
    zodiac_list = list(zodiac_dict)
    if sign_zodiac > len(zodiac_list) or sign_zodiac == 0:
        return HttpResponseNotFound(f'Не существующий номер зодиака {sign_zodiac}')
    name_zodiac = zodiac_list[sign_zodiac - 1]
    redirect_url = reverse('horoscope_name', args=(name_zodiac,))
    return HttpResponseRedirect(redirect_url)


def info_by_date(request, date):
    return HttpResponse(f'Вот Ваша дата! - {date}')


def info_day(request, month, day):
    for elem in zodiac_dict_date:
        if month == zodiac_dict_date[elem][0][1] and zodiac_dict_date[elem][0][0] <= day <= 31 or \
                month == zodiac_dict_date[elem][1][1] and 1 <= day <= zodiac_dict_date[elem][1][0]:
            redirect_url = reverse('horoscope_name', args=(elem,))
            return HttpResponseRedirect(redirect_url)
    else:
        return HttpResponseNotFound(f'Несуществующий месяц - {month} или несуществующий день - {day}')
