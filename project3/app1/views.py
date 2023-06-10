from django.shortcuts import render,redirect
from .models import Item
from django.views.generic.edit import UpdateView
# Create your views here.

def index(request):
    obj1=Item.objects.all()
    if request.method=='POST':
        slno=request.POST.get('slno','')
        name=request.POST.get('name','')
        desc=request.POST.get('desc','')
        x=Item(slno=slno,name=name,desc=desc)
        x.save()
    return render(request,'index.html',{'obj':obj1})

def delete(request,id):
    task=Item.objects.get(id=id)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request, id):
    task = Item.objects.get(id=id)

    if request.method == 'POST':
        slno = request.POST.get('slno')
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        Item.objects.filter(id=id).update(slno=slno,name=name,desc=desc)
        return redirect('/')
    return render(request, 'update.html', {'task': task})