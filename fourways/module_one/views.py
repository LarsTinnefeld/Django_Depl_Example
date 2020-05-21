from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'module_one/index.html')


def other(request):
    return render(request, 'module_one/other.html')


def relative_url_templates(request):
    return render(request, 'module_one/relative_url_templates.html')
