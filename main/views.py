from django.shortcuts import render
from main.models import Jobs


# Create your views here.


def index(request):
    jobs = Jobs.objects.all()
    context = {"jobs": jobs}

    return render(request, "main/index.html", context=context)


def about(request):
    return render(request, "main/about.html")


# def more_designs(request):
#     rooms = RoomInspire.objects.all()
#     context = {"rooms": rooms}
#     return render(request, "main/design.html", context=context)
