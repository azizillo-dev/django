import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conf.settings')
django.setup()

from mebellar.models import Mebel

def populate():
    mebellar_data = [
        {
            "name": "Luks Charm Divan \"Chesterfield\"",
            "price": 7500000.00,
            "category": "divan",
            "material": "Tabiiy charm va yong'oq yog'ochi",
            "color": "To'q jigarrang",
            "count": 5,
            "desc": "Mehmonxona uchun maxsus ishlangan, yuqori sifatli tabiiy charm va qattiq yog'ochdan yasalgan klassik divan.",
            "is_have": True
        },
        {
            "name": "Katta Ovqatlanish Stoli \"Royal Oak\"",
            "price": 4200000.00,
            "category": "stol",
            "material": "Eman (dub) yog'ochi",
            "color": "Och yog'och rangi",
            "count": 8,
            "desc": "12 kishilik oilaviy ovqatlanish uchun mo'ljallangan mustahkam eman yog'ochidan tayyorlangan stol.",
            "is_have": True
        },
        {
            "name": "Yumshoq Stul \"Velvet Elegance\"",
            "price": 650000.00,
            "category": "stul",
            "material": "Baxmal mato va metall",
            "color": "Zumrad yashil",
            "count": 24,
            "desc": "Ovqatlanish stoli yoki ofis uchun qulay va zamonaviy baxmal qoplamali stul.",
            "is_have": True
        },
        {
            "name": "Kupe Shkaf \"Milano 3-Eshikli\"",
            "price": 8900000.00,
            "category": "shkaf",
            "material": "MDF va ko'zgu",
            "color": "Oq matoviy",
            "count": 3,
            "desc": "Yotoqxona uchun katta hajmli, ko'zgyli va silliq ochiluvchi kupe shkaf.",
            "is_have": True
        },
        {
            "name": "Ikki Kishilik Karavot \"Dreamer King\"",
            "price": 6800000.00,
            "category": "karavot",
            "material": "Yog'och va ortopedik asos",
            "color": "Kulrang",
            "count": 6,
            "desc": "180x200 sm o'lchamdagi, ortopedik matrasingiz uchun mukammal mos tushuvchi ikki kishilik karavot.",
            "is_have": True
        },
        {
            "name": "Yig'iluvchi Divan \"Transform-Loft\"",
            "price": 5400000.00,
            "category": "divan",
            "material": "Mikrovelyur va po'lat",
            "color": "To'q ko'k",
            "count": 10,
            "desc": "Kunduzi qulay o'tirish, kechqurun esa yotoq sifatida foydalanish mumkin bo'lgan yig'iluvchi divan.",
            "is_have": True
        },
        {
            "name": "Yozuv Stoli \"Ergo-Office\"",
            "price": 2100000.00,
            "category": "stol",
            "material": "LDSP va temir karkas",
            "color": "Qora va yog'och",
            "count": 15,
            "desc": "Dasturchilar va ofis xodimlari uchun ergonomik dizayndagi zamonaviy yozuv stoli.",
            "is_have": True
        },
        {
            "name": "Kitob Shkafi \"Nordic Bookshelf\"",
            "price": 3200000.00,
            "category": "shkaf",
            "material": "Qarag'ay yog'ochi",
            "color": "Och jigarrang",
            "count": 7,
            "desc": "Uy kutubxonasi yoki ish xonasi uchun 5 qavatli ochiq va yopiq javonli kitob shkafi.",
            "is_have": True
        },
        {
            "name": "Bar Stuli \"Loft Black\"",
            "price": 850000.00,
            "category": "stul",
            "material": "Eko-charm va metall",
            "color": "Qora",
            "count": 18,
            "desc": "Oshxona bar stoykasi uchun balandligi sozlanadigan zamonaviy bar stuli.",
            "is_have": True
        },
        {
            "name": "Jurnal Stoli \"Glass & Marble\"",
            "price": 1600000.00,
            "category": "boshqa",
            "material": "Chiniqqan shisha va marmar naqshli asos",
            "color": "Oq va tilla",
            "count": 12,
            "desc": "Mehmonxonada divan oldiga qo'yish uchun nafis shisha va marmar naqshli jurnal stoli.",
            "is_have": True
        }
    ]

    print("Mebellar qo'shish boshlandi...")
    count = 0
    for item in mebellar_data:
        obj, created = Mebel.objects.get_or_create(
            name=item["name"],
            defaults=item
        )
        if created:
            count += 1
            print(f"[+] Yangi qo'shildi ({item['category']}): {item['name']}")
        else:
            print(f"[=] Mavjud: {item['name']}")
            
    print(f"\nJami qo'shilgan yangi ma'lumotlar soni: {count}")
    print(f"Bazadagi umumiy mebellar soni: {Mebel.objects.count()}")

if __name__ == "__main__":
    populate()
