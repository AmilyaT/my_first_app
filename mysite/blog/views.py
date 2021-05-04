from django.http import HttpResponse

# Create your views here.

def my_info(request):
    data = {
        "Name" : "Amilya Teasley",
        "Track" : "Backend Python",
        "Message" : "You guys are doing an excellent job! I'm learning a lot, but this is really HARD for a newbie"
    }
    return HttpResponse(data.items())
    