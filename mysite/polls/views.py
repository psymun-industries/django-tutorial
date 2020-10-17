from django.http import HttpResponse


def index(request):
    return HttpResponse("Shiver me timbers, You're at the polls index.")
