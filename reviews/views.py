from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "base.html")

def search(request):
    search = request.GET.get("search") or ""
    return render(request, "book_search.html", {"search": search})
