from django.urls import path
from .views import HomePageView, RegisterView, UserLoginView, UserLogoutView,cartPageView,productPageView,checkoutPageView,ProductDetailView,CartView,contactPageView
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
    path('',HomePageView.as_view(), name='home'),
    path('cart/',cartPageView.as_view(), name='cart'),
    # path('add-to-cart/<int:pk>/', CartView.as_view(), name='cart_item'),
    
    path('contact/',contactPageView.as_view(), name='contact'),
    
    path('product/',productPageView.as_view(), name='product'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('checkout/',checkoutPageView.as_view(), name='checkout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='user_login'),
    path('logout/', UserLogoutView.as_view(), name='user_logout'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)