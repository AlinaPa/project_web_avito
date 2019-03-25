from django.core.management import BaseCommand

from avito_parser.parser_avito import save_products


class Command(BaseCommand):
    def handle(self, *args, **options):
        save_products()




