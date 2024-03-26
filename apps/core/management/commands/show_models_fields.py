from django.core.management.base import BaseCommand
from django.apps import apps

class Command(BaseCommand):
    help = "Show models, associated fields, and their types, with related models for ForeignKey and ManyToManyField"

    """
    Author
        name (CharField)
        email (EmailField)
        books (ManyToManyField) - Related Model: Book

    Book
        title (CharField)
        author (ForeignKey) - Related Model: Author
    """

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("*" * 100))
        self.stdout.write(self.style.SUCCESS("{}").format(self.help))

        model_list = apps.get_models()
        for model in model_list:
            print(model.__name__)
            field_list = model._meta.get_fields()
            for field in field_list:
                field_type = field.__class__.__name__
                if field_type in ("ForeignKey", "ManyToManyField"):
                    related_model = field.related_model.__name__
                    print(f"\t{field.name} ({field_type}) - Related Model: {related_model}")
                else:
                    print(f"\t{field.name} ({field_type})")

        self.stdout.write(self.style.SUCCESS("*" * 100))
