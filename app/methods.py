import requests
from geopy.geocoders import Nominatim

API_PRESENT_DAY = "https://islomapi.uz/api/present/day?region={}"
API_PRESENT_WEEK = "https://islomapi.uz/api/present/week?region={}"


def get_location(lat, long):
    """
    Bu method lokatsiyadan foydalanib shahrni topadi!
    :param lat:
    :param long:
    :return:
    """
    geolocator = Nominatim(user_agent='MyNamazVaqtlariBot', timeout=10)
    location = geolocator.reverse(f"{lat},{long}")
    location = location.raw['address']
    return location.get('city')


def get_prayer_time(location, select):
    """
    Bu method shaharni olib tanlangan vaqt bo'yivcha namoz vaqtlarini qaytaradi
    :return:
    """
    if select == 'Bugun':
        response = requests.get(url=API_PRESENT_DAY.format(location))
        if response.status_code == 200:
            return response.json()
        else:
            print("Xatolik sodir bo'ldi.Shaharni to'g'ri tanlaganingizga ishonch hosil qiling!\nStatus kodi:",
                  response.status_code)
    elif select == 'Hafta':
        response = requests.get(url=API_PRESENT_WEEK.format(location))
        if response.status_code == 200:
            return response.json()
        else:
            print("Xatolik sodir bo'ldi.Shaharni to'g'ri tanlaganingizga ishonch hosil qiling!\nStatus kodi:",
                  response.status_code)
    else:
        return False


if __name__ == '__main__':
    print(get_prayer_time('Toshkent', 'Hafta'))
    # print(get_location(41.326466, 69.22848))
