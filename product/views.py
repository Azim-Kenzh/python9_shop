from django.http import Http404
from django.shortcuts import render, get_list_or_404, get_object_or_404

# Create your views here.
from product.models import Category, Product


def homepage(request):
    categories = Category.objects.all()
    return render(request, 'product/index.html', {'categories': categories})



#prodicts/category
# def products_list(request, category_slug):
#     # products = Product.objects.all()
#
#     # if not Category.objects.filter(slug=category_slug).exists():
#     #     raise  Http404
#     # products = Product.objects.filter(category_id=category_slug)
#
#     # category = get_object_or_404(Category,  slug=category_slug)
#     # products = Product.objects.filter(category=category)
#
#     products = get_list_or_404(Product, category_id=category_slug)
#     # select * from product where category_id = category_slug
#     return render(request, 'product/products_list.html', {'products': products})

# #products/?category=slug
# def products_list2(request):
#     category_clug = request.GET.get('category')
#     products = Product.objects.all()
#     if category_clug is not None:
#         products = products.filter(category_id=category_slug)
#      return render(request, '', {'products': products})

def products_list(request, category_slug):
    if not Category.objects.filter(slug=category_slug).exists():
        raise Http404('Нет такой категории')
    products = Product.objects.filter(category_id=category_slug)
    return render(request, 'product/products_list.html', {'products': products})


def product_details(request, product_id):
    product =  get_object_or_404(Product, id=product_id)
    return render(request, 'product/product_details.html', {'product': product})
    # product = Product.objects.get(id=product_id)


#TODO: переписать вьюшку products_list / + + +
#TODO: подключить картинки для товаров / + + +
#TODO: добавить детали продукта /
#TODO: переписать вьюшку на CBV(Class-Based Views)
#TODO: сделать переход из категории в листинг продуктов
