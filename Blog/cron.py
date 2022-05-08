from .models import Entry, Feature
from .serializers import FeatureSerializer
from datetime import datetime
from random import randint


def get_random_feature():
    filter_entries = Entry.objects.filter(submitted_date__lte=datetime.today())
    num_entries = len(filter_entries)

    random_entry = filter_entries[randint(0, num_entries - 1)]
    feature = Feature(entry=random_entry, title=random_entry.title, body=random_entry.body)
    feature.save()

