import requests
from django_lol_project.champion_app.lol_data.Reference_ import champ_list, version, url_

class Champion:
    def __init__(self, list_index):
        self.name_index = champ_list[list_index]

        self.url = url_.format(version, champ_list[list_index])
        self.url_image_loading = 'ddragon.leagueoflegends.com/cdn/img/champion/loading/{}_0.jpg'.format(self.name_index)

        req_ = requests.get(self.url)
        res_ = req_.json()

        self.dict_ = res_.get('data')

        self.name = self.dict_[self.name_index]['name']
        self.key = self.dict_[self.name_index]['key']
        self.classification = self.dict_[self.name_index]['tags']
        self.attack = self.dict_[self.name_index]['info']['attack']
        self.defense = self.dict_[self.name_index]['info']['defense']
        self.magic = self.dict_[self.name_index]['info']['magic']
        self.difficulty = self.dict_[self.name_index]['info']['difficulty']
        self.description = self.dict_[self.name_index]['lore']

        self.li = [self.name, self.classification, self.description]