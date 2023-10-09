from django.shortcuts import render


from ._variable_ import Variable_, Class_


def homeview(request):

    return render(request,'champion_app/home.html')

def championpage(request):

    Aatrx = Variable_.aatrx
    return render(request, 'champion_app/champion_page.html', context={"Aatrx": Aatrx,})
