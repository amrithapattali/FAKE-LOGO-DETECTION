from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render,get_object_or_404
from .models import Product,CartItem


# Create your views here.

    
class HomePageView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['premium_products'] = Product.objects.filter(premium=True)
        context['regular_products'] = Product.objects.filter(premium=False)
        
         # Include all products in the context
        context['all_products'] = Product.objects.all()
        return context
    
class ProductDetailView(DetailView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product'
    
class CartView(View):
    def get(self, request, *args, **kwargs):
        # Retrieve cart items for the current user (assuming you have a user-based cart)
        cart_items = CartItem.objects.filter(user=request.user)
        
        context = {
            'cart_items': cart_items
        }
        return render(request, 'cart.html', context)
    
class cartPageView(TemplateView):
    template_name = 'cart.html'
    
class productPageView(TemplateView):
    template_name = 'product.html'
    
class contactPageView(TemplateView):
    template_name = 'contact.html'
    
class checkoutPageView(TemplateView):
    template_name = 'checkout.html'
    
class RegisterView(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        if request.method == "POST":
            n = request.POST['n']
            e = request.POST['e']
            p = request.POST['p']
            cp = request.POST['cp']
            if p == cp:
                user = User.objects.create_user(username=n, email=e, password=p)
                user.save()
                return redirect('home')
        return render(request, 'signup.html')

class UserLoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        if request.method == "POST":
            n = request.POST['u']
            p = request.POST['p']

            user = authenticate(username=n, password=p)

            if user:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, "invalid credentials")

        return render(request, 'login.html')

class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')
    


