from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

# Create your views here.
class Index(View):
    def get(self, request):
        param = {}
        param['name'] = 'Django'
        return render(request, 'base.html', param)
        #return HttpResponse('You call me by GET ')
    def post(self, request):
        return HttpResponse('You call me by POST')

#def index(request):
#    if request.method == 'GET':
#        return HttpResponse('You call me by GET ')
#    elif request.method == 'POST':
#        return HttpResponse('You call me by POST')
