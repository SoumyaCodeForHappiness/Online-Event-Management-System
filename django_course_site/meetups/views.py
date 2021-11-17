from django.shortcuts import render, redirect
# from django.http import HttpResponse
from .models import Meetup, Participant

from .forms import RegistrationForm
# Create your views here.

def index(request):
    # this data we defined on our own
    # meetups = [
    #     { 'title': 'A first meetup', 'location': 'New York', 'slug': 'a-first-meetup'},
    #     {'title': 'A second meetup', 'location': 'Paris', 'slug': 'a-second-meetup'}
    # ]

    # this is from data-base
    meetups = Meetup.objects.all()
    return render(request,'meetups/index.html',{
        'meetups': meetups
    })


def meetup_details(request, meetup_slug):
    # selected_meetup = {
    #     'title': 'A first meetup!',
    #     'description': 'this is the first meetup'

    # from data-base
    try:
        selected_meetup = Meetup.objects.get(slug=meetup_slug)
        if request.method == 'GET':
            registration_form = RegistrationForm()
        else:
            registration_form = RegistrationForm(request.POST)
            if registration_form.is_valid():
                # participant = registration_form.save()
                user_email = registration_form.cleaned_data['email']
                participant, _ = Participant.objects.get_or_create(email=user_email)
                selected_meetup.Participants.add(participant)
                return redirect('confirm-registration',meetup_slug = meetup_slug)
        return render(request, 'meetups/meetup-details.html', {
                'meetup_found': True,
                'meetup': selected_meetup,
                'form': registration_form
            })
    except Exception as exc:
        print(exc)
        return render(request, 'meetups/meetup-details.html', {
            'meetup_found': False,
        })

def confirm_registration(request, meetup_slug):
    meetup = Meetup.objects.get(slug=meetup_slug)
    return render(request, 'meetups/registration-success.html', {
        'organizer_email': meetup.organizer_email
    })
