from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Product
from django.views import View
from .forms import ProductForm



class ProductListView(View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, 'products/products_list.html', {"products" : products})




class ProductDetailView(View):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        return render(request, 'products/detail.html', {"product" : product})
    


class ProductCreateView(View):
    def get(self, request):
        form = ProductForm()
        return render(request, "products/create.html", {"form" : form})
    
    def post(self, request):
        form = ProductForm(data=request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.owner = request.user
            product.save()

            return redirect("products:list")
        return render(request, "products/create.html", {"form" : form})




class ProductUpdateView(LoginRequiredMixin, View):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk, owner=request.user)
        form = ProductForm(instance=product)
        return render(request, 'products/update.html', {"form" : form})
    
    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk, owner=request.user)
        form = ProductForm(data=request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products:detail', pk=product.pk)
        return render(request, 'products/update.html', {"form" : form})
    

class ProductDeleteView(View):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk, owner=request.user)
        return render(request, 'products/product_confirm_delete.html', {'product': product})

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk, owner=request.user)
        product.delete()
        return redirect('products:list')








































