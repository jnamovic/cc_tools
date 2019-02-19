import test_data
import json

#Creates and returns a GameLibrary object(defined in test_data) from loaded json_data
def make_game_library_from_json( json_data ):
    #Initialize a new GameLibrary
    game_library = test_data.GameLibrary()

    ### Begin Add Code Here ###
    for game in json_data:
        plat = test_data.Platform(game["platform"]["name"] , game["platform"]["launch_year"])
        new_game = test_data.Game(game["title"], plat, game["year"])
        game_library.add_game(new_game)

    ### End Add Code Here ###

    return game_library


#Part 2
input_json_file = "data/test_data.json"

### Begin Add Code Here ###
with open(input_json_file,"r") as reader:
    game_json = json.load(reader)
    library = make_game_library_from_json(game_json)
    print(library)

### End Add Code Here ###

