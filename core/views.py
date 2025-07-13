from django.shortcuts import render

from core.models import Slider


# Create your views here.

def index(request):
    sliders = Slider.objects.all()


    context = {
    'sliders':sliders
    }

    return render(request, 'central/index.html',context)
