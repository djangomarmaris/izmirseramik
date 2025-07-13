from django.db import models

# Create your models here.
from django.db import models

class Slider(models.Model):
    title = models.CharField(max_length=200, verbose_name="Büyük Başlık")
    subtitle = models.CharField(max_length=200, verbose_name="Alt Başlık")
    image = models.ImageField(upload_to='slider/', verbose_name="Slider Görseli")
    button_text = models.CharField(max_length=50, blank=True, null=True, verbose_name="Buton Yazısı")
    button_link = models.URLField(blank=True, null=True, verbose_name="Buton Linki")
    order = models.PositiveIntegerField(default=0, verbose_name="Sıralama")

    class Meta:
        ordering = ['order']
        verbose_name = "Slider"
        verbose_name_plural = "Sliderlar"

    def __str__(self):
        return self.title



from django.db import models

class Texture(models.Model):
    name = models.CharField(max_length=100, unique=True ,verbose_name='Doku')
    image = models.ImageField(upload_to='textures/', blank=True, null=True)

    def __str__(self):
        return self.name

class Color(models.Model):
    name = models.CharField(max_length=100, unique=True , verbose_name='Renk')
    hex_code = models.CharField(max_length=7, blank=True, null=True)
    image = models.ImageField(upload_to='colors/', blank=True, null=True)

    def __str__(self):
        return self.name

class Size(models.Model):
    width = models.PositiveIntegerField(verbose_name='Boy')
    height = models.PositiveIntegerField(verbose_name='En')


    def __str__(self):
        return f"{self.width}x{self.height} cm"

class UsageArea(models.Model):
    name = models.CharField(max_length=100, unique=True , verbose_name='Kullanım ALanı')
    image = models.ImageField(upload_to='usage_areas/', blank=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Product Name")
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    image = models.ImageField(upload_to="products/", verbose_name="Main Image")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price", blank=True, null=True)

    texture = models.ForeignKey(Texture, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Texture")
    color = models.ForeignKey(Color, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Color")
    size = models.ForeignKey(Size, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Size")
    usage_areas = models.ManyToManyField(UsageArea, blank=True, verbose_name="Usage Areas")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name
