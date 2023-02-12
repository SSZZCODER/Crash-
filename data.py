import json
from items import Item
from player import Player

class saveData:
    def save():
        
        f = open("savedata.json", "w")
        playerdata = {}
        playerdata["position"] = [Player.player_x, Player.player_y]
        playerdata["health"] = Player.health
        playerdata["inventory"] = []
        small = {}
        
        for i in range(Player.playerInventory.amount):
            small[Player.playerInventory[i].name] = Player.playerInventory[i].amount
        playerdata["inventory"].append(small) 
        json.dump(playerdata,f)
        f.close()
       
