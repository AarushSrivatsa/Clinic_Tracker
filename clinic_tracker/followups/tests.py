from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Clinic, UserProfile, FollowUp, PublicViewLog

class FollowUpTests(TestCase):

    def setUp(self):

        self.client = Client()

        self.clinic = Clinic.objects.create(name="Test Clinic")

        self.user = User.objects.create_user(
            username="testuser",
            password="testpass"
        )

        self.profile = UserProfile.objects.create(
            user=self.user,
            clinic=self.clinic
        )

        self.followup = FollowUp.objects.create(
            clinic=self.clinic,
            created_by=self.user,
            patient_name="Test Patient",
            phone="1234567890",
            language="en",
            due_date="2026-02-20"
        )


    def test_clinic_code_generated(self):
        self.assertIsNotNone(self.clinic.clinic_code)


    def test_public_token_generated(self):
        self.assertIsNotNone(self.followup.public_token)


    def test_dashboard_requires_login(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 302)


    def test_cross_clinic_access_blocked(self):

        other_clinic = Clinic.objects.create(name="Other Clinic")

        other_user = User.objects.create_user(
            username="otheruser",
            password="testpass"
        )

        UserProfile.objects.create(
            user=other_user,
            clinic=other_clinic
        )

        self.client.login(username="otheruser", password="testpass")

        response = self.client.get("/")

        self.assertNotContains(response, "Test Patient")


    def test_public_view_log_created(self):

        self.client.get(f"/p/{self.followup.public_token}/")

        self.assertEqual(
            PublicViewLog.objects.count(),
            1
        )
