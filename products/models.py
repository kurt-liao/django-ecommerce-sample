from django.db import models

# Create your models here.
# class Category(models.Model):
#     title = models.CharField(max_length=255)
#     slug = models.SlugField(unique=True)
#     image = models.ImageField(upload_to='categories', blank=True)
#     description = models.CharField(max_length=255, blank=True)
#     created_time = models.DateTimeField(auto_now_add=True)
#     modified = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.title

#     class Meta:
#         verbose_name_plural = 'Categories'

# class Product(models.Model):
#     title = models.CharField(max_length=255)
#     slug = models.SlugField(unique=True)
#     image = models.ImageField(upload_to='products', blank=True)
#     description = models.CharField(max_length=255, blank=True)
#     price = models.DecimalField(max_digits=15, decimal_places=0, default=0)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     created_time = models.DateTimeField(auto_now_add=True)
#     modified = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.title


class Category(models.Model):
    title = models.CharField(max_length=300)
    primaryCategory = models.BooleanField(default=False)

    def __str__(self):
        return self.title


# Product Model
class Product(models.Model):
    mainimage = models.ImageField(upload_to='products/', blank=True)
    name = models.CharField(max_length=300, default='')
    slug = models.SlugField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    preview_text = models.TextField(max_length=200,
                                    verbose_name='Preview Text',
                                    blank=True)
    detail_text = models.TextField(max_length=1000,
                                   verbose_name='Detail Text',
                                   blank=True)
    price = models.DecimalField(max_digits=15, decimal_places=0)

    def __str__(self):
        return self.name
