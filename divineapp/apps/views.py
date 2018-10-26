from django.shortcuts import render

#Views
def index(request):
    return render(request, 'apps/index.html')

def apps(request, app_id='1'):
    #TODO: access apps_id with 'app_id' variable
    return render(request, 'apps/apps.html')
