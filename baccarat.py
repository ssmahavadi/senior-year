# Baccarat

class Card(object):
    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    SUITS = ["C", "D", "H", "S"]

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        if self.rank == "A":
            self.value = 1
        elif self.rank == "10" or self.rank == "J" or self.rank == "Q" or self.rank == "K":
            self.value = 0
        else:
            self.value = int(self.rank)

    def __str__(self):
        rep = self.rank + self.suit
        return rep
    
      
class Hand(Card):
    def __init__(self):
        self.cards = []
        self.sums = 0

    def __str__(self):
        if self.cards:
           rep = ""
           for card in self.cards:
               rep += str(card) + "\t"
        else:
            rep = "<empty>"
        return rep

    def add(self, card):
        self.cards.append(card)

    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)

    def isNatural(self):
        if len(self.cards) == 2 and 8 <= self.sums <= 9:
            return True
        else:
            return False

    def sameSuit(self):
        if (self.cards[0].suit == self.cards[1].suit):
            return True
        else:
            return False

    def sum (self):
        print (self)
        #code to deal initial hand
        if len(self.cards) == 2:
            self.sums = 0
            for card in self.cards:
                self.sums += card.value
        #code to deal additional/third card
        else:
            self.sums += self.cards[2].value
        self.sums %= 10
        return self.sums
    

class Deck(Hand):
    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS: 
                self.add(Card(rank, suit))

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    
    def deal(self, hand, per_hand = 2):
        for rounds in range(per_hand):
            if self.cards:
                top_card = self.cards[0]
                self.give(top_card, hand)
            else:
                print("Can't continue deal. Out of cards!")
        #returns value of additional/third card
        if per_hand==1:
            return top_card.value

class Player(object):
    #only use to deal with money
    def __init__(self):
        self.pot = 100

    def setBets(self, opinion, normal, bonus1, bonus2):
        self.opinion = opinion #whether the person thinks the Player, Banker, or Tie will win
        self.normalBet = normal #normal bet value
        self.bonus1 = bonus1 #same suit bet value
        self.bonus2 = bonus2 #natural win bet value

    def normal(self, result):
        if self.opinion == result and result == "Tie":
            self.pot += self.normalBet * 8
        elif self.opinion == result and result == "Banker":
            self.pot += int(self.normalBet * 0.95)
        elif self.opinion == result and result == "Player":
            self.pot += self.normalBet
        else:
            self.pot -= self.normalBet
        return self.pot

    def sameSuit(self, pSuit, bSuit):
        if (not(pSuit == "")) and (pSuit == bSuit):
            self.pot += self.bonus1 * 250
        elif (not(pSuit == "")) or (not(bSuit == "")):
            self.pot += self.bonus1 * 25
        else:
            self.pot -= self.bonus1
        return self.pot
            
    def naturalWins(self, natural):
        #If you win with a natural eight or nine, casinos pay 9:1
        if natural:
            self.pot += self.bonus2 * 9
        else:
            self.pot -= self.bonus2
        return self.pot


class Game(object):
    def __init__(self):
        self.player = Hand()
        self.banker = Hand()
        self.result = ""
        self.natural = False
        self.psameSuit = ""
        self.bsameSuit = ""
    
        self.deck = Deck()
        self.deck.populate()
        self.deck.shuffle()

    def play(self):
        #deal two initial cards to everyone
        self.deck.deal(self.player, per_hand=2)
        self.deck.deal(self.banker, per_hand=2)

        if(self.player.cards[0].suit == self.player.cards[1].suit):
            self.psameSuit = self.player.cards[0].suit
        if(self.banker.cards[0].suit == self.banker.cards[1].suit):
            self.bsameSuit = self.banker.cards[0].suit

        self.player.sum()
        pSum = self.player.sums
        self.banker.sum()
        bSum = self.banker.sums


        #outcomes
        if self.player.isNatural() and self.banker.isNatural():
            #self.natural = True
            if(pSum>bSum):
                self.result = "Player"
            elif(bSum>pSum):
                self.result = "Banker"
            else:
                self.result = "Tie"
        
        elif self.player.isNatural():
            self.natural = True
            self.result = "Player"

        elif self.banker.isNatural():
            self.result = "Banker"

        elif 6 <= pSum <= 7:    #player stands
            if bSum <= 5:
                self.deck.deal(self.banker, per_hand=1)
                self.banker.sum()
                bSum = self.banker.sums

            if(pSum>bSum):
                self.result = "Player"
            elif(bSum>pSum):
                self.result = "Banker"
            else:
                self.result = "Tie"

        elif pSum <= 5:     #player draws third card
            pAddCard = self.deck.deal(self.player, per_hand=1)
            self.player.sum()
            pSum = self.player.sums
        
            if bSum <= 2:
                self.deck.deal(self.banker, per_hand=1)
                self.banker.sum()
                bSum = self.banker.sums

            elif bSum == 3 and (not pAddCard == 8):
                self.deck.deal(self.banker, per_hand=1)
                self.banker.sum()
                bSum = self.banker.sums

            elif bSum == 4 and (2 <= pAddCard <= 7):
                self.deck.deal(self.banker, per_hand=1)
                self.banker.sum()
                bSum = self.banker.sums

            elif bSum == 5 and (4 <= pAddCard <= 7):
                self.deck.deal(self.banker, per_hand=1)
                self.banker.sum()
                bSum = self.banker.sums

            elif bSum == 6 and (6 <= pAddCard <= 7):
                self.deck.deal(self.banker, per_hand=1)
                self.banker.sum()
                bSum = self.banker.sums

            if(pSum>bSum):
                self.result = "Player"
            elif(bSum>pSum):
                self.result = "Banker"
            else:
                self.result = "Tie"

        #result output
        if self.result == "Tie":
            print ("It's a tie!")
        else:
            print (self.result + " wins.")
        
        return self.result
        

