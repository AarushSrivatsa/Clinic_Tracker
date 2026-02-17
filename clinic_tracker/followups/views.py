from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import FollowUp, PublicViewLog
from .forms import FollowUpForm
from django.db.models import Count

@login_required
def dashboard(request):

    clinic = request.user.userprofile.clinic

    followups = FollowUp.objects.filter(clinic=clinic)

    status = request.GET.get("status")
    due_from = request.GET.get("due_from")
    due_to = request.GET.get("due_to")

    if status:
        followups = followups.filter(status=status)

    if due_from:
        followups = followups.filter(due_date__gte=due_from)

    if due_to:
        followups = followups.filter(due_date__lte=due_to)

    followups = followups.annotate(view_count=Count("publicviewlog"))

    return render(request, "followups/dashboard.html", {
        "followups": followups
    })

@login_required
def create_followup(request):

    if request.method == "POST":
        form = FollowUpForm(request.POST)
        if form.is_valid():
            followup = form.save(commit=False)
            followup.clinic = request.user.userprofile.clinic
            followup.created_by = request.user
            followup.save()
            return redirect("dashboard")
    else:
        form = FollowUpForm()

    return render(request, "followups/followup_form.html", {
        "form": form
    })

@login_required
def dashboard(request):

    clinic = request.user.userprofile.clinic

    followups = FollowUp.objects.filter(
        clinic=clinic
    ).annotate(
        view_count=Count("publicviewlog")
    )

    return render(request, "followups/dashboard.html", {
        "followups": followups
    })

from django.shortcuts import get_object_or_404


@login_required
def mark_done(request, id):
    if request.method == "POST":
        clinic = request.user.userprofile.clinic
        followup = get_object_or_404(
            FollowUp,
            id=id,
            clinic=clinic
        )
        followup.status = "done"
        followup.save()

    return redirect("dashboard")

def public_followup(request, token):
    followup = FollowUp.objects.get(public_token=token)
    PublicViewLog.objects.create(
        followup=followup,
        user_agent=request.META.get("HTTP_USER_AGENT", ""),
        ip_address=request.META.get("REMOTE_ADDR")
    )

    return render(request, "followups/public_followup.html", {
        "followup": followup
    })