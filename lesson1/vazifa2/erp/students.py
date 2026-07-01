from django.http import HttpResponse

students = {
    1: "Ali",
    2: "Vali",
    3: "Hasan",
    4: "Husan",
    5: "Aziza",
    6: "Madina",
    7: "Jasur",
    8: "Sardor",
    9: "Muhammad",
    10: "Zuhra"
}

def get_students(request):
    result = ""

    for student_id, name in students.items():
        result += f"ID: {student_id} Name: {name}<br>"

    return HttpResponse(result)







 












        
