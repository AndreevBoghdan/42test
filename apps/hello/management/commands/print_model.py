from django.core.management.base import BaseCommand
from django.db.models import get_apps, get_models


class Command(BaseCommand):

    def handle(self, **options):
        for app in get_apps():
            for model in get_models(app):
                self.stderr.write('error: %s: objects: %s\n'
                                  % (model.__name__, model.objects.count()))
