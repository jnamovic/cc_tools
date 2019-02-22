import cc_dat_utils

#Part 3
#Load your custom JSON file
#Convert JSON data to cc_data
#Save converted data to DAT file

import cc_data
import json

#Creates and returns a GameLibrary object(defined in test_data) from loaded json_data
def make_levels_from_json( json_data ):
    #Initialize a new GameLibrary
    data_file = cc_data.CCDataFile();
    for level in json_data:
        new_level = cc_data.CCLevel();
        new_level.level_number = level["level_num"]
        new_level.time = level["time"]
        new_level.num_chips = level["chip_num"]
        new_level.upper_layer = level["upper_layer"]
        lower=[]
        step=1024
        while(step>0):
            lower.append(0)
            step-=1;
        new_level.lower_layer=lower;

        for option in level["optional_layers"]:
            id=option["id"]
            if(id==3):
                result = cc_data.CCMapTitleField(option["title"])
            if (id == 6):
                result = cc_data.CCEncodedPasswordField(option["pass"])
            if (id == 7):
                result = cc_data.CCMapHintField(option["hint"])
            if(id==10):
                monsterList=[]

                for monster in option["coord"]:

                    monsterList.append(cc_data.CCCoordinate(monster[0], monster[1]))
                result = cc_data.CCMonsterMovementField(monsterList)
            new_level.optional_fields.append(result)

        data_file.add_level(new_level);

    return data_file


input_json_file = "data/level_data.json"


with open(input_json_file, "r") as reader:
    game_json = json.load(reader)
    dat_file = make_levels_from_json(game_json)
    cc_dat_utils.write_cc_data_to_dat(dat_file, "data/pfgd_test.dat")
    print(dat_file)

