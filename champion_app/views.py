from django.shortcuts import render



def homeview(request):

    return render(request,'champion_app/home.html')

def championpage(request):
    return render(request, 'champion_app/champion_page.html')
