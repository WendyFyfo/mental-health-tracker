from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306223906',
        'name': 'Muhammad Wendy Fyfo Anggara',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)
# Create your views here.
