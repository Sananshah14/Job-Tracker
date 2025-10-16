# jobs/views.py

import calendar
import json
from django.shortcuts import render, redirect, get_object_or_404
from .models import Job
from .forms import JobForm
from django.shortcuts import render
from django.db.models import Count
from django.contrib import messages
from django.views.generic.edit import CreateView
from django.db.models.functions import ExtractMonth
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

def home_redirect(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful! Please log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
        return render(request, 'jobs/signup.html', {'form': form})
    
def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/job_list.html', {'jobs': jobs})


def add_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('job_list')
    else:
        form = JobForm()
    return render(request, 'jobs/add_job.html', {'form': form})

def update_job(request, job_id):
    job = get_object_or_404(Job, pk=job_id)

    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('job_list')
    else:
        form = JobForm(instance=job)

    return render(request, 'jobs/update_job.html', {'form': form, 'job': job})

def delete_job(request, job_id):
    job = get_object_or_404(Job, pk=job_id)

    if request.method == 'POST':
        job.delete()
        return redirect('job_list')

    return render(request, 'jobs/delete_job.html', {'job': job})

@login_required
def dashboard(request):
    return render(request, 'jobs/dashboard.html')

# jobs/views.py

def job_statistics(request):
    # Retrieve job status data for the pie chart
    job_status_data = Job.objects.values_list('status').annotate(count=Count('id'))

    # Extract data for pie chart
    jobStatusLabels = [jobStatus[0] for jobStatus in job_status_data]
    jobStatusValues = [jobStatus[1] for jobStatus in job_status_data]

    # Retrieve other data
    total_jobs = Job.objects.count()
    pending_jobs = Job.objects.filter(status='Pending').count()
    rejected_jobs = Job.objects.filter(status='Rejected').count()
    interview_jobs = Job.objects.filter(status='Call for Interview').count()

    # Retrieve month names and total jobs per month
    month_names = Job.objects.values_list('application_date__month', flat=True).distinct()
    months = [calendar.month_name[month] for month in month_names]

    total_jobs_per_month = Job.objects.annotate(month=ExtractMonth('application_date')).values('month').annotate(total_jobs=Count('id'))
    total_jobs_per_month = [month['total_jobs'] for month in total_jobs_per_month]

    # Retrieve progress per month
    progress_per_month = Job.objects.filter(status='Call for Interview').annotate(month=ExtractMonth('application_date')).values('month').annotate(progress=Count('id'))
    progress = [month['progress'] for month in progress_per_month]

    return render(
        request,
        'jobs/job_statistics.html',
        {
            'jobStatusLabels': json.dumps(jobStatusLabels),
            'jobStatusValues': json.dumps(jobStatusValues),
            'total_jobs': total_jobs,
            'pending_jobs': pending_jobs,
            'rejected_jobs': rejected_jobs,
            'interview_jobs': interview_jobs,
            'months': json.dumps(months),
            'total_jobs_per_month': json.dumps(total_jobs_per_month),
            'progress_per_month': json.dumps(progress),
        },
    )

class LoginInterfaceView(LoginView):
    template_name = 'jobs/login.html'
    
class LogoutInterfaceView(TemplateView):
    template_name = 'jobs/logout.html'
    
class HomeView(TemplateView):
    template_name = 'jobs/home.html'

class SignupView(CreateView):  
    form_class = UserCreationForm
    template_name = 'jobs/signup.html'
    success_url= '/jobs/login',
    
    # def get(self, request, *args, **kwargs):
    #     if self.request.user.is_authenticated():
    #         return redirect('jobs.dashboard')
    #     return super().get(request, *args, **kwargs)