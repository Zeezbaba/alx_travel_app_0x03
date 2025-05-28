from django.db import models
from django.contrib.auth.models import User

class Listing(models.Model):
    listing_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    available_from = models.DateField(null=True, blank=True)
    available_to = models.DateField(null=True, blank=True)
    host_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='listings')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Booking(models.Model):
    booking_id = models.IntegerField(primary_key=True)
    listing_id = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='bookings')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    start_date = models.DateField()
    end_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=20, choices=[
        ('pending', 'pending'),
        ('confirmed', 'confirmed'),
        ('canceled', 'canceled')
    ], default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.listing_id.title} - {self.user_id.username}"

class Review(models.Model):
    class Rating(models.IntegerChoices):
        ONE = 1, '1 - Poor'
        TWO = 2, '2 - Fair'
        THREE = 3, '3 - Good'
        FOUR = 4, '4 - Very Good'
        FIVE = 5, '5 - Excellent'
    review_id = models.IntegerField(primary_key=True)
    listing_id = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='reviews')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField(choices=Rating.choices, default=Rating.THREE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user_id.username} for {self.listing_id.title}"
