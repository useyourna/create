from django.shortcuts import render

def first(request):
    return render(request, 'first.html')
    
    
def second(request):
    return render(request, 'second.html')
    
    
def third(request):
    return render(request, 'third.html')
# Create your views here.
