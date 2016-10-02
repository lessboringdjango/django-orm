from django.core.management.base import BaseCommand
from game.grade import grade


class Command(BaseCommand):

    help = 'Grade the specified level manually'

    def add_arguments(self, parser):
        parser.add_argument('which', type=int)

    def handle(self, *args, **options):
        try:
            print grade(options['which'])
        except Exception as e:
            print {'message': e.message}
