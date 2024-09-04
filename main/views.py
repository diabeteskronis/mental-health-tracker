from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306221062',
        'name': 'Andharu Hanif Achmadsyah',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)