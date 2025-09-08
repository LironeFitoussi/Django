from django.http import (
    HttpResponse,
    HttpResponseNotFound,
    HttpResponseRedirect,
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
    "december": "Reflect on your year and set goals for the next year!",
}


def index(request):
    list_items = ""
    for month in month_challenges.keys():
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
        #<li><a href="/challenges/january">January</a>...etc</li>
    response_data = f"""
        <ul>
            {list_items}
        </ul>
    """
    return HttpResponse(response_data)


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
        return HttpResponseNotFound("Invalid month!")
