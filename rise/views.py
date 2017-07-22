from django.shortcuts import render
from .models import getinformation,upfront
from .forms import WireForm,CardForm
from django.shortcuts import render,get_list_or_404,redirect
from django.contrib import messages
# View for for collection banking info
def BankingInfo(request):
    form =WireForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        print (form.cleaned_data.get("title"))
        return redirect('rise:process')
    context ={"form":form}
    return render(request,'rise/home.html',context)
# view to display form to collect card details
def CardInfo(request):
    form =CardForm(request.POST or None)
    if form.is_valid():
        instance =form.save(commit=False)
        instance.save()
        return redirect('rise:complete')
    context ={"card":form}
    return render(request,'rise/card.html',context)
# this view popup on processing 
def Process(request):
    content=""
    return render(request,"rise/processing.html",{'content':content})
def Complete(request):
    content=""
    return render(request,"rise/complete.html",{'content':content})
    