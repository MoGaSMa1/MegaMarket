from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Author(models.Model):
    Author = models.CharField(max_length=20, db_index=True)
    def __str__(self):
        return self.Author

class Series(models.Model):
    Series = models.CharField(max_length=20)
    def __str__(self):
        return self.Series

class Gener(models.Model):
    Gener = models.CharField(max_length=20)
    def __str__(self):
        return self.Gener

class Publish(models.Model):
    Publish = models.CharField(max_length=20)
    def __str__(self):
        return self.Publish
    
    
class Book(models.Model):
    name = models.CharField(verbose_name="Name", max_length=50, db_index=True)
    img = models.ImageField(verbose_name="IMG", upload_to='', blank=True)
    price = models.DecimalField(verbose_name="Price", max_digits=10, decimal_places=2)
    author = models.ForeignKey("books.Author", on_delete=models.PROTECT, verbose_name="Author")
    series = models.ForeignKey("books.Series", on_delete=models.PROTECT, verbose_name="Series")
    gener = models.ForeignKey("books.Gener", on_delete=models.PROTECT, verbose_name="Gener")
    year = models.IntegerField(verbose_name="Year", validators=[MinValueValidator(1900), MaxValueValidator(2030)])
    pages = models.IntegerField(verbose_name="Pages", validators=[MinValueValidator(0), MaxValueValidator(5000)])
    
    class binding(models.TextChoices):
        HARD = "hard", _("Hard")
        SOFT = "soft", _("Soft")
        INFO = "info", _("NOINFO")

    binding = models.CharField(
        verbose_name="Binding", 
        max_length=4,
        choices=binding.choices,
        default=binding.INFO,
        blank=True
    )

    class formattt(models.TextChoices):
        SLARGE = "slarge", _("Slarge")
        LARGE = "large", _("Large")
        MEDIUM = "medium", _("Medium")
        SMALL = "small", _("Small")
        MIDGET = "midget", _("Midget")
        INFO = "info", _("NOINFO")

    formatt = models.CharField(
        verbose_name="Format", 
        max_length=6,
        choices=formattt.choices,
        default=formattt.INFO,
    )

    isbn = models.CharField(verbose_name="ISBN", max_length=10, default=None, blank=True)
    weight = models.IntegerField(verbose_name="Weight", validators=[MinValueValidator(0), MaxValueValidator(5000)], default=None, blank=True)
    ager = models.IntegerField(verbose_name="Ager", validators=[MinValueValidator(0), MaxValueValidator(18)], default=None, blank=True)
    publish = models.ForeignKey("books.Publish", on_delete=models.PROTECT, verbose_name="Publish", default=None)
    quantity = models.IntegerField(verbose_name="quantity", validators=[MinValueValidator(0), MaxValueValidator(50000)], default=None)
    available = models.BooleanField(verbose_name="Availability", default=True)
    rating = models.IntegerField(verbose_name="Rating", validators=[MinValueValidator(0), MaxValueValidator(10)], default=None, blank=True)
    created = models.DateTimeField(verbose_name="Added", auto_now_add=True)
    modified = models.DateTimeField(verbose_name="Last change", auto_now=True)

    def __str__(self):
        return self.name