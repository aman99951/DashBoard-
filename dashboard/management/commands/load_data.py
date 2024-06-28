# dashboard/management/commands/load_data.py

import os
import json
from datetime import datetime
from django.core.management.base import BaseCommand
from django.utils import timezone
from dashboard.models import DataPoint  # Replace with your actual model import


class Command(BaseCommand):
    help = 'Loads data from JSON file into the database'

    def handle(self, *args, **options):
        json_file = r'C:\Users\aman9\OneDrive\projects\django\eshopdjango-master\Pictures\Desktop\my_dashboard\my_dashboard\jsondata.json'

        with open(json_file, 'r') as f:
            data = json.load(f)
            for entry in data:
                try:
                    if entry["published"]:
                        published_date = datetime.strptime(
                            entry["published"], "%B, %d %Y %H:%M:%S")
                    else:
                        # Default to current time if published date is not provided
                        published_date = timezone.now()
                except (ValueError, KeyError):
                    # Handle cases where published date format is incorrect or missing
                    published_date = timezone.now()  # Default to current time if there's an issue

                datapoint = DataPoint(
                    end_year=entry["end_year"],
                    intensity=entry["intensity"],
                    sector=entry["sector"],
                    topic=entry["topic"],
                    insight=entry["insight"],
                    url=entry["url"],
                    region=entry["region"],
                    start_year=entry["start_year"],
                    impact=entry["impact"],
                    added=timezone.now(),
                    published=published_date,
                    country=entry["country"],
                    relevance=entry["relevance"],
                    pestle=entry["pestle"],
                    source=entry["source"],
                    title=entry["title"],
                    likelihood=entry["likelihood"]
                )
                datapoint.save()

        self.stdout.write(self.style.SUCCESS('Data loaded successfully.'))
