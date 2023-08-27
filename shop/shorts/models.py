from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import now
from .managers import CustomUserManager


class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def get_name(self):
        return self.usernames


class Short(models.Model):
    title = models.CharField(max_length=150)
    price = models.IntegerField(default=0)
    article = models.IntegerField(default=0)
    description = models.TextField(max_length=3000)
    designer = models.CharField(max_length=100)
    main_image = models.ImageField(upload_to = 'short_images/', blank = True)
    replace_image = models.ImageField(upload_to = 'short_images/', blank = True)
    composition = models.TextField(max_length=300, default='')
    color = models.CharField(max_length=60, default='Black')
    length = models.CharField(max_length=100, default='До линии бедер')
    size = models.CharField(max_length=100, default='XXS (40-42)')
    country = models.CharField(max_length=80, default='Россия')
    style = models.CharField(max_length=80, default='Повседневный')
    sex = models.CharField(max_length=40, default='Мужской')
    season = models.CharField(max_length=60, default='Мульти')
    model = models.IntegerField(default=180)
    time = models.IntegerField(default=7)

    def __str__(self):
        return self.title
    

class Photo(models.Model):
    short = models.ForeignKey(Short, on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField(upload_to = 'short_images/', blank = True)

    def __str__(self):
        return self.short.title


class Category(models.Model):
    short = models.ForeignKey(Short, on_delete=models.CASCADE, related_name='categories')
    category = models.CharField(max_length=60)

    def __str__(self):
        return self.short.title + ' - ' + self.category


class Size(models.Model):
    short = models.ForeignKey(Short, on_delete=models.CASCADE, related_name='sizes')
    size = models.CharField(max_length=25)

    def __str__(self):
        return self.short.title + ' - ' + self.size
    

class Color(models.Model):
    short = models.ForeignKey(Short, on_delete=models.CASCADE, related_name='colors')
    color = models.CharField(max_length=60)

    def __str__(self):
        return self.short.title + ' - ' + self.color
    

class Comment(models.Model):
    SCORE_CHOICES = (
        (5, '5'),
        (4, '4'),
        (3, '3'),
        (2, '2'),
        (1, '1'),
    )

    DELIVERY_CHOICES = (
        ('early', 'Во время'),
        ('late', 'Задержали'),
    )

    MATERIAL_CHOICES = (
        ('great', 'Отличный'),
        ('good', 'Хороший'),
        ('bad', 'Плохой'),
    )

    PRINT_CHOICES = (
        ('great', 'Отличный'),
        ('good', 'Хороший'),
        ('bad', 'Плохой'),
    )

    
    short = models.ForeignKey(Short, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')
    name = models.CharField(max_length=50)
    score = models.IntegerField(default=0, choices=SCORE_CHOICES)
    delivery = models.CharField(max_length=60, default='early', choices=DELIVERY_CHOICES)
    material = models.CharField(max_length=60, default='great',choices=MATERIAL_CHOICES)
    print = models.CharField(max_length=60, default='great', choices=PRINT_CHOICES)
    date = models.DateTimeField(default=now)
    text = models.TextField()

    def __str__(self):
        return self.short.title
    

class Order(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    phone = models.IntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=250)
    country = models.CharField(max_length=50)
    subject = models.CharField(max_length=100)
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    promo = models.CharField(max_length=15, default='')

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Order {}'.format(self.id)
    
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Short, on_delete=models.CASCADE, related_name='order_items')
    color = models.CharField(max_length=60, default='Black')
    size = models.CharField(max_length=25, default='XXS (40-42)')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity