from django.core.management.base import BaseCommand
from users.models import User

class Command(BaseCommand):
    help = "Elimina todos los registros del modelo users.User"

    def add_arguments(self, parser):
        parser.add_argument(
            "--yes",
            action="store_true",
            help="Confirmar borrado (sin prompt).",
        )

    def handle(self, *args, **options):
        total = User.objects.count()
        if total == 0:
            self.stdout.write(self.style.WARNING("No hay usuarios para borrar."))
            return

        if not options["yes"]:
            self.stdout.write(
                self.style.WARNING(
                    f"Se van a borrar {total} usuarios. Ejecuta con --yes para confirmar."
                )
            )
            return

        deleted, _ = User.objects.all().delete()
        self.stdout.write(self.style.SUCCESS(f"✅ Borrados {deleted} objetos."))
