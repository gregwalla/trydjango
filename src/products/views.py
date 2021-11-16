from django.shortcuts import render

from .forms import ProductForm, RawProductForm

from .models import Product



# Create your views here.
def product_create_view(request):
    context = {}
    return render(request, "products/product_create.html", context)


# def product_create_view(request):
#     print(f'get request : {request.GET}')
#     print(f'post request : {request.POST}')
#     title = request.POST
#     context = {
#          }
#     #print(f'context : {context}')
#     return render(request, "products/product_create.html", context)

# def product_create_view(request):
#     form = ProductForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = ProductForm()

#     context = {
#         'form' : form
#          }
#     #print(f'context : {context}')
#     return render(request, "products/product_create.html", context)


def product_detail_view(request):
    obj = Product.objects.get(id=3)
    context = {
        'object' : obj
         }
    #print(f'context : {context}')
    return render(request, "products/product_detail.html", context)