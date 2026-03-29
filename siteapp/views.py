from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods

from .forms import InterestForm


@require_http_methods(["GET", "POST"])
def home(request):
    if request.method == "POST":
        form = InterestForm(request.POST)
        if form.is_valid():
            # Demo: no persistence; extend with a model when ready.
            request.session["interest_submitted"] = True
            return redirect("home")
    else:
        form = InterestForm()

    submitted = request.session.pop("interest_submitted", False)
    return render(
        request,
        "siteapp/index.html",
        {"form": form, "interest_submitted": submitted},
    )
