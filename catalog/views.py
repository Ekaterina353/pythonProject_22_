from django.views.generic import ListView, DetailView
from django.views import View
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from catalog.models import Product


class HomeListView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products'


# def home(request):
#    products = Product.objects.all()
#    context = {'products': products}
#    return render(request, 'product_list.html', context=context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
    return render(request, 'contacts.html')

class CatalogContactsView(View):
    def get(self, request):
        return render(request, 'catalog/contacts.html')

    def post(self, request):
        #Получение данных из формы
        name = request.POST.get('name')
        message = request.POST.get('message')
        # Обработка данных (например, сохранение в БД, отправка email и т. д.)
        # Здесь мы просто возвращаем простой ответ
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")



class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'


#def product_detail(request, pk):
#    product = get_object_or_404(Product, id=pk)
#    context = {'product': product}
#    return render(request, 'product_detail.html', context=context)
