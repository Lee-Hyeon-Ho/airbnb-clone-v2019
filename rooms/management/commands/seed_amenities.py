from django.core.management.base import BaseCommand
from rooms.models import Amenity


class Command(BaseCommand):

    help = "This command create amenities"

    # def add_arguments(self, parser):
    #     parser.add_argument(
    #         "--times", help="How many times do you want me to tell you yhat I love you?")

    def handle(self, *args, **options):
        amenities = (
            'Wifi',
            'Kitchen',
            'Washer',
            'Dryer',
            'Air conditioning',
            'Heating',
            'Dedicated workspace',
            'TV',
            'Hair dryer',
            'Iron',
            'Pool',
            'Hot tub',
            'Free parking on premises',
            'EV charger',
            'Crib',
            'Gym',
            'BBQ grill',
            'Breakfast',
            'Indoor fireplace',
            'Smoking allowed',
            'Beachfront',
            'Waterfront',
            'Smoke alarm',
            'Carbon monoxide alarm',
        )
        for a in amenities:
            Amenity.objects.create(name=a)
        self.stdout.write(self.style.SUCCESS("Amenities created!"))
