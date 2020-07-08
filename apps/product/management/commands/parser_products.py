from django.core.management import BaseCommand

from avito_parser.parser_avito import get_avito_ads


class Command(BaseCommand):
    def handle(self, *args, **options):
        get_avito_ads()
