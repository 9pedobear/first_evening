from django.shortcuts import render
from .models import Blog

def index(request):
    data = Blog.objects.all()
    context = {
        'data' : data
    }
    return render(request,
                  template_name='index.html',
                  context=context)

