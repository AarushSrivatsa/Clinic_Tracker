from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("create/", views.create_followup, name="create_followup"),
    path("p/<uuid:token>/", views.public_followup, name="public_followup"),
    path("done/<int:id>/", views.mark_done, name="mark_done"),

]