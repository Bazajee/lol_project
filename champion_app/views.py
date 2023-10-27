from django.shortcuts import render


from champion_app.game_data import Variable_


def homeview(request):

    return render(request,'champion_app/home.html')

def championpage(request):

    Aatrx = Variable_.Aatrox
    return render(request, 'champion_app/champion_page.html', context={"Aatrx": Aatrx, })
