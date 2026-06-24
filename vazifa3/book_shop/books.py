from django.http import HttpResponse

books = {
	1: {"title": "Olamning Quloqchasi", "author": "Xurshid Davron", "price": "25000"},
	2: {"title": "Sariq Devni minib", "author": "O'tkir Hoshimov", "price": "18000"},
	3: {"title": "Zulmat va Nur", "author": "Muhammad Yusuf", "price": "22000"},
	4: {"title": "Bahor kelar", "author": "Gulsanam Mamazoitova", "price": "15000"},
	5: {"title": "Ikki dunyo", "author": "Abdulla Qahhor", "price": "20000"},
	6: {"title": "Kitobxon", "author": "Rustam Rahimov", "price": "17000"},
}


def get_books(request):
	result = ""

	for book_id, book in books.items():
		result += f"ID: {book_id} Title: {book['title']} Author: {book['author']} Price: {book['price']}"

	return HttpResponse(result)





def get_authors(request):
	result = ""
	for k, v in books.items():
		result += f"ID: {k} : {v['author']}"

	return HttpResponse(result)



def get_prices(request):
	result = ""
	for k, v in books.items():
		result += f"ID: {k} Title: {v['title']} Price: {v['price']}"

	return HttpResponse(result)


def get_titles(request):
	result = ""
	for k, v in books.items():
		result += f"ID: {k} Title: {v['title']}"

	return HttpResponse(result)


def get_count(request):
	count = len(books)
	return HttpResponse(f"Total books: {count}")








