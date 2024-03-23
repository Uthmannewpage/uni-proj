from django import forms
from .models import ActiveJobPostings, Applicants, Interviewer, WeeklyInterviews, Placements

class ActiveJobPostingsForm(forms.ModelForm):
    class Meta:
        model = ActiveJobPostings
        fields = '__all__'

class ApplicantsForm(forms.ModelForm):
    class Meta:
        model = Applicants
        fields = '__all__'

class InterviewerForm(forms.ModelForm):
    class Meta:
        model = Interviewer
        fields = '__all__'

class WeeklyInterviewsForm(forms.ModelForm):
    class Meta:
        model = WeeklyInterviews
        fields = '__all__'

class PlacementsForm(forms.ModelForm):
    class Meta:
        model = Placements
        fields = '__all__'