def main():
    print("Welcome to Baccarat!\n")

    players = []
    numberPlayer = int(input("How many players? (1 - 3): "))

    again = "None"
    while (not(again == 'n')) and (numberPlayer>0):
        for i in range(numberPlayer):
            if again == "None":
                play = Player()
                pot = play.pot
            if again == 'y':
                pot = players[i].pot
                
            q1 = input("Would Player " + str(i+1) + " like to bet on the result? (Enter y/n): ")
            normalOption = ""
            normalBet = 0
            if q1 == 'y':
                normalOption = input("Who/what would you like to bet on? (Player, Banker, Tie): ")
                while (not(10<=normalBet<=pot)):
                    normalBet = int(input("How much would you like to bet on the result? (min: $10; max: $" + str(pot) + "): "))
                pot -= normalBet
                    
            q2 = input("Would Player " + str(i+1) + " like to place a bet on 'Same Suit'? (Enter y/n): ")
            bonus1 = 0
            if q2 == 'y':
                while (not(10<=bonus1<=pot)):
                    bonus1 = int(input("How much would you like to bet on 'Same Suit'? (min: $10; max: $" + str(pot) + "): "))
                pot -= bonus1
            
            q3 = input("Would Player " + str(i+1) + " like to bet on 'Natural Wins'? (Enter y/n): ")
            bonus2 = 0
            if q3 == 'y':
                while (not(10<=bonus2<=pot)):
                    bonus2 = int(input("How much would you like to bet on 'Natural Wins'? (min: $10; max:$ " + str(pot) + "): ")) 
                pot -= bonus2
            
            play.setBets(normalOption, normalBet, bonus1, bonus2)
            if again == "None":
                players.append(play)
        
        game = Game()
        #for normal bet
        result = game.play()
        #for natural wins bet
        natural = game.natural
        #for same suit bet
        playerSuit = game.psameSuit
        bankerSuit = game.bsameSuit
        for i in range(0, numberPlayer):
            oldPot = players[i].pot
            
            if players[i].normalBet > 0:
                newPot = players[i].normal(result)
                if newPot < oldPot:
                    print("Player " + str(i+1) + ": You lost the Normal Bet. Your pot total is now $" + str(newPot) + ".")
                else:
                    print("Player " + str(i+1) + ": You won the Normal Bet. Your pot total is now $" + str(newPot) + ".")
                oldPot = newPot
                
            if players[i].bonus1 >0:
                newPot = players[i].sameSuit(playerSuit, bankerSuit)
                if newPot < oldPot:
                    print("Player " + str(i+1) + ": You lost the Same Suit Bet. Your pot total is now $" + str(newPot) + ".")
                else:
                    print("Player " + str(i+1) + ": You won the Same Suit Bet. Your pot total is now $" + str(newPot) + ".")
                oldPot = newPot
                          
            if players[i].bonus2 > 0:
                newPot = players[i].naturalWins(natural)
                if newPot < oldPot:
                    print("Player " + str(i+1) + ": You lost the Natural Wins Bet. Your pot total is now $" + str(newPot) + ".")
                else:
                    print("Player " + str(i+1) + ": You won the Natural Wins Bet. Your pot total is now $" + str(newPot) + ".")
                oldPot = newPot

            if oldPot <= 0:
                players.pop(i)
                numberPlayer = len(players)
            if not len(players) == 0:
                again = input("Do you want to play again? (Enter y/n): ")
            else:
                again = 'n'

main()
