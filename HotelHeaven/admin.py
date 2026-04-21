from django.contrib import admin
from HotelHeaven.models import *

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'password', 'admin_photo']

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['country_name']

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ['country', 'state_name']

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['state', 'city_name']

@admin.register(HotelCategory)
class HotelCategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name']

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ['hotel_name', 'hotel_description', 'hotel_category', 'location', 'city', 'phone', 'email', 'zip_code', 'added_at', 'rating', 'number_reviews']

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['hotel', 'name', 'description', 'price_per_night', 'num_beds', 'capacity', 'is_available', 'created_at']

@admin.register(RoomImages)
class RoomImagesAdmin(admin.ModelAdmin):
    list_display = ['room', 'admin_photo']

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['hotel', 'user', 'rating', 'comment', 'added_at']

@admin.register(FavoriteHotel)
class FavoriteHotelAdmin(admin.ModelAdmin):
    list_display = ['user', 'hotel']

@admin.register(Bookings)
class BookingsAdmin(admin.ModelAdmin):
    list_display = ['user','room','check_in_date', 'check_out_date', 'num_adults', 'num_children', 'total_price', 'is_confirmed', 'created_at']

@admin.register(Payments)
class PaymentsAdmin(admin.ModelAdmin):
    list_display = ['booking', 'amount', 'payment_date', 'payment_method', 'status']
