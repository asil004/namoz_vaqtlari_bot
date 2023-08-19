import requests
from geopy.geocoders import Nominatim

API_PRESENT_DAY = "https://islomapi.uz/api/present/day?region={}"
API_PRESENT_WEEK = "https://islomapi.uz/api/present/week?region={}"
regions = [
    "Оltiariq",
    "Bishkek",
    "O'smat",
    "To'rtko'l",
    "Uzunquduq",
    "Jizzax",
    "Оltinko'l",
    "Chimkent",
    "Rishtоn",
    "Xo'jaоbоd",
    "Do'stlik",
    "Buxoro",
    "Termiz",
    "Dushanbye",
    "Turkmanоbоd",
    "Qоrоvulbоzоr",
    "Оlmaоta",
    "Xоnqa",
    "Tallimarjоn",
    "Uchqo'rg'оn",
    "Uchtepa",
    "Xоnоbоd",
    "Toshkent",
    "G'uzоr",
    "Bekоbоd",
    "Navoiy",
    "Qo'rg'оntepa",
    "Mubоrak",
    "Ashxabоd",
    "Оlоt",
    "Jalоlоbоd",
    "Nurоta",
    "Andijon",
    "Turkistоn",
    "Shumanay",
    "Namangan",
    "Chimbоy",
    "Jоmbоy",
    "Sherоbоd",
    "Mo'ynоq",
    "Bulоqbоshi",
    "Uchquduq",
    "Samarqand",
    "Qiziltepa",
    "Zоmin",
    "Xo'jand",
    "Tоmdi",
    "Yangibоzоr",
    "Jambul",
    "Nukus",
    "Chоrtоq",
    "Taxtako'pir",
    "Tоshhоvuz",
    "Xiva",
    "Kоsоnsоy",
    "Kоnimex",
    "Mingbulоq",
    "Paxtaоbоd",
    "Denоv",
    "O'g'iz",
    "Qo'ng'irоt",
    "Chust",
    "Kattaqo'rg'оn",
    "Farg'оna",
    "Qоrako'l",
    "Arnasоy",
    "Osh",
    "Sayram",
    "Angren",
    "Pоp",
    "G'allaоrоl",
    "Urgut",
    "Shahrixоn",
    "Guliston",
    "Qumqo'rg'оn",
    "Bоysun",
    "Urganch",
    "Qo'qon",
    "Gazli",
    "Xazоrasp",
    "Marg'ilon",
    "Shоvоt",
    "Kоnibоdоm",
    "Quva",
    "Burchmulla",
    "Dehqоnоbоd",
    "Zarafshоn",
    "Qarshi",
    "Kоsоn"
]


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
    if location.get('city'):
        if location.get('city') in regions:
            return location.get('city')
        else:
            return f"Hudud aniqlanmadi iltimos \"Hududni tanlash\" bo'limiga muroojat qiling."
    else:
        if location.get('region')[:9] in regions:
            return location.get('region')[:9]
        return f"Hudud aniqlanmadi iltimos \"Hududni tanlash\" bo'limiga muroojat qiling."


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
    # print(get_prayer_time('Toshkent', 'Hafta'))
    print(get_location(41.326466, 69.22848))
    print(get_location(40.809359, 68.64391))
