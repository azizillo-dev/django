from django.http import HttpResponse

courses = {
    1: {
        "name": "Python Backend",
        "days": "Dushanba, Chorshanba, Juma",
        "time": "18:00 - 20:00",
        "teacher": "Shaxriyor"
    },
    2: {
        "name": "Frontend React",
        "days": "Seshanba, Payshanba, Shanba",
        "time": "14:00 - 16:00",
        "teacher": "Javohir"
    },
    3: {
        "name": "Django",
        "days": "Dushanba, Chorshanba",
        "time": "20:00 - 22:00",
        "teacher": "Sardor"
    },
    4: {
        "name": "Data Science",
        "days": "Seshanba, Payshanba",
        "time": "10:00 - 12:00",
        "teacher": "Azizbek"
    },
    5: {
        "name": "Flutter",
        "days": "Chorshanba, Juma",
        "time": "16:00 - 18:00",
        "teacher": "Muhammadali"
    }
}


def get_courses(request):
    result = ""

    for course_id, course in courses.items():
        result += (
            f"ID: {course_id}"
            f"Name: {course['name']}"
            f"Days: {course['days']}"
            f"Time: {course['time']}"
            f"Teacher: {course['teacher']}"
        )

    return HttpResponse(result)







