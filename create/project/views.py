from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentResistration
from .models import User

# Create your views here.
#this post is add data 
def addandpost(request):
  if request.method == 'POST':
    fm=StudentResistration(request.POST)
    if fm.is_valid():
      nm = fm.cleaned_data['name']
      em = fm.cleaned_data['email']
      mb = fm.cleaned_data['mobile']
      pd = fm.cleaned_data['password']
      reg = User(name=nm,email=em,mobile=mb,password=pd)
      reg.save()
      fm=StudentResistration()  
  else:
    fm=StudentResistration()  
  data=User.objects.all()
  return render(request, 'project/addandpost.html',{'form':fm, 'dt':data})

#delete data on addpost
def delete(request,id):
  if request.method=='POST':
    pi = User.objects.get(pk=id)
    pi.delete()
    return HttpResponseRedirect('/')

#update_data on dashboard
    
def update_data(request, id):
  if request.method=='POST':
    pi = User.objects.get(pk=id)
    fm = StudentResistration(request.POST, instance=pi)
    if fm.is_valid():
      fm.save()
  else:
    pi = User.objects.get(pk=id)
    fm = StudentResistration(instance=pi)    
  return render(request, 'project/update.html', {'form':fm})