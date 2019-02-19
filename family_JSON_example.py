import json
import family_data

with open("data/family.json","r") as reader:
    family_json = json.load(reader)

print(family_json)


def make_family_from_json(json_data):
    # Initialize a new family
    new_family = family_data.Family()
    # Set the parents
    # Spelling important here!
    # We used parents as the name of the parent name array
    # To get that data from the json data we need to use those exact keys
    new_family.parents = json_data["parents"]
    # Loop through the kids_data and make a new Kid for each entry in the kids_data
    # Note: this is how to loop through data in python
    # One thing to note is "kid_data" is a variable that is declared as part of the loop
    for kid_json in json_data["kids"]:
        #  The loop steps through each element in the list (here the list is kids_data)
        #  and the variable kid_data represents the current element in the list
        # Make a new Kid
        kid = family_data.Kid(kid_json["name"], kid_json["age"])
        # Add the Kid to the new_family
        new_family.add_kid(kid)
        # We're done making and adding all the kids, so return the finished Family
    return new_family


make_family_from_json(family_json)

