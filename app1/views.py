from django.shortcuts import render

# Create your views here.
def operation2(request): 
    k=2001
    d={'a':k % 400}
    return render(request,'if-elif-else.html',d)
    
