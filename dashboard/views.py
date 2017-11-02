from django.shortcuts import redirect, render

from .models import Job
from .tasks import process_job


def index(request):
    if request.method == "POST":
        job = Job.objects.create(type=request.POST["type"])
        process_job.send(job.pk)
        return redirect("index")
    return render(request, "dashboard/index.html", {
        "jobs": Job.objects.all(),
    })
