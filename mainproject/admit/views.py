from django.shortcuts import render
from django.views import View
from .models import *
# Create your views here.

class MainView(View):
    def get(self, request, searched_value=""):
        university = University.objects.all()
        context = {
            'university' : university.filter(name__contains=searched_value),
            'searched_value':searched_value
        }
        return render(request, 'main.html', context)

    def post(self, request):
        print(request.POST)
        data = request.POST
        button_type = request.POST.get('buttonType', None)

        if button_type == 'create_uni':
            name = request.POST.get('uni_name')
            daad_url = request.POST.get('daad_url')   
            University.objects.create(name=name,daad_url=daad_url) 

        if button_type == 'search':
            searched_value = request.POST.get('searched_value')
            return self.get(request, searched_value=searched_value)

        return self.get(request)

