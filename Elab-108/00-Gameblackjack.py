import random, time

class Card():
    ''' Card(): create a card object. To create a deck, try \Card.test_Card()\! '''
    symbols = {"D":"♦", "C":"♣", "H":"♥", "S":"♠"}
    def __init__(self, name, suit):
        self.name = name
        self.suit = suit
    def get_name(self):
        return self.name
    def get_suit(self):
        return self.suit
    def __repr__(self):
        return f"{self.name}{Card.symbols[self.suit]}"
    def test_Card():
        Names = ['A',2,3,4,5,6,7,8,9,'T','J','Q','K']
        Suits = ['D','C','H','S']
        deck = [Card(str(n), s) for s in Suits for n in Names]
        random.shuffle(deck)
        res = [str(card) for card in deck]
        return ' '.join(res)
    #---------------------------------------------------------------------
    def render(self, x, y, color='blue', RENDER=False):
        if not RENDER:
            return None
        # Draw border
        pen.penup()
        pen.color(color)
        pen.goto(x+50, y+75)
        xy = ((x+50, y+75), (x+50, y-75), (x-50, y-75), (x-50, y+75))
        pen.begin_fill()
        pen.pendown()
        for pos in xy:
            pen.goto(pos)
        pen.end_fill()
        pen.penup()
        # Draw card info
        if self.name not in ['','O']:
            # Draw suit in the middle
            pen.color('white')
            pen.goto(x-18, y-30)
            pen.write(self.symbols[self.suit], False, font=("Courier New", 48, "normal"))
            # Draw top left
            pen.goto(x-40, y+45)
            pen.write(self.name, False, font=("Courier New", 18, "normal"))
            pen.goto(x-40, y+25)
            pen.write(self.symbols[self.suit], False, font=("Courier New", 18, "normal"))
            # Draw bottom right
            pen.goto(x+30, y-60)
            pen.write(self.name, False, font=("Courier New", 18, "normal"))
            pen.goto(x+30, y-80)
            pen.write(self.symbols[self.suit], False, font=("Courier New", 18, "normal"))
        pen.penup()
    #---------------------------------------------------------------------

class Deck:
    Names = ['A',2,3,4,5,6,7,8,9,'T','J','Q','K']
    Suits = ['D','C','H','S']
    def __init__(self):
        Names, Suits = Deck.Names, Deck.Suits
        self.cards = [Card(str(n), s) for s in Suits for n in Names]
    def shuffle(self):
        random.shuffle(self.cards)
    def get_card(self):
        return self.cards.pop()
    def set_cards(self, cards):
        self.cards = cards
    def reset(self, n=1):
        Names, Suits = Deck.Names, Deck.Suits
        self.cards = [Card(str(n), s) for s in Suits for n in Names]
        for i in range(n):
            self.shuffle()
    def __repr__(self):
        res = [str(x) for x in self.cards]
        return ' '.join(res)

def preamble(RENDER=False):
    ''' จัดการ environment ในการวาดเต่า '''
    if not RENDER:
        return None
    #--------------------------------------------------------------------------------------
    global wn, pen
    wn, pen = turtle.Screen(), turtle.Turtle()
    wn.bgcolor('black')
    wn.setup(800, 600)
    wn.title('Deck of Cards Simulator by @TokyoEdtech, rebrewed by KunTotoNaMikeLabDotNet')
    pen.speed(0)
    pen.hideturtle()
    #--------------------------------------------------------------------------------------

def test_turtle_deck(RENDER=False):
    ''' ไว้ตรวจสอบเต่าวาดไพ่ ฟังชัน Card.render() '''
    preamble(RENDER)
    # create a deck f card
    deck = Deck()
    # shuffle deck
    deck.reset()
    print(deck)
    # render n cards (back) in a row
    nbOfCards = 5
    start_x = -250
    for x in range(nbOfCards):
        card = Card('', '')
        card.render(start_x + x*125, 175, 'orange', RENDER=True)
    time.sleep(1)
    # re-render n cards in a row
    start_x = -250
    for x in range(nbOfCards):
        card = deck.get_card()
        card.render(start_x + x*125, 175, RENDER=True)
    print('Done..')

def createVirtualDeck(s='K♣ Q♠ A♣ 3♥ 2♠ 6♥ 8♥ 9♥ J♠ 4♦ 2♥ 9♠'):
    dd = s.split()
    res = []
    suit = {'♦':'D','♣':'C','♥':'H','♠':'S'}
    for d in dd:
        card = Card(d[0], suit[d[1]])
        res.append(card)
    deck = Deck()
    deck.set_cards(res)
    return deck
###
# test_turtle_deck(True)
###
#--------------------------------------------------------------------------------------
# put your additional class or def (aka., utilities) here
# for example,
# class myCards:
#     ''' myCard(): ลิสเก็บไพ่ที่ผู้เล่นถืออยู่ '''
#     pass
#
# def print_result(com, player, com_score, player_score):
#     pass
#--------------------------------------------------------------------------------------

