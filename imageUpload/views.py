from django.shortcuts import render,redirect
from .models import Image
from .forms import ImageForm


def upload_image(request):
    if request.method=='POST':
        form=ImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form=ImageForm()
    return render(request,'upload_image.html',{'form':form})

def image_list(request):
    images=Image.objects.all()
    return render(request,'image_list.html',{'images':images})

def delete_image(request,id):
    if request.method=='POST':
        image=Image.objects.get(pk=id)
        image.delete()
    return redirect('/')

def update_image(request,id):
    image=Image.objects.get(pk=id)
    if request.method=='POST':
        form=ImageForm(request.POST,request.FILES,instance=image)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form=ImageForm(instance=image)
    return render(request,'image_list.html',{'form':form})