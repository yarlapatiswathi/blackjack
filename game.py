import random
cards=['2','3','4','5','6','7','8','9','10','J','Q','K','A']
suits=['heart','club','spades','diamonds']
values={'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'K':10,'Q':10,'J':10,'A':11}

class Cards:
    def __init__(self,card,suit):
        self.card=card
        self.suit=suit
        self.value=values[card]
    def __str__(self):
        return f"{self.card} {self.suit}"

class Deck:
    def __init__(self):
        self.all_card_objs=[]
        for suit in suits:
            for card in cards:
                self.all_card_objs.append(Cards(card,suit))
    def shuffle_obj(self):
        random.shuffle(self.all_card_objs)
    def HIT(self):
        return self.all_card_objs.pop()


class Player:
    def __init__(self):
        
        self.player_cards=[]
 
    def total(self):
        total_value=0
        for card in self.player_cards:
            total_value+=card.value
        if card.value==11 and total_value>21:
            total_value-=10 
        return total_value   
        
class Dealer:
    def __init__(self):
        self.dealer_cards=[]
        self.ace=0
    def total(self):
        total_value=0
        
        for card in self.dealer_cards:
            total_value+=card.value
        if card.value==11:
            self.ace+=1
        while total_value>21 and self.ace:
                total_value-=10    
        return total_value               

player=Player()
dealer=Dealer()
deck=Deck()
deck.shuffle_obj()
game_on=True
print("Player cards")
while game_on:
    for i in range(2):
        player.player_cards.append(deck.HIT())
        dealer.dealer_cards.append(deck.HIT())
        print(player.player_cards[i])
    print("dealer cards")    
    print(dealer.dealer_cards[i])
    print("players total= ",player.total())
    game=''
    pick=input("Do u want to pick a card(y/n)").lower()
    while pick=='y':
            player.player_cards.append(deck.HIT())
            print("new player card",player.player_cards[-1])
            print("new player total",player.total())            
            if player.total()>21:
                game='bust'
                print("Player Bust")
                print("Dealer won")
                game_on=False
                break
            pick=input("Do you still want to pick a card")
                
    else:
        while dealer.total()<=17:
                dealer.dealer_cards.append(deck.HIT())
                print("dealer HIT the card")         
                if dealer.total()>21:
                    game='bust'
                    print("Dealer Bust")
                    print("player won")
                    game_on=False
                    break 
        else:
            break
print("dealers total",dealer.total())
print("dealers cards",*dealer.dealer_cards)
print("players total",player.total())
print("players cards",*player.player_cards)                    
if game!='bust': 
    if player.total()<=21 and player.total()>dealer.total():
        print("Player Won!")
    elif dealer.total()<=21 and player.total()<dealer.total():
        print("Dealer won")
    elif dealer.total()==player.total():
        print("game tie")       


