from BoxSetting import BoxSetting
from PlayerAccount import PlayerAccount
from newBox import newBox

player = PlayerAccount()

def play():
    while True:
        print("Spiele ein Spiel um Geld zu Verdienen? = MoneyGame")
        print("Kaufe Lootboxen? = BuyBox")
        print("Verkaufe Lootboxen? = SellBox")
        print("Öffne Lootboxen? = OpenBox")
        print("Verkaufe Skins? = SellSkin")
        print("Infos über deinen Account? = Info")
        print("Aufhören? = exit")
        x = input("Was möchtest du machen?")
        
        if x == "MoneyGame":
            player.play_moneygame()
        
        if x == "BuyBox":
            player.buy_box()
            print(player.konto)
            
        if x == "SellBox":
            player.sell_box()
            print(player.konto)
            
        if x == "OpenBox":
            player.open_box()
            
        if x == "SellSkin":
            player.sell_skins()
            print(player.konto)
            
        if x == "Info":
            player.info()
            
        if x == "exit":
            break
play()

#Box = newBox()
            
