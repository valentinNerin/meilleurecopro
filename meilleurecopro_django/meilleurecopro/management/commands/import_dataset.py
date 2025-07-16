import csv
from django.core.management.base import BaseCommand
from meilleurecopro.models import Estate

class Command(BaseCommand):
    help = 'Bulk import estates from a CSV file into the Estate model'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)
        parser.add_argument('--batch-size', type=int, default=500, help='Number of rows per bulk_create batch')

    def handle(self, *args, **options):
        Estate.objects.all().delete()

        file_path = options['csv_file']
        batch_size = options['batch_size']
        estates = []

        with open(file_path, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for i, row in enumerate(reader, 1):
                condominium_expenses: float
                if row['CONDOMINIUM_EXPENSES'] == '':
                    condominium_expenses = 0
                else:
                    condominium_expenses = float(row['CONDOMINIUM_EXPENSES'])

                estate = Estate(
                    city = row['CITY'],
                    dept_code = row['DEPT_CODE'],
                    zip_code = row['ZIP_CODE'],
                    condominium_expenses = condominium_expenses,
                    ad_url = row['AD_URLS']
                )
                estates.append(estate)

                # Bulk insert in batches
                if i % batch_size == 0:
                    Estate.objects.bulk_create(estates)
                    self.stdout.write(f'Inserted {i} records...')
                    estates = []

            # Insert remaining records
            if estates:
                Estate.objects.bulk_create(estates)
                self.stdout.write(f'Inserted remaining {len(estates)} records.')

        self.stdout.write(self.style.SUCCESS('CSV import completed.'))