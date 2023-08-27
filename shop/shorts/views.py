from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from .models import Short, Comment, Order, OrderItem
from django.contrib.auth import login
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth import login as auth_login
from django.contrib.auth import views as auth_views
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout
from django.urls import reverse
from django.utils import timezone
from .forms import SignupForm, CommentForm
from .cart import Cart


def custom_function(request):
    currency = request.POST.get('hat__hidden')
    city = request.POST.get('modal-hidden')
    if currency == None:
        currency = request.COOKIES.get('currency')
        if currency == None: 
            currency = 'RUB'
    if city == None:
        city = request.COOKIES.get('city')
        if city == None: 
            city = 'Moskow'
    return [currency, city]

def inject(items):
    items = items[1:-1]
    items = items.split(',')
    return items

    

def index(request):
    form = SignupForm()
    currency, city = custom_function(request)

    short_list = Short.objects.all()
    content = {'short_list': short_list, 'currency': currency, 'city': city, 'form': form}
        
    template = loader.get_template('shorts/index.html') 
    response = HttpResponse(template.render(content, request))
    currency, city = currency, city
    response.set_cookie('currency', currency)
    response.set_cookie('city', city)
    return response

def short_item(request, id):
    form = SignupForm()
    create_comment = CommentForm
    currency, city = custom_function(request)

    short = Short.objects.get(id=id)
    comments = Comment.objects.filter(short=short)
    content = {'short': short, 'currency': currency, 'city': city, 'form': form, 'create_comment': create_comment, 'comments': comments}

    template = loader.get_template('shorts/short_item.html') 
    response = HttpResponse(template.render(content, request))
    currency, city = currency, city
    response.set_cookie('currency', currency)
    response.set_cookie('city', city)
    return response

def about(request):
    form = SignupForm()
    currency, city = custom_function(request)

    content = {'currency': currency, 'city': city, 'form': form}

    template = loader.get_template('shorts/about.html') 
    response = HttpResponse(template.render(content, request))
    currency, city = currency, city
    response.set_cookie('currency', currency)
    response.set_cookie('city', city)
    return response

def contacts(request):
    form = SignupForm()
    currency, city = custom_function(request)

    content = {'currency': currency, 'city': city, 'form': form}

    template = loader.get_template('shorts/contacts.html') 
    response = HttpResponse(template.render(content, request))
    currency, city = currency, city
    response.set_cookie('currency', currency)
    response.set_cookie('city', city)
    return response

def production(request):
    form = SignupForm()
    currency, city = custom_function(request)

    content = {'currency': currency, 'city': city, 'form': form}

    template = loader.get_template('shorts/production.html')
    response = HttpResponse(template.render(content, request))
    currency, city = currency, city
    response.set_cookie('currency', currency)
    response.set_cookie('city', city)
    return response  

def job(request):
    form = SignupForm()
    currency, city = custom_function(request)

    content = {'currency': currency, 'city': city, 'form': form}

    template = loader.get_template('shorts/job.html')
    response = HttpResponse(template.render(content, request))
    currency, city = currency, city
    response.set_cookie('currency', currency)
    response.set_cookie('city', city)
    return response  

def payment(request):
    form = SignupForm()
    currency, city = custom_function(request)

    content = {'currency': currency, 'city': city, 'form': form}

    template = loader.get_template('shorts/payment.html')
    response = HttpResponse(template.render(content, request))
    currency, city = currency, city
    response.set_cookie('currency', currency)
    response.set_cookie('city', city)
    return response 

def refund(request):
    form = SignupForm()
    currency, city = custom_function(request)

    content = {'currency': currency, 'city': city, 'form': form}

    template = loader.get_template('shorts/refund.html')
    response = HttpResponse(template.render(content, request))
    currency, city = currency, city
    response.set_cookie('currency', currency)
    response.set_cookie('city', city)
    return response 

def cart(request):
    form = SignupForm()
    currency, city = custom_function(request)
    cart = Cart(request)
    total_price = cart.get_total_price()
    summary = cart.__len__()

    default_size = request.COOKIES.get('default_size')
    default_color = request.COOKIES.get('default_color')

    content = {'currency': currency, 'city': city, 'form': form, 'cart': cart, 'total_price': total_price, 'default_size': default_size, 
               'default_color': default_color, 'summary': summary}

    template = loader.get_template('shorts/cart.html')
    response = HttpResponse(template.render(content, request))
    currency, city = currency, city
    response.set_cookie('currency', currency)
    response.set_cookie('city', city)
    return response

def cart_new(request, product_id):
    form = SignupForm()
    currency, city = custom_function(request)
    cart = Cart(request)
    default_size = request.POST.get('size')
    default_color = request.POST.get('color')

    product = get_object_or_404(Short, id=product_id)

    cart.add(product=product, update_quantity=False, default_color=default_color, default_size=default_size)

    content = {'currency': currency, 'city': city, 'form': form, 'cart': cart, 'product': product}

    response = redirect(reverse('cart'))
    currency, city = currency, city
    response.set_cookie('currency', currency)
    response.set_cookie('city', city)
    response.set_cookie('default_size', default_size)
    response.set_cookie('default_color', default_color)
    return response

