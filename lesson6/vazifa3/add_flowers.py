import os
import django

# Django sozlamalarini yuklaymiz
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conf.settings')
django.setup()

from flowers.models import Flower

flowers_data = [
    {
        "name": "Qizil Atirgul",
        "price": 50000,
        "desc": "Sifatli, xushbo'y hidga ega qizil atirgul. Sovg'alar uchun eng mashhur tanlov.",
        "is_tikonli": True,
        "color": "Qizil"
    },
    {
        "name": "Oq Atirgul",
        "price": 55000,
        "desc": "Toza va beg'uborlik ramzi bo'lgan oq atirgul. To'y va bayramlar uchun ideal.",
        "is_tikonli": True,
        "color": "Oq"
    },
    {
        "name": "Sariq Lola",
        "price": 30000,
        "desc": "Bahor faslining eng yorqin va go'zal guli. Xonaga quvnoq kayfiyat bag'ishlaydi.",
        "is_tikonli": False,
        "color": "Sariq"
    },
    {
        "name": "Moychechak",
        "price": 25000,
        "desc": "Tabiiy va sodda go'zallik. Tinchlantiruvchi hidga va chiroyli barglarga ega.",
        "is_tikonli": False,
        "color": "Oq-Sariq"
    },
    {
        "name": "Siyohrang Binafsha",
        "price": 40000,
        "desc": "Kichik tuvakda o'sishga moslashgan, nafis siyohrang dekorativ gul.",
        "is_tikonli": False,
        "color": "Siyohrang"
    },
    {
        "name": "Pushti Xrizantema",
        "price": 45000,
        "desc": "Uzoq vaqt so'lmasdan turadigan, juda ko'p bargli chiroyli va chidamli gul.",
        "is_tikonli": False,
        "color": "Pushti"
    },
    {
        "name": "Dekorativ Kaktus",
        "price": 60000,
        "desc": "Suvni ko'p talab qilmaydigan, kompyuter stoli uchun juda mos kaktus.",
        "is_tikonli": True,
        "color": "Yashil"
    },
    {
        "name": "Qalampirgul",
        "price": 35000,
        "desc": "O'ziga xos shaklga va chidamlilikka ega bo'lgan klassik go'zal gul.",
        "is_tikonli": False,
        "color": "Qizil"
    },
    {
        "name": "Kralicha Orxideya",
        "price": 150000,
        "desc": "Tropik mintaqa guli, juda nafis va premium darajadagi eng chiroyli sovg'a.",
        "is_tikonli": False,
        "color": "Oq-Pushti"
    },
    {
        "name": "Xushbo'y Nilufar",
        "price": 80000,
        "desc": "Juda kuchli va yodda qolarli xushbo'y ifor tarqatuvchi yirik go'zal gul.",
        "is_tikonli": False,
        "color": "Oq"
    }
]

print("10 ta yangi gul qo'shish boshlandi...\n")
for data in flowers_data:
    flower = Flower.objects.create(**data)
    print(f"Qo'shildi: {flower.name} | Narxi: {flower.price} so'm | Rangi: {flower.color} | Tikonlimi: {'Ha' if flower.is_tikonli else 'Yoq'}")

print(f"\nJami gullar soni: {Flower.objects.count()} ta.")
