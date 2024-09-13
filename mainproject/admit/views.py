from django.shortcuts import render
from django.views import View
from .models import *
# Create your views here.

class MainView(View):
    def get(self, request):
        university = University.objects.all()
        context = {
            'university' : university
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

        return self.get(request)

