from django.shortcuts import render, redirect
from admin_datta.forms import RegistrationForm, LoginForm, UserPasswordChangeForm, UserPasswordResetForm, UserSetPasswordForm
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetConfirmView, PasswordResetView
from django.views.generic import CreateView
from django.contrib.auth import logout
from .forms import ActiveJobPostingsForm, ApplicantsForm, InterviewerForm, WeeklyInterviewsForm, PlacementsForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import timedelta
from .models import *
from django.db.models import Count
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import ActiveJobPostings, Applicants, Interviewer, WeeklyInterviews, Placements
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.contrib import messages

def index(request):
    today = timezone.now().date()
    start_of_week = today - timedelta(days=today.weekday())  
    
    all_interviews =  WeeklyInterviews.objects.all()
    all_applicants = Applicants.objects.all()
    all_placements = Placements.objects.all()
    all_job_postings = ActiveJobPostings.objects.all()

    total_active_job_postings = all_job_postings.count()
    total_applicants = all_applicants.count()
    total_interviews = all_interviews.count()
    total_placements = all_placements.count()
    

    job_postings_list = list(all_job_postings.values())
    interviews_list = list(all_interviews.values())
    placements_list = list(all_placements.values())
    applicants_list = list(all_applicants.values())

    interviews_today = all_interviews.filter(interview_date=today)
    interviews_this_week = all_interviews.filter(interview_date__range=[start_of_week, today])
    accepted_interviews_this_week = all_interviews.filter(interview_outcome='Accepted').count()
    rejected_outcomes_today = interviews_today.filter(interview_outcome='Rejected').count()
    rejected_outcomes_this_week = all_interviews.filter(interview_outcome='Rejected').count()

    pending_applicants = all_applicants.filter(status='Pending').count()

    placements_today = all_placements.filter(placement_date=today).count()
    placements_this_week = all_placements.filter(placement_date__range=[start_of_week, today]).count()
    placed_candidates_today = all_placements.filter(placement_status='Placed', placement_date=today).count()
    placed_candidates_this_week = all_placements.filter(placement_status='Placed', placement_date__range=[start_of_week, today]).count()

  

    context = {
        'segment': 'index',
        'total_active_job_postings': total_active_job_postings,
        'total_applicants': total_applicants,
        'total_interviews': total_interviews,
        'total_placements': total_placements,
        'interviews_today': interviews_today,
        'interviews_this_week': interviews_this_week,
        'accepted_interviews_this_week': accepted_interviews_this_week,
        'rejected_outcomes_today': rejected_outcomes_today,
        'rejected_outcomes_this_week': rejected_outcomes_this_week,
        'placements_today': placements_today,
        'placements_this_week': placements_this_week,
        'placed_candidates_today': placed_candidates_today,
        'placed_candidates_this_week': placed_candidates_this_week,
        'all_interviews': all_interviews,
        'all_applicants': all_applicants,
        'all_placements': all_placements,
        'all_job_postings': all_job_postings,
        'job_postings_list': job_postings_list,
        'interviews_list': interviews_list,
        'placements_list': placements_list,
        'applicants_list': applicants_list,
        'pending_applicants': pending_applicants,
    }

    return render(request, "pages/index.html", context)

def delete_interview(request, interview_id):
    interview = get_object_or_404(WeeklyInterviews, pk=interview_id)
    
    if request.method == 'POST':
        interview.delete()
        return redirect('index')
    
def delete_applicant(request, applicant_id):
    applicant = get_object_or_404(Applicants, pk=applicant_id)
    
    if request.method == 'POST':
        applicant.delete()
        return redirect('index')
    
def delete_job_posting(request, job_id):
    job = get_object_or_404(ActiveJobPostings, pk=job_id)
    
    if request.method == 'POST':
        job.delete()
  
        return redirect('index')
    
def delete_placement(request, placement_id):
    placement = get_object_or_404(Placements, pk=placement_id)
    
    if request.method == 'POST':
        placement.delete()
        # Optionally add a success message or perform other actions
        
        # Redirect to the index page or any other appropriate page after deletion
        return redirect('index')

