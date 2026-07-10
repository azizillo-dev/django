from django.shortcuts import render, redirect
from .models import Course
from .forms import CourseForm





def home(request):
    return render(request, "home.html")


def list(request):
    courses = Course.objects.all()
    context = {
        "courses" : courses
    }
    return render(request, "list.html", context)


def detail(request, pk):
    course = Course.objects.get(id=pk)
    context = {
        "course":course
    }
    return render(request, "detail.html", context)



def delete(request, pk):
    course = Course.objects.get(id=pk)
    if request.method == "POST":
        course.delete()
        return redirect('list')
    return render(request, 'delete.html', {"course":course})

def create(request):
    form = CourseForm()
    if request.method == "POST":
        form = CourseForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    return render(request, "create.html", context={"form":form})




def update(request, pk):
    course = Course.objects.get(id=pk)
    form = CourseForm(instance=course)
    if request.method == "POST":
        form = CourseForm(data=request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('list')
    context = {"form": form, "course": course}
    return render(request, 'update.html', context)








