from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Job
from django.views import generic

# Create your views here.

def index(request):
    template = loader.get_template("curriculum/curriculum.html")
    context = {}
    return HttpResponse(template.render(context,request))

#class JobView(generic.ListView):
#    template = loader.get_template("curriculum/job_list.html")
#    context_object_name = "job_list"
#
#    def get_queryset(self):
#        return Job.objects.all()
    
def jobs(request):
    template = loader.get_template("curriculum/job_list.html")
    job_list = Job.objects.order_by("-start_date")
    context = {
        "job_list":job_list
    }

    return HttpResponse(template.render(context,request))
    