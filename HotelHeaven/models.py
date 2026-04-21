from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=30)
    profile_pic = models.ImageField(upload_to='photos/', blank=True, null=True)

    def __str__(self):
        return f"{self.first_name}{self.last_name}"

    def admin_photo(self):
        return mark_safe('<img src="{}"width = "100" / > '.format(self.profile_pic.url))


class Country(models.Model):
    country_name = models.CharField(max_length=30)

    def __str__(self):
        return self.country_name

class State(models.Model):
    country = models.ForeignKey(Country,on_delete=models.CASCADE )
    state_name = models.CharField(max_length=50)

    def __str__(self):
        return self.state_name

class City(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE )
    city_name = models.CharField(max_length=50)

    def __str__(self):
        return self.city_name

class HotelCategory(models.Model):
    Category_Name = [
        ('luxury', 'Luxury'),
        ('boutique', 'Boutique'),
        ('budget-friendly', 'Budget-Friendly'),
        ('resort', 'Resort'),
        ('business', 'Business'),
        ('extended-stay', 'Extended-Stay'),
        ('airport', 'Airport'),
    ]
    category_name = models.CharField(max_length=50, choices=Category_Name)

    def __str__(self):
        return self.category_name

class Hotel(models.Model):
    hotel_name = models.CharField(max_length=50)
    hotel_description = models.TextField()
    hotel_category = models.ForeignKey(HotelCategory, on_delete=models.CASCADE)
    location = models.CharField(max_length=200)
    city = models.ForeignKey(City,on_delete=models.CASCADE)
    phone = models.BigIntegerField()
    email = models.EmailField()
    zip_code = models.CharField(max_length=10)
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.PositiveSmallIntegerField()
    number_reviews = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.hotel_name

class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True,null=True)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    num_beds = models.PositiveIntegerField()
    capacity = models.PositiveIntegerField()
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class RoomImages(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos/',blank=True, null=True)

    def admin_photo(self):
        return mark_safe('<img src="{}"width = "100" / > '.format(self.image.url))

class Review(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField(blank=True, null=True)
    added_at = models.DateTimeField(auto_now_add=True)

class FavoriteHotel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)

class Bookings(models.Model):
    user = models.CharField(max_length=50)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in_date = models.DateTimeField()
    check_out_date = models.DateTimeField()
    num_adults = models.PositiveIntegerField()
    num_children = models.PositiveIntegerField(default=0)
    total_price = models.DecimalField(max_digits=10,decimal_places=2)
    is_confirmed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)



class Payments(models.Model):
    Payment_method_choices = [
        ('credit_card', 'Credit Card'), ('debit_card', 'Debit Card'), ('paypal', 'PayPal'), ('other', 'Other')
    ]
    Status_choices = [
        ('pending', 'Pending'), ('completed', 'Completed'), ('failed', 'Failed')
    ]

    booking = models.ForeignKey(Bookings, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=50, choices=Payment_method_choices)
    status = models.CharField(max_length=50, choices=Status_choices, default='pending')