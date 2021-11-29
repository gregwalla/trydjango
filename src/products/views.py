from django.shortcuts import render, get_object_or_404, redirect

from .forms import ProductForm, RawProductForm

from .models import Product

def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = { 'form' : form }
    return render(request, "products/product_create.html", context)

def product_delete_view(request, id): #2:56:30
    obj = get_object_or_404(Product, id = id)
    if request.method == 'POST':
        obj.delete()
        return redirect('../../')
    context = { 'object' : obj}
    return render(request, "products/product_delete.html", context)

def product_detail_view(request):
    obj = Product.objects.get(id=3)
    context = {  'object' : obj }
    return render(request, "products/product_detail.html", context)

def product_list_view(request): #2:58
    queryset = Product.objects.all()
    context = { 'object_list' : queryset }
    return render(request, "products/product_list.html", context)

def render_initial_data(request): #2:49
    initial_data = { 'title': "My initial CFE title",  "description" : "basics"}
    obj = Product.objects.get(id = 40   )  
    form = ProductForm(request.POST or None,  instance = obj)
    context = {'form' : form}
    return render(request, "products/product_create.html", context)

def dynamic_lookup_view(request, id): #2:51, #2:54
    obj = get_object_or_404(Product, id = id)
    context = { 'object' : obj}
    return render(request, "products/product_detail.html", context)