class Playslot:
    def __init__(self, name='', inhand=None, score=0 , com = False):
        if inhand is None:
            inhand = []
        self.name = name
        self.inhand = inhand
        self.scorelist = [0]
        self.score = score
        self.n_card = 0
        self.n_ace = 0
        self.stophit = False
        self.com = com
        self.gotfirstA = False
        self.gotsecondA = False
        self.got5cards = False

    def get_cards(self) -> str:
        if self.com:
            return f"O{Card.symbols[self.inhand[0].get_suit()]} " + " ".join(map(str, self.inhand[1:]))
        else:
            return " ".join(map(str, self.inhand))

    def count_point(self) -> int:
        aces = self.n_ace
        p = 0
        ten = ['T', 'J', 'Q', 'K']
        i = 0
        for card in self.inhand:
            name = card.get_name()
            if name in ten:
                p += 10
            elif name == 'A':
                aces += 1
                p += 11
            elif name in ['2', '3', '4', '5', '6', '7', '8', '9']:
                p += int(name)
            i += 1
        # p += aces * 11
        while p > 21 and aces > 0:
            p -= 10
            aces -= 1
        return p

    def cal_score(self) -> int:
        self.score = self.count_point()
        return self.count_point()

    def hit_card(self, card=None):
        if card is None:
            card = Deck().get_card()
        self.inhand.append(card)
        self.score = self.cal_score()
        self.n_card += 1
        for card in self.inhand:
            name = card.get_name()
            if name == 'A' and self.gotfirstA:
                self.gotsecondA = True
            if name == 'A':
                self.gotfirstA = True
        if self.score >=21 :
            self.stophit = True
        if self.n_card == 5:
            self.got5cards = True
            self.stophit = True
        self.scorelist.append(self.score)

    def get_score(self) -> int:
        return self.score

    def first_dealer(self):
        p = 0
        ten = ['T', 'J', 'Q', 'K']
        add_A = False
        for card in self.inhand:
            name = card.get_name()
            if name in ten:
                p += 10
            elif name == 'A':
                add_A = True
                p += 11
            elif name in ['2', '3', '4', '5', '6', '7', '8', '9']:
                p += int(name)
            if add_A and p > 21:
                p -= 10
        for card in self.inhand:
            name = card.get_name()
            if name in ten:
                p -= 10
                break
            elif name == 'A':
                add_A = True
                p -= 11
                break
            elif name in ['2', '3', '4', '5', '6', '7', '8', '9']:
                p -= int(name)
                break
        if add_A and p > 21:
            p += 10
        return p

    def __str__(self):
        if self.com:
            cards = self.get_cards()
            self.com = False
            return f"{self.name:>9}: {cards:<16}-> {self.first_dealer()}"
        else:
            return f"{self.name:>9}: {self.get_cards():<16}-> {self.get_score()}"

                        
"""
///
//
/
add tongtong Class&Function optional
/
//
///
"""
def play(player1='Computer', player2='Player', d=None, RENDER=False):
    preamble(RENDER)
    # create a deck of cards
    if d==None:
        deck = Deck()
        deck.reset()
    else:
        #----------------------------- virtual deck
        #d = 'A♦ A♥ 3♥ 4♣ 4♥ 7♣ 5♣ 6♦ A♠'
        deck = createVirtualDeck(d)
    #----------------------
    #print(deck) # for DEBUG
    #----------------------
    ###-------------- student code begins here --------------###
    computer = Playslot(player1,[],com=True)
    player = Playslot(player2,[])

    computer.hit_card(deck.get_card())
    player.hit_card(deck.get_card())
    computer.hit_card(deck.get_card())
    player.hit_card(deck.get_card())
    
    botsee = player.score
    
    # starting point
    print(computer)
    print(player)
    
    while not player.stophit :
        hit_input = input("Draw another card (y/n): ")
        if hit_input == "n" or hit_input == "N":
            break
        player.hit_card(deck.get_card())
        print(player)
        
    print("+++++++++++++++++++++++++++++++++") 
    
    s2 = player.score

    while computer.score <= 17 and computer.n_card < 5 and not computer.stophit:
        computer.hit_card(deck.get_card())
    while computer.score < botsee and computer.n_card < 5 and not computer.stophit:
        computer.hit_card(deck.get_card())
    while s2 == 21 and computer.n_card < 5 and not computer.stophit:
        computer.hit_card(deck.get_card())
    while player.n_card == 5 and computer.n_card < 5 and not computer.stophit:
        computer.hit_card(deck.get_card())

    print(computer)
    print(player)

    s1 = computer.score
    print("++++++++++++++++++++++++++++++++++++++++++++++++++ ")

    if s1 > 21 and s2 > 21 :
        print("Draw!")
    elif (s1 > 21 or s2 > 21) :
        if s1 <= 21:
            print(f"{computer.name} wins.")
        elif s2 <= 21:
            print(f"{player.name} wins.")
    else:
        if player.got5cards and computer.got5cards:
            print("Draw!")
        elif player.got5cards :
            if s1 == 21 and computer.n_card == 2:
                print("Draw!")
            else:
                print(f"{player.name} wins.")
        elif computer.got5cards:
            if s2 == 21 and player.n_card == 2:
                print("Draw!")
            else:
                print(f"{computer.name} wins.")
        else:
            if s1 < s2 :
                print(f"{player.name} wins.")
            elif s1 > s2:
                print(f"{computer.name} wins.")
            else:
                print("Draw!")

    print("++++++++++++++++++++++++++++++++++++++++++++++++++ ")
    
"""
///
// 
/
Play section
/
//
///
"""

print("Welcome to Tongvk Casino!")
print("--------------------------------------")
name = input("How sould I call you Please? : ")
i = 1

ch = input("Wanna Play BlackJack? (1-yes) / (2-no) >> ")
if ch == '1' or ch == 'yes':
    print(f"{name} sure has a lot of money.")
    random.seed()
    play(player2=name)
while ch == '1' or ch == 'yes':
    print("")
    print(f"Game played : {i}")
    i += 1
    ch = input("Wanna Play BlackJack again? (1-yes) / (2-no) >> ")
    if ch == '1' or ch == 'yes':
        random.seed()
        play(player2=name)
