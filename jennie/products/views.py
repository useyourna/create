from django.shortcuts import render, redirect, get_object_or_404
from .models  import Product
import pdb


def list(request):
    products = Product.objects.all()
    return render(request, 'list.html', {'all_products':products})

def create(request):
    if request.method == "POST":
        title= request.POST.get('title')
        description = request.POST.get('description')
        price = request.POST.get('price')
        product=Product.objects.create(title=title, price=price, description=description) 
        product.save() 
        return redirect('list')
        
    return render(request, 'create.html')
    


def show(request, id):
    product = get_object_or_404(Product, pk=id)
    default_view_count = product.view_count
    product.view_count = default_view_count + 1    
    return render(request, 'show.html', {'product':product})
    
def edit(request, id):
    product = get_object_or_404(Product, pk=id)
    return render(request, 'edit.html', {'product': product})
    

def update(request, id):
    if request.method == "POST":
        product = Product.objects.get(pk=id)
        title = request.POST.get('title')
        description = request.POST.get('description')
        price = int(request.POST.get('price'))
        product.title = title
        product.description = description
        product.price = price
        product.save()
    return redirect('products:show', product.pk)
    

def delete(request, id):
    if request.method == "POST":
        product= Product.objects.get(pk=id)
        product.delete()
    return redirect('list')
# Create your views here.