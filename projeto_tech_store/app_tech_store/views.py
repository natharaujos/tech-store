from django.shortcuts import render
from .models import Product

def home(request):
    return render(request, 'home/home.html')

def admin_add_products(request):
    return render(request, 'admin/produtos/cadastro/cadastroProdutos.html')

def admin_list_products(request):
    new_product = Product()
    new_product.name = request.POST.get('name')
    new_product.description = request.POST.get('description')
    new_product.category = request.POST.get('category')
    new_product.price = request.POST.get('price')
    new_product.productqtt = request.POST.get('productqtt')

    products = {
        'products': Product.objects.all()
    }

    return render(request, 'admin/produtos/listagem/listagemProdutos.html', products)
