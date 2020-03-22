import random

class Board:
    def __init__(self):
        self.real_estate = []
        self.players = []
    
    def add_real_estate(self, real_estate):
        self.real_estate.append(real_estate)

    def add_players(self, players):
        self.players = players
    
    def shuffle_players(self):
        random.shuffle(self.players)


class Player:
    def __init__(self, name, initial_balance=300.00):
        self.name = name
        self.balance = initial_balance
        self.is_in_the_game = True
        self.board_position = 0
        self.initial_balance = initial_balance

    def subtract_from_balance(self, amount):
        self.balance = self.balance - amount

    def owner_has_amount_available(self, needed_amount):
        return True if self.balance >= needed_amount else False

    def kick_player(self):
        if self.balance < 0:
            self.is_in_the_game = False
        return self.is_in_the_game

    def walk(self):
        thrown_dice = random.choice(range(1, 7))
        self.board_position += thrown_dice

        if self.board_position > 19:
            print(f"{self.name} RECEBEU PELA RODADA")
            self.board_position -= 19
            self.balance += self.initial_balance

        return self.board_position
    


class RandomPlayer(Player):
    def is_buying_opportunity(self, real_estate):
        if (real_estate.owner is None and self.balance >= real_estate.buying_cost
            and random.choice([True, False])):
            real_estate.buy(self)
            return True
        
        return False


class CautiousPlayer(Player):
    def is_buying_opportunity(self, real_estate):
        if (real_estate.owner is None and (self.balance - 80) >= real_estate.buying_cost):
            real_estate.buy(self)
            return True
        
        return False


class ImpulsivePlayer(Player):
    def is_buying_opportunity(self, real_estate):
        if (real_estate.owner is None and self.balance >= real_estate.buying_cost):
            real_estate.buy(self)
            return True
        
        return False


class HighlyDemandingPlayer(Player):
    def is_buying_opportunity(self, real_estate):
        if (real_estate.owner is None and self.balance >= real_estate.buying_cost 
            and real_estate.rent_cost > 50):
            real_estate.buy(self)
            return True
        
        return False


class RealEstate:
    def __init__(self, re_name, buying_cost, rent_cost, owner=None):
        self.re_name = re_name
        self.buying_cost = buying_cost
        self.rent_cost = rent_cost
        self.owner = owner

    def buyable(self):
        if self.owner:
            return False
        return True

    def buy(self, possible_owner):
        if self.buyable():
            if possible_owner.owner_has_amount_available(self.buying_cost):
                possible_owner.subtract_from_balance(self.buying_cost)
                self.owner = possible_owner
                return True
        return False

    def pay_rent(self, player):
        if not self.buyable():
            print(f"{self.owner.name} recebeu aluguel")
            player.subtract_from_balance(self.rent_cost)
            self.owner.balance += self.rent_cost
            return True

    def bank_reposetion(self):
        self.owner = None
        return True
