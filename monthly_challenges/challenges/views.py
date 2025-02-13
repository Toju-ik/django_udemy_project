from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

# Create your views here. This is for the exchanging of requests and responses with the view processing the request and returning a response
monthly_challenges = {
    "january": "Fast for 20 days this month!",
    "february": "Read 5 books this month!",
    "march": "Meditate every day for 10 minutes!",
    "april": "Try a new healthy recipe each week!",
    "may": "Go for a 30-minute walk daily!",
    "june": "Learn a new language phrase daily!",
    "july": "Practice gratitude by writing daily!",
    "august": "Spend one hour on a hobby each day!",
    "september": "Declutter one room of your house!",
    "october": "Volunteer for a local charity!",
    "november": "Write a daily journal entry!",
    "december": "Reflect on your achievements and set new goals!"
}

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    forward_month = months[month]
    redirect_path = reverse("monthly_challenge", args=[forward_month])
    return HttpResponseRedirect("/challenges/" + forward_month)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}<h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not supported!!<h1>")

