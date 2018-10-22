from django.shortcuts import render


def index(request):
    return render(request,'home/index.html')

def contacts(request):
    # Content from request or data base extracted Here
    # and passed to the template for display
    return render(request, 'home/contacts.html')
