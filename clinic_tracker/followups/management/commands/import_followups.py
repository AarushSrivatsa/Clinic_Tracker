import csv
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from followups.models import FollowUp

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("--csv", type=str, required=True)
        parser.add_argument("--username", type=str, required=True)

    def handle(self, *args, **options):

        file_path = options["csv"]
        username = options["username"]

        user = User.objects.get(username=username)

        clinic = user.userprofile.clinic

        created = 0
        skipped = 0

        with open(file_path, newline="") as csvfile:

            reader = csv.DictReader(csvfile)

            for row in reader:

                try:

                    FollowUp.objects.create(
                        clinic=clinic,
                        created_by=user,
                        patient_name=row["patient_name"],
                        phone=row["phone"],
                        language=row["language"],
                        due_date=row["due_date"],
                        notes=row.get("notes", "")
                    )

                    created += 1

                except Exception:
                    skipped += 1

        self.stdout.write(f"Created: {created}, Skipped: {skipped}")
