import os
import sys
import random
import datetime
import django

# Add the project base directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Set the Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "alx_travel_app.settings")

# Set up Django
django.setup()

from listings.models import Booking, User, Listing
from listings.tasks import send_booking_email

# Replace these with actual valid IDs
USER_ID = 1
LISTING_ID = 1

def create_booking():
    try:
        user = User.objects.get(id=USER_ID)
        listing = Listing.objects.get(listing_id=LISTING_ID)

        # Define booking dates
        start = datetime.date(2025, 7, 15)
        end = datetime.date(2025, 7, 20)

        # Calculate total price
        price = 5 * float(listing.price_per_night)

        # Create booking (ensure booking_id is unique)
        booking = Booking.objects.create(
            booking_id=random.randint(1000, 9999),  # Change this to a UUID or unique number in real apps
            user_id=user,
            listing_id=listing,
            start_date=start,
            end_date=end,
            total_price=price,
            status='pending'
        )

        print(f"✅ Booking created successfully for {user.username} at '{listing.title}'")
        print(f"📦 Booking ID: {booking.booking_id}")

        # Trigger the email notification
        send_booking_email.delay(user.email, booking.booking_id)
        print(f"📧 Email task triggered for {user.email}")

    except User.DoesNotExist:
        print(f"❌ User with id {USER_ID} does not exist.")
    except Listing.DoesNotExist:
        print(f"❌ Listing with id {LISTING_ID} does not exist.")
    except Exception as e:
        print(f"❌ An error occurred: {e}")

if __name__ == "__main__":
    create_booking()