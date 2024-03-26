# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand
from django.db import transaction
from django.contrib.sites.models import Site
from django.conf import settings

from apps.core.models import Website

en_meta_description = """django boiler plate"""
en_meta_keywords = """django, python, web, application, boiler, plate, template"""
tr_meta_description = """django proje taslak"""
tr_meta_keywords = """django, python, web, uygulama, site, template, taslak"""


class Command(BaseCommand):
    help = "init website"

    def handle(self, *args, **options):
        self.stdout.write(
            self.style.SUCCESS("\n{} Process started...{}\n").format(
                self.help, __name__
            )
        )

        try:
            with transaction.atomic():
                website, created = Website.objects.get_or_create(
                    name="Example",
                    en_meta_description=en_meta_description,
                    en_meta_keywords=en_meta_keywords,
                    tr_meta_description=tr_meta_description,
                    tr_meta_keywords=tr_meta_keywords,
                )

                self.stdout.write(self.style.SUCCESS("... Updating Site default object ..."))
                site = Site.objects.get(pk=1)
                if settings.DEBUG:
                    site.domain = "localhost:8000"
                    site.name = "Localhost djbp"
                else:
                    site.domain = "example.com"
                    site.name = "example"
                site.save()

        except Exception as e:
            raise e

        self.stdout.write(self.style.SUCCESS("Process finished"))
