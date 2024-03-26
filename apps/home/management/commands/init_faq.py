# -*- coding: utf-8 -*-

import json
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "init F.A.Q"

    def read_and_save(self, filename: str):
        try:
            pass
        except Exception as e:
            self.stdout.write(self.style.ERROR(e))

    def handle(self, *args, **options):
        self.stdout.write(
            self.style.SUCCESS("\n{} Process started...{}\n").format(
                self.help, __name__
            )
        )

        try:
            pass

        except Exception as e:
            raise e

        self.stdout.write(self.style.SUCCESS("Process finished"))
