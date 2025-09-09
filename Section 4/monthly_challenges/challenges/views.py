from django.http import (
    HttpResponse,
    HttpResponseNotFound,   
    HttpResponseRedirect,
    Http404,
)
from django.urls import reverse
from django.template.loader import render_to_string
from django.shortcuts import render

month_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Read a new book and finish it by the end of the month!",
    "may": "Try a new healthy recipe every week!",
    "june": "Go for a run three times a week!",
    "july": "Practice meditation for 10 minutes daily!",
    "august": "Drink at least 2 liters of water every day!",
    "september": "Write a journal entry every day!",
    "october": "Declutter one area of your home each week!",
    "november": "Volunteer for a local cause or charity!",
    "december": None,
}


def index(request):
    return render(request, "challenges/index.html", {
        "month_challenges": list(month_challenges.keys())
    })


# Dynamic Parameter
def month_challenge(request, month):
    try:
        # print(month_challenges)
        challenge_text = month_challenges[month]
        # response_data = f"<h1>{challenge_text}</h1>"
        response_data = render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month
        })
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>Invalid month!</h1>")


# Dynamic Parameter as number
def month_challenge_by_number(request, month):
    try:
        months = list(month_challenges.keys())
        month_name = months[month - 1]
        redirect_path = reverse(
            "month-challenge", args=[month_name]
        )  # /challenges/january
        return HttpResponseRedirect(redirect_path)
    except:
        raise Http404()
