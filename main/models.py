from django.db import models
from django.utils.html import mark_safe
# Create your models here.

class Banner(models.Model):
    img = models.CharField(max_length=200)
    alt_text = models.CharField(max_length=300)

    class Meta:
        verbose_name_plural = '1. Banners'                                                                  

class Category(models.Model):
    title = models.CharField(max_length = 100)
    image = models.ImageField(upload_to="cat_imgs/")

    class Meta:
        verbose_name_plural = '2. Categories'

    def image_tag(self):
        return mark_safe('<img src="%s"  width="50" height="50" />' % (self.image.url))

    def __str__(self):
        return self.title

class Brand(models.Model):
    title = models.CharField(max_length = 100)
    image = models.ImageField(upload_to="brand_imgs/")
  
    class Meta:
        verbose_name_plural = '3. Brands'

    def __str__(self):
        return self.title

class Color(models.Model):
    title = models.CharField(max_length = 100)
    color_code = models.CharField(max_length=100, default=None)
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = '4. Colors'

    def color_bg(self):
        return mark_safe('<div style="width:30px; height:30px; background-color:%s"><div>' % (self.color_code))

class Size(models.Model):
    title = models.CharField(max_length = 100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = '5. Sizes'

class Product(models.Model):
    title = models.CharField(max_length = 100)
    image = models.ImageField(upload_to = "product_imgs/")
    slug = models.CharField(max_length = 400)
    detail = models.TextField()
    specs = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    status = models.BooleanField(default = True)

    class Meta:
        verbose_name_plural = '6. Products'

    def __str__(self):
        return self.title

#Product Attribute  
class ProductAttribute(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = '7. ProductAttributes'

    def __str__(self):
      return self.product.title


    



