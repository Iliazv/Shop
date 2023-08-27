from django.contrib.auth.forms import AuthenticationForm
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path
from django.conf import settings
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('short_item/<int:id>/', views.short_item, name='short_item'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('production/', views.production, name='production'),
    path('job/', views.job, name='job'),
    path('payment/', views.payment, name='payment'),
    path('refund/', views.refund, name='refund'),
    path('category/<str:arg>/', views.category, name='category'),
    path('searched/', views.searched, name='searched'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('registered/', views.registered, name='registered'),
    path('cart/', views.cart, name='cart'),
    path('cart_new/<int:product_id>', views.cart_new, name='cart_new'),
    path('cart_add/<int:product_id>', views.cart_add, name='cart_add'),
    path('cart_decrease/<int:product_id>', views.cart_decrease, name='cart_decrease'),
    path('cart_remove/<int:product_id>', views.cart_remove, name='cart_remove'),
    path('account/', views.account, name='account'),
    path('logout/', views.logout_view, name='logout_view'),
    path('change_password/', views.change_password, name='change_password'),
    path('change_username/', views.change_username, name='change_username'),
    path('create_comment/<int:arg>/', views.create_comment, name='create_comment'),
    path('cart_registration/', views.cart_registration, name='cart_registration'),
    path('register_order/', views.register_order, name='register_order'),
    path('create_order/', views.create_order, name='create_order'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)