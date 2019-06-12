from django.shortcuts import render
from NeisAssistant.forms import Form
from .models import Teachers

# Create your views here.

def write(request):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            form.save()
    else :
        form = Form()
    return render(request, 'write.html', {'form':form})

def list(request):
    teacherlist = Teachers.objects.all()
    return render(request, 'list.html', {'teacherlist':teacherlist})

def view(request, tId):
    teacher = Teachers.objects.get(tId = tId)
    return render(request, 'view.html', {'teacher':teacher})

