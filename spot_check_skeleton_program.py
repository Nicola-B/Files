#Nicola Batty
#03/03/2015
#Files and records spot check game database progam

import pickle

class blank_game_record:
    def __init__(self):
        self.name = None
        self.platform = None
        self.genre = None
        self.cost = None
        self.number_of_players = None
        self.online_functionality = None

def load_games():
    try:
        with open("game database.dat", mode="rb") as game_database:
            games = pickle.load(game_database)
    except FileNotFoundError:
        games = []
    return games  

def save_games(games):
    with open("game database.dat", mode="wb") as game_database:
        pickle.dump(games,game_database)

#the parameter is games because eventually you will be displaying
#multiple games using this function
def display_games(games):
    print ("_"*93)
    print ("|{0:<20}|{1:<11}|{2:<13}|{3:<5}|{4:<17}|{5:<20}|".format("Name", "Platform", "Genre", "Cost", "Number of players", "Online functionality"))
    print ("_"*93)
    line = blank_game_record()
    for line in games:
        print ("|{0:<20}|{1:<11}|{2:<13}|{3:<5}|{4:<17}|{5:<20}|".format(line.name, line.platform, line.genre, line.cost, line.number_of_players, line.online_functionality))
        print ("_"*93)
    
    

def get_game_from_user(games):
    game = True
    while game:
        game_record = blank_game_record()
        name = input("Please enter the name of the game(-1 to end list): ")
        if name == "-1":
            game = False
        else:
            platform = input("Please enter the platform of the game(e.g. XBox, PlayStation, PC etc.): ")
            genre = input("Please enter the genre of the game: ")
            cost = input("Please enter the cost of the game: £ ")
            number_of_players = input("Please enter the nunber of players in the game: ")
            online_funcionality = input("Please enter the online funcionality of the game(i.e. if it has online funcionality or not): ")
            game_record.name = name
            game_record.platform = platform
            game_record.genre = genre
            game_record.cost = cost
            game_record.number_of_players = number_of_players
            game_record.online_functionality = online_funcionality
            games.append(game_record)
    return games
    
def display_menu():
    print()
    print("***Welcome to the Computer and Video Game Database***")
    print()
    print("1. Add new games")
    print("2. Display games")
    print("3. Exit program")
    print()

def what_number():
    try:
        selected_option = int(input("Please select a menu option: "))
    except ValueError:
        print("This is not a number plases enter the number 1, 2 or 3")
        selected_option = what_number()
    return selected_option

def main():
    games = load_games()
    exit_program = False
    while not exit_program:
        display_menu()
        selected_option = what_number()
        if selected_option == 1:
            games = get_game_from_user(games)
        elif selected_option == 2:
            display_games(games)
        elif selected_option == 3:
            save_games(games)
            exit_program = True
        else:
            print("Please enter a valid option (1-3)")
            print()
    

if __name__ == "__main__":
    main()
