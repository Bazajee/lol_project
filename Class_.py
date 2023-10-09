import Variable_
import requests

class Champion:
    def __init__(self, list_index):
        self.name_index = Variable_.champ_list[list_index]

        self.url = Variable_.url_.format(Variable_.version, Variable_.champ_list[list_index])
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

        #self.list = list(self.dict_[self.name_index])