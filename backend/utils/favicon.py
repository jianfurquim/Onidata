from django.http import HttpResponse


def empty_favicon(request):
    return HttpResponse(status=204)
