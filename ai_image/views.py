from django.shortcuts import render
from django.http import HttpResponse
from .models import Document

def index(request):
    return render(request,"ai_image/index.html")

def upload(request):
    if request.method=="POST":
        form=DocumentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect(upload)
        else:
            form=DocumentForm()
            obj=Document.objects.all()

        return render(request,"ai_image/model_form_upload.html",){
            "form":form,
            "obj":obj
        }