def data_entry(request):
    if request.method == 'POST':
        table_select = request.POST.get('table_select')

        if table_select == 'ActiveJobPostings':
            form = ActiveJobPostingsForm(request.POST)
        elif table_select == 'Applicants':
            form = ApplicantsForm(request.POST)
        elif table_select == 'Interviewer':
            form = InterviewerForm(request.POST)
        elif table_select == 'WeeklyInterviews':
            form = WeeklyInterviewsForm(request.POST)
        elif table_select == 'Placements':
            form = PlacementsForm(request.POST)
        else:
            form = None

        if form.is_valid():
            form.save()
            # Redirect to a success page or perform any other action upon successful form submission
            return HttpResponseRedirect('/success/')  # Redirect to a success page

    else:
        form = None  # Initial form render won't have any form submitted yet

    return render(request, "pages/data_entry.html", {'form': form})

def submit_data(request):
    if request.method == 'POST':
        table_select = request.POST.get('table_select')

        if table_select == 'ActiveJobPostings':
            form = ActiveJobPostingsForm(request.POST)
            model = ActiveJobPostings
        elif table_select == 'Applicants':
            form = ApplicantsForm(request.POST)
            model = Applicants
        elif table_select == 'Interviewer':
            form = InterviewerForm(request.POST)
            model = Interviewer
        elif table_select == 'WeeklyInterviews':
            form = WeeklyInterviewsForm(request.POST)
            model = WeeklyInterviews
        elif table_select == 'Placements':
            form = PlacementsForm(request.POST)
            model = Placements
        else:
            form = None
            model = None

        if form and model:
            if form.is_valid():
                form.save()
                
                return redirect('data_entry')  # Redirect to a success page named 'success'

    # If the request method is not POST or form/model is not valid, render the data entry form again
    return redirect('data_entry')




def delete_active_job_posting(request, posting_id):
    try:
        posting = ActiveJobPostings.objects.get(id=posting_id)
        posting.delete()
        messages.success(request, 'Job posting deleted successfully.')
    except ActiveJobPostings.DoesNotExist:
        messages.error(request, 'Job posting not found.')
    return redirect('posting_list')

def delete_applicant(request, applicant_id):
    try:
        applicant = Applicants.objects.get(id=applicant_id)
        applicant.delete()
        messages.success(request, 'Applicant deleted successfully.')
    except Applicants.DoesNotExist:
        messages.error(request, 'Applicant not found.')
    return redirect('applicant_list')

def delete_interviewer(request, interviewer_id):
    try:
        interviewer = Interviewer.objects.get(id=interviewer_id)
        interviewer.delete()
        messages.success(request, 'Interviewer deleted successfully.')
    except Interviewer.DoesNotExist:
        messages.error(request, 'Interviewer not found.')
    return redirect('interviewer_list')

def delete_weekly_interview(request, interview_id):
    try:
        interview = WeeklyInterviews.objects.get(id=interview_id)
        interview.delete()
        messages.success(request, 'Weekly interview deleted successfully.')
    except WeeklyInterviews.DoesNotExist:
        messages.error(request, 'Weekly interview not found.')
    return redirect('interview_list')

def delete_placement(request, placement_id):
    try:
        placement = Placements.objects.get(id=placement_id)
        placement.delete()
        messages.success(request, 'Placement deleted successfully.')
    except Placements.DoesNotExist:
        messages.error(request, 'Placement not found.')
    return redirect('placement_list')

def get_table_data(request, table_name):
    if table_name == 'ActiveJobPostings':
        data = ActiveJobPostings.objects.all()
    elif table_name == 'Applicants':
        data = Applicants.objects.all()
    elif table_name == 'Interviewer':
        data = Interviewer.objects.all()
    elif table_name == 'WeeklyInterviews':
        data = WeeklyInterviews.objects.all()
    elif table_name == 'Placements':
        data = Placements.objects.all()
    else:
        data = []

    context = {'data': data}
    return HttpResponse(render_to_string('table_data.html', context))
   
def delete_data(request):
    return render(request, 'pages/delete_data.html')

def tables(request):
  context = {
    'segment': 'tables'
  }
  return render(request, "pages/dynamic-tables.html", context)
