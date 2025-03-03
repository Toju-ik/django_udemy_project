from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.template.loader import  render_to_string


# Create your views here. This is for the exchanging of requests and responses with the view processing the request and returning a response

# dictionary
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

def index(request):

    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalize_month = month.capitalize()
        month_path = reverse("monthly_challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalize_month}</a></li>"

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("<h1>This month is not supported!!<h1>")
    
    redirect_month = months[month -1]
    redirect_path = reverse("monthly_challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "challenge_text": challenge_text,
            "month": month.capitalize() + ""
        })
    except:
        return HttpResponseNotFound("<h1>This month is not supported!!<h1>")

