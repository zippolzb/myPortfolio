from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("jobs/", views.jobs, name="jobs"),
#    path("jobs/", views.JobView.as_view(), name = "jobs")
]