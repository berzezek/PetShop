from django.db import models
from io import BytesIO
from PIL import Image
from django.core.files import File
import datetime


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255, blank=True)
    is_available = models.BooleanField(default=True)
    def __str__(self):
        return self.name


class Product(models.Model):

    UNIT = (
        ('kg', 'Kilogram'),
        ('g', 'Gram'),
        ('l', 'Liter'),
        ('ml', 'Milliliter'),
        ('pcs', 'Pieces'),
        ('box', 'Box'),
        ('pack', 'Pack'),
        ('bottle', 'Bottle'),
    )

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255, null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=1.00)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    unit = models.CharField(max_length=50, choices=UNIT, default='pcs')
    quantity = models.FloatField(default=1, blank=True)
    barcode = models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='images/', blank=True, null=True)
    self_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    is_expired = models.BooleanField(default=False)
    expiration_date = models.DateField(blank=True, null=True)
    is_available = models.BooleanField(default=True, blank=True)
    is_visible = models.BooleanField(default=True, blank=True)

    
    def __str__(self):
        return self.name

    def get_image(self):
        if self.image:
            return f'{self.image.url}' 
        return ''

    def get_thumbnail(self):
        if self.thumbnail:
            return f'{self.thumbnail.url}' 
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()
                return f'{self.thumbnail.url}' 
            else:
                return ''

    def make_thumbnail(self, image, size=(200, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)
        
        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)
        
        thumb_file = File(thumb_io, name=image.name)
        
        return thumb_file

    def get_expiration_date(self):
        if self.expiration_date and self.is_expired:
            return self.expiration_date
        else:
            return datetime.date.today() + datetime.timedelta(days=365) 


class Cart(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING)
    date = models.DateTimeField(auto_now_add=True)
    is_refunded = models.BooleanField(default=False)
    date_of_refund = models.DateTimeField(null=True, blank=True)
    is_sold = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.id} - {self.date}'


class Order(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name

    def order_price(self):
        return self.product.price * self.quantity

    def quantity_left(self):
        quantity_left = self.product.quantity - self.quantity
        self.product.quantity = quantity_left
        return quantity_left



