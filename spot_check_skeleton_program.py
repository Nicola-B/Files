#Nicola Batty
#03/03/2015
#Files and records spot check game database progam

#import pdb

class blank_game_record:
    def __init__(self):
        self.name = None
        self.platform = None
        self.genre = None
        self.cost = None
        self.number_of_players = None
        self.online_functionality = None

def load_games(filename):
    open(filename, mode="a",encoding="utf-8") game_data:
        main()

def save_games(filename, games):
    open(filename, mode="w", encoding="utf-8") as game_data:
        game_data.write(games)

#the parameter is games because eventually you will be displaying
#multiple games using this function
def display_games(games):
    print ("_"*43)
    print ("|{0:<20}|{1:<11}|{2:<13}|{3:<5}|{4:<17}|{5<20}|".format("Name", "Paltform", "Genre", "Cost", "Number of players", "Online functionality"))
    print ("_"*43)
    for line in games:
        print ("|{0:<20}|{1:<11}|{2:<13}|{3:<5}|{4:<17}|{5<20}|".format(line.name, line.paltform, line.genre, line.cost, line.number_of_players, line.online_functionality))
        print ("_"*43)
    
    

def get_game_from_user():
    #pdb.set_trace()
    games = []
    while game == -1:
        game_record = blank_game_record()
        name = input("Please enter the name of the game: ")
        if name == -1:
            game = -1
        else:
            platform = input("Please enter the platform of the game(e.g. XBox, PlayStation, PC etc.): ")
            genre = input("Please enter the genre of the game: ")
            cost = input("Please enter the cost of the game: £ ")
            number_of_players = int(input("Please enter the nunber of players in the game: "))
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

def main():
    exit_program = False
    while not exit_program:
        display_menu()
        selected_option = int(input("Please select a menu option: "))
        if selected_option == 1:
           games = get_game_from_user()
        elif selected_option == 2:
            display_games(games)
        elif selected_option == 3:
            filename = "game_databace.txt"
            save_games(filename, games)
            exit_prigram = True
        else:
            print("Please enter a valid option (1-3)")
            print()

if __name__ == "__main__":
    main()