def cart_add(request, product_id):
    form = SignupForm()
    currency, city = custom_function(request)
    cart = Cart(request)

    product = get_object_or_404(Short, id=product_id)

    cart.add(product=product, update_quantity=False)

    content = {'currency': currency, 'city': city, 'form': form, 'cart': cart, 'product': product}

    response = redirect(reverse('cart'))
    currency, city = currency, city
    response.set_cookie('currency', currency)
    response.set_cookie('city', city)
    return response

def cart_decrease(request, product_id):
    form = SignupForm()
    currency, city = custom_function(request)
    cart = Cart(request)
    product = Short.objects.get(id=product_id)
    
    cart.decrease(product=product, update_quantity=False)

    content = {'currency': currency, 'city': city, 'form': form, 'cart': cart, 'product': product}

    response = redirect(reverse('cart'))
    currency, city = currency, city
    response.set_cookie('currency', currency)
    response.set_cookie('city', city)
    return response

def cart_remove(request, product_id):
    form = SignupForm()
    currency, city = custom_function(request)
    cart = Cart(request)
    product = Short.objects.get(id=product_id)
    
    cart.remove(product=product)

    content = {'currency': currency, 'city': city, 'form': form, 'cart': cart, 'product': product}

    response = redirect(reverse('cart'))
    currency, city = currency, city
    response.set_cookie('currency', currency)
    response.set_cookie('city', city)
    return response

def cart_registration(request):
    form = SignupForm()
    currency, city = custom_function(request)
    cart = Cart(request)
    total_price = cart.get_total_price()
    promo = request.POST.get('promo')
    if promo == None:
        promo = ''
    sizes = request.POST.getlist('size')
    colors = request.POST.getlist('color')
    content = {'currency': currency, 'city': city, 'form': form, 'cart': cart, 'promo': promo, 'total_price': total_price, 'sizes': sizes, 'colors': colors}

    template = loader.get_template('shorts/cart_registration.html')
    response = HttpResponse(template.render(content, request))
    currency, city = currency, city
    response.set_cookie('currency', currency)
    response.set_cookie('city', city)
    response.set_cookie('colors', colors)
    response.set_cookie('sizes', sizes)
    return response

def register_order(request):
    form = SignupForm()
    shorts = Short.objects.all()
    currency, city = custom_function(request)
    cart = Cart(request)
    country = request.POST.get('country')
    phone = request.POST.get('phone')
    subject = request.POST.get('subject')
    address = request.POST.get('address')
    phone = request.POST.get('phone')
    name = request.POST.get('name')
    email = request.POST.get('email')
    surname = request.POST.get('surname')
    comment = request.POST.get('comment')
    promo = request.POST.get('promo')
    colors = request.COOKIES.get('colors')
    sizes = request.COOKIES.get('sizes')
    
    colors = list(inject(colors))
    sizes = list(inject(sizes))

    new_order = Order(country=country, subject=subject, address=address, phone=phone,
                     name=name, email=email, surname=surname, comment=comment, promo=promo)
    new_order.save()

    index = 0
    for item in cart:
        OrderItem.objects.create(order=new_order,
            product=item['product'],
            color= colors[index],
            size = sizes[index],
            price=item['price'],
            quantity=item['quantity'])
        index += 1
    cart.clear()
    
    content = {'currency': currency, 'city': city, 'form': form, 'cart': cart, 'shorts': shorts}

    template = loader.get_template('shorts/index.html')
    response = HttpResponse(template.render(content, request))
    currency, city = currency, city
    response.set_cookie('currency', currency)
    response.set_cookie('city', city)
    return response

def create_order(request):
    form = SignupForm()
    currency, city = custom_function(request)
    cart = Cart(request)
    country = request.POST.get('country')
    return HttpResponse(country)
    # subject = request.POST.get('subject')
    # address = request.POST.get('address')
    # phone = request.POST.get('phone')
    # name = request.POST.get('name')
    # email = request.POST.get('email')
    # surname = request.POST.get('surname')
    # comment = request.POST.get('comment')
    # promo = request.POST.get('promo')
    # new_order = Order(country=country, subject=subject, address=address, phone=phone,
    #                   name=name, email=email, surname=surname, comment=comment, promo=promo)
    # new_order.save()
    # for item in cart:
    #     OrderItem.objects.create(order=new_order,
    #         product=item['product'],
    #         price=item['price'],
    #         quantity=item['quantity'])
    # cart.clear()
    
    # content = {'currency': currency, 'city': city, 'form': form, 'cart': cart}

    # template = loader.get_template('shorts/index.html')
    # response = HttpResponse(template.render(content, request))
    # currency, city = currency, city
    # response.set_cookie('currency', currency)
    # response.set_cookie('city', city)
    # return response

