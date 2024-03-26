# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand
from django.utils.translation import gettext as _
from django.db import transaction
from django.core.management import call_command
from django.conf import settings


class Command(BaseCommand):
    help = "init all & setup project"

    @staticmethod
    def get_variable_name_as_str(var):
        return f"{var=}".split("=")[0]

    def handle(self, *args, **options):
        self.stdout.write(
            self.style.SUCCESS("\nProcess started...{}\n").format(__name__)
        )
        try:
            with transaction.atomic():
                if settings.DEBUG:
                    pass

                # dev or prod call commands
                call_command(command_name="init_website")
                call_command(command_name="init_system_users")
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Process failed {e}"))

        self.stdout.write(self.style.SUCCESS("Process finished"))
