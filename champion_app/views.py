from django.shortcuts import render


from champion_app.game_data import Variable_


def homeview(request):

    return render(request,'champion_app/home.html')

def championpage(request):

    Aatrox_name, Aatrox_desctiption = Variable_.Aatrox.name, Variable_.Aatrox.description
    champ_class_list = Variable_.champ_class_list
    return render(request, 'champion_app/champion_page.html', context={"Aatrox_name": Aatrox_name,"Aatrox_description":Aatrox_desctiption, "champ_class_list": champ_class_list, })
