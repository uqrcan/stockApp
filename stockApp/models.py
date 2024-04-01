from django.db import models
from django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=40)

    def _str_(self):
        return self.name

    def total_products(self):
        return self.product_set.count()

class Brand(models.Model):
    name = models.CharField(max_length=40)
    image = models.ImageField(upload_to='brands/')

    def _str_(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=40)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    stock = models.IntegerField(editable=False) # read_only olarak işaretlenmiştir.
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def _str_(self):
        return self.name

class Firm(models.Model):
    name = models.CharField(max_length=40)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    image = models.ImageField(upload_to='firms/')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def _str_(self):
        return self.name

class Purchase(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    firm = models.ForeignKey(Firm, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    price_total = models.DecimalField(max_digits=10, decimal_places=2, editable=False) # Hesaplanacak alan
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.price_total = self.quantity * self.price
        super(Purchase, self).save(*args, **kwargs)

class Sale(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    price_total = models.DecimalField(max_digits=10, decimal_places=2, editable=False) # Hesaplanacak alan
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.price_total = self.quantity * self.price
        super(Sale, self).save(*args, **kwargs)