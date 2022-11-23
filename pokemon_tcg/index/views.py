from django.shortcuts import render

# create a function


def index(request):

    # return response
    return render(request, "index/index.html")
