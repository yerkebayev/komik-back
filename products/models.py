from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.TextField()
    main_image = models.ImageField(upload_to='main_images/')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_gallery/')
