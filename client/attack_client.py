import os
import requests
from business_object.attack_factory import AttackFactory
from business_object.attack_factory import AbstractAttack


END_POINT = "/attack"

class Attack_client():

    def __init__(self) -> None:
        self.__HOST = os.environ["HOST_WEBSERVICE"]


    def get_attack(self, id:int):
        req = requests.get(f"{self.__HOST}{END_POINT}/{id}")

        # Check if the request is ok
        attack = None
        if req.status_code==200:
            raw_attack = req.json()
            attack_factory = AttackFactory()
            attack = attack_factory.instantiate_attack(
                type = raw_attack['attack_type']
                , id = raw_attack["id"]
                , power = raw_attack['power']
                , name = raw_attack['name']
                , description = raw_attack["description"]
            )
        return attack




    def get_all_attacks(self):
        pass


    def get_pokemon(self, nom_de_Pokemon):
        pass


if __name__ == "main":
    response = get_attack(3)
    print(response.json())