def searched(request):
    shorts = Short.objects.all()
    input_text = request.POST.get('search_field')
    hidden_text = request.POST.get('hidden_text')
    if input_text != None:
        searched_shorts = shorts.filter(title__iregex=input_text)
    else:
        searched_shorts = shorts.filter(title__iregex=hidden_text)
        input_text = hidden_text
    form = SignupForm()
    currency, city = custom_function(request)

    content = {'currency': currency, 'city': city, 'form': form, 'input_text': input_text, 'searched_shorts': searched_shorts}

    template = loader.get_template('shorts/searched.html')
    response = HttpResponse(template.render(content, request))
    currency, city = currency, city
    response.set_cookie('currency', currency)
    response.set_cookie('city', city)
    return response

def category(request, arg):
    category_list = []
    all_shorts = Short.objects.all()
    for short in all_shorts:
        categories_raw = short.categories.all()
        categories = [elem.category for elem in categories_raw]
        if arg in categories:
            category_list.append(short)
    
    form = SignupForm()
    currency, city = custom_function(request)

    content = {'currency': currency, 'city': city, 'form': form, 'category_list': category_list, 'arg': arg}

    template = loader.get_template('shorts/category.html')
    response = HttpResponse(template.render(content, request))
    currency, city = currency, city
    response.set_cookie('currency', currency)
    response.set_cookie('city', city)
    return response

def login(request):
    form = SignupForm()
    email = request.POST.get('email')
    password = request.POST.get('password')
    user = authenticate(request, email=email, password=password)
    if user is not None:
        auth_login(request, user)
        return redirect('registered')
    else: 
        currency, city = custom_function(request)
        short_list = Short.objects.all()
        modal = 'login'
        content = {'short_list': short_list, 'modal': modal, 'currency': currency, 'city': city, 'form': form}

        template = loader.get_template('shorts/index.html') 
        response = HttpResponse(template.render(content, request))
        currency, city = currency, city
        response.set_cookie('currency', currency)
        response.set_cookie('city', city)
        return response

def register(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=password)
            auth_login(request, user)
            return redirect('registered')

    if request.user.is_authenticated:
        return render(request, 'shorts/index.html')
    else:
        currency, city = custom_function(request)
        short_list = Short.objects.all()
        modal = 'register'
        content = {'short_list': short_list, 'modal': modal, 'currency': currency, 'city': city, 'form': form}

        template = loader.get_template('shorts/index.html') 
        response = HttpResponse(template.render(content, request))
        currency, city = currency, city
        response.set_cookie('currency', currency)
        response.set_cookie('city', city)
        return response

@login_required
def registered(request):
    short_list = Short.objects.all()
    user = request.user
    form = SignupForm()
    currency, city = custom_function(request)

    content = {'currency': currency, 'city': city, 'form': form, "short_list": short_list, "user": user}

    template = loader.get_template('shorts/index.html')
    response = HttpResponse(template.render(content, request))
    currency, city = currency, city
    response.set_cookie('currency', currency)
    response.set_cookie('city', city)
    return response

def logout_view(request):
    logout(request)  
    return redirect(reverse('index'))

def account(request):
    user = request.user
    form = SignupForm()
    currency, city = custom_function(request)

    content = {'currency': currency, 'city': city, 'form': form, 'user': user}

    template = loader.get_template('shorts/account.html')
    response = HttpResponse(template.render(content, request))
    currency, city = currency, city
    response.set_cookie('currency', currency)
    response.set_cookie('city', city)
    return response  

def change_password(request):
    user = request.user
    form = SignupForm()
    currency, city = custom_function(request)

    password = request.POST.get('new_password')
    password_confirm = request.POST.get('new_password_confirm')
    if password == password_confirm:
        user.set_password(password)
        user.save()
        content = {'currency': currency, 'city': city, 'form': form, 'user': user}

        template = loader.get_template('shorts/account.html')
        response = HttpResponse(template.render(content, request))
        currency, city = currency, city
        response.set_cookie('currency', currency)
        response.set_cookie('city', city)
        return response
    else:
        modal = 'change_password'
        content = {'currency': currency, 'city': city, 'form': form, 'user': user, 'modal': modal}

        template = loader.get_template('shorts/account.html')
        response = HttpResponse(template.render(content, request))
        currency, city = currency, city
        response.set_cookie('currency', currency)
        response.set_cookie('city', city)
        return response
    
def change_username(request):
    user = request.user
    name = request.POST.get('FIO')
    user.username = name
    user.save()
    form = SignupForm()
    currency, city = custom_function(request)

    content = {'currency': currency, 'city': city, 'form': form, 'user': user}

    template = loader.get_template('shorts/account.html')
    response = HttpResponse(template.render(content, request))
    currency, city = currency, city
    response.set_cookie('currency', currency)
    response.set_cookie('city', city)
    return response

def create_comment(request, arg):
    user = request.user
    short = Short.objects.get(id=arg)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.short = short
            comment.user = user
            comment.date = timezone.now()
            comment.save()
    
    create_comment = CommentForm
    form = SignupForm()
    comments = Comment.objects.filter(short=short)
    currency, city = custom_function(request)

    content = {'short': short, 'currency': currency, 'city': city, 'form': form, 'user': user, 'create_comment': create_comment, 'comments': comments}

    template = loader.get_template('shorts/short_item.html')
    response = HttpResponse(template.render(content, request))
    currency, city = currency, city
    response.set_cookie('currency', currency)
    response.set_cookie('city', city)
    return response