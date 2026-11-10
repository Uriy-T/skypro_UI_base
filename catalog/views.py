from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from .models import Category, Product


def contacts(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        return HttpResponse('Сообщение отправлено. Спасибо.')
    return render(request, 'contacts.html')


def categories(request: HttpRequest) -> HttpResponse:
    categories_data = Category.objects.all()
    context = {'categories': categories_data}
    return render(request, 'categories.html', context)


def category_products(request: HttpRequest, category_id: int) -> HttpResponse:
    products = Product.objects.filter(product_category_id=category_id)
    category = Category.objects.get(pk=category_id)
    context = {'products': products,
               'category': category.category_name}
    return render(request, 'products_category.html', context)


def product_detail(request: HttpRequest, product_id: int) -> HttpResponse:
    product = Product.objects.get(pk=product_id)
    context = {'product': product}
    return render(request, 'product_detail.html', context)


def create_product(request: HttpRequest) -> HttpResponse:
    categories = Category.objects.all()

    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        description = request.POST.get('product_description')
        category_id = request.POST.get('product_categories')
        price = request.POST.get('price')
        image = request.FILES.get('product_image')

        Product.objects.create(
            product_name=product_name,
            description=description,
            product_category_id=category_id,
            price_per_unit=price,
            product_image=image,
        )
        return redirect('catalog:products_category', category_id=category_id)

    context = {'categories': categories}
    return render(request, 'create_product.html', context)
