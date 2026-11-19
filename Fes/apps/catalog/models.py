from django.db import models


class Brand(models.Model):
    """Автор книги."""
    name = models.CharField("Название", max_length=50, unique=True)
    country = models.CharField("Страна", max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Автор"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Car(models.Model):
    """Книга."""

    class Status(models.TextChoices):
        AVAILABLE = "available", "В наличии"
        RESERVED = "reserved", "Забронирована"
        SOLD = "sold", "Продана"

    class FuelType(models.TextChoices):
        PETROL = "petrol", "Роман"
        DIESEL = "diesel", "Детектив"
        ELECTRO = "electro", "Криминал"
        HYBRID = "hybrid", "Драмма"

    brand = models.ForeignKey(
        Brand, on_delete=models.PROTECT,
        related_name="book", verbose_name="Автор",
    )
    model = models.CharField("Книга", max_length=100)
    year = models.PositiveIntegerField("Год")
    price = models.DecimalField("Цена, ₽", max_digits=12, decimal_places=2)
    color = models.CharField("Издание", max_length=30, blank=True)
    engine_volume = models.DecimalField(
        "Количество страниц", max_digits=3, decimal_places=1, null=True, blank=True,
    )
    fuel_type = models.CharField(
        "Жанр", max_length=20, choices=FuelType.choices, blank=True,
    )
    mileage = models.PositiveIntegerField("Популярность", default=0)
    status = models.CharField(
        "Статус", max_length=20,
        choices=Status.choices, default=Status.AVAILABLE,
    )
    vin = models.CharField("ISBN", max_length=17, unique=True, blank=True, null=True)
    description = models.TextField("Описание", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.brand.name} {self.model} ({self.year})"

    def get_absolute_url(self):
        return reverse("catalog:car_detail", args=[self.pk])

    @property
    def is_available(self):
        return self.status == self.Status.AVAILABLE
