from entities import *
import random

board = Board()

# Adding Real Estate

def add_real_estate_to_board(board):
    board.add_real_estate(RealEstate(re_name="Real Estate", buying_cost=80, rent_cost=8))
    board.add_real_estate(RealEstate(re_name="Real Estate", buying_cost=180, rent_cost=51))
    board.add_real_estate(RealEstate(re_name="Real Estate", buying_cost=200, rent_cost=60))
    board.add_real_estate(RealEstate(re_name="Real Estate", buying_cost=100, rent_cost=25))
    board.add_real_estate(RealEstate(re_name="Real Estate", buying_cost=150, rent_cost=35))
    board.add_real_estate(RealEstate(re_name="Real Estate", buying_cost=170, rent_cost=52))
    board.add_real_estate(RealEstate(re_name="Real Estate", buying_cost=160, rent_cost=45))
    board.add_real_estate(RealEstate(re_name="Real Estate", buying_cost=140, rent_cost=40))
    board.add_real_estate(RealEstate(re_name="Real Estate", buying_cost=210, rent_cost=70))
    board.add_real_estate(RealEstate(re_name="Real Estate", buying_cost=130, rent_cost=55))
    board.add_real_estate(RealEstate(re_name="Real Estate", buying_cost=120, rent_cost=33))
    board.add_real_estate(RealEstate(re_name="Real Estate", buying_cost=220, rent_cost=75))
    board.add_real_estate(RealEstate(re_name="Real Estate", buying_cost=90, rent_cost=25))
    board.add_real_estate(RealEstate(re_name="Real Estate", buying_cost=270, rent_cost=100))
    board.add_real_estate(RealEstate(re_name="Real Estate", buying_cost=110, rent_cost=44))
    board.add_real_estate(RealEstate(re_name="Real Estate", buying_cost=125, rent_cost=55))
    board.add_real_estate(RealEstate(re_name="Real Estate", buying_cost=70, rent_cost=20))
    board.add_real_estate(RealEstate(re_name="Real Estate", buying_cost=95, rent_cost=35))
    board.add_real_estate(RealEstate(re_name="Real Estate", buying_cost=280, rent_cost=70))
    board.add_real_estate(RealEstate(re_name="Real Estate", buying_cost=175, rent_cost=75))

add_real_estate_to_board(board)

# Adding Players
players = [
    RandomPlayer("0 Random"),
    CautiousPlayer("1 Cautious"),
    ImpulsivePlayer("2 Impulsive"),
    HighlyDemandingPlayer("3 Demanding")
]

board.add_players(players)
# board.shuffle_players()

# Rounds
for round in range(0, 1000):
    if len(board.players) < 2:
        print(board.players)
        break

    print("$" * 100)

    for n, player in enumerate(board.players):
        print(f" #{n} - {player.balance}")

    for n, player in enumerate(board.players):

        

        if not player.is_in_the_game:
            pass

        else:

            player.walk()
            real_estate = board.real_estate[player.board_position]

            print(f" Casa #{player.board_position}")

            if real_estate.buyable():
                print(f"Player #{n} - Casa #{player.board_position} é compravel? {real_estate.buyable()}")
                player.is_buying_opportunity(real_estate)
                print(f"Player #{n} - Casa #{player.board_position} é compravel? {real_estate.buyable()}")

            if (real_estate.owner is not None and real_estate.owner is not player):
                print(f"Casa #{player.board_position} - SENHOR BARRIGA AQUI")
                real_estate.pay_rent(player)

            kicked = player.kick_player()

            if not kicked:
                print(f"player #{n} ({player}) has been kicked")
            
            print(f" #{n} - {player.balance}")
    
    for n, player in enumerate(board.players):
        print(f" #{n} - {player.balance}")
            
print(board.players)
print("Finished")        



