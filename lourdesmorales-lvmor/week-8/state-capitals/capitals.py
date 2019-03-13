# an array of state dictionaries

import random

states = [
    {"name": "Alabama", "capital": "Montgomery"},
    {"name": "Alaska", "capital": "Juneau"},
    {"name": "Arizona", "capital": "Phoenix"},
    {"name": "Arkansas", "capital": "Little Rock"},
    {"name": "California", "capital": "Sacramento"},
    {"name": "Colorado", "capital": "Denver"},
    {"name": "Connecticut", "capital": "Hartford"},
    {"name": "Delaware", "capital": "Dover"},
    {"name": "Florida", "capital": "Tallahassee"},
    {"name": "Georgia", "capital": "Atlanta"},
    {"name": "Hawaii", "capital": "Honolulu"},
    {"name": "Idaho", "capital": "Boise"},
    {"name": "Illinois", "capital": "Springfield"},
    {"name": "Indiana", "capital": "Indianapolis"},
    {"name": "Iowa", "capital": "Des Moines"},
    {"name": "Kansas", "capital": "Topeka"},
    {"name": "Kentucky", "capital": "Frankfort"},
    {"name": "Louisiana", "capital": "Baton Rouge"},
    {"name": "Maine", "capital": "Augusta"},
    {"name": "Maryland", "capital": "Annapolis"},
    {"name": "Massachusetts", "capital": "Boston"},
    {"name": "Michigan", "capital": "Lansing"},
    {"name": "Minnesota", "capital": "St. Paul"},
    {"name": "Mississippi", "capital": "Jackson"},
    {"name": "Missouri", "capital": "Jefferson City"},
    {"name": "Montana", "capital": "Helena"},
    {"name": "Nebraska", "capital": "Lincoln"},
    {"name": "Nevada", "capital": "Carson City"},
    {"name": "New Hampshire", "capital": "Concord"},
    {"name": "New Jersey", "capital": "Trenton"},
    {"name": "New Mexico", "capital": "Santa Fe"},
    {"name": "New York", "capital": "Albany"},
    {"name": "North Carolina", "capital": "Raleigh"},
    {"name": "North Dakota", "capital": "Bismarck"},
    {"name": "Ohio", "capital": "Columbus"},
    {"name": "Oklahoma", "capital": "Oklahoma City"},
    {"name": "Oregon", "capital": "Salem"},
    {"name": "Pennsylvania", "capital": "Harrisburg"},
    {"name": "Rhode Island", "capital": "Providence"},
    {"name": "South Carolina", "capital": "Columbia"},
    {"name": "South Dakota", "capital": "Pierre"},
    {"name": "Tennessee", "capital": "Nashville"},
    {"name": "Texas", "capital": "Austin"},
    {"name": "Utah", "capital": "Salt Lake City"},
    {"name": "Vermont", "capital": "Montpelier"},
    {"name": "Virginia", "capital": "Richmond"},
    {"name": "Washington", "capital": "Olympia"},
    {"name": "West Virginia", "capital": "Charleston"},
    {"name": "Wisconsin", "capital": "Madison"},
    {"name": "Wyoming", "capital": "Cheyenne"},
]

for dictionary in states:
    dictionary["correct"] = 0
    dictionary["wrong"] = 0


def play_game():
    welcome_message = "Welcome to the 50 states game!"
    print(welcome_message)
    is_game_over = False
    while is_game_over == False:
        random.shuffle(states)
        for dictionary in states:
            print("What is the capital of " + dictionary.get("name") + "?")
            guess = input("Enter guess: ")
            if guess.upper() == dictionary.get("capital").upper():
                print("Yay! Your answer is correct")
                # dictionary["correct"] = dictionary["correct"] + 1
                dictionary["correct"] += 1
            else:
                print("Incorrect response")
                dictionary["wrong"] += 1
            print(
                "You answered "
                + str(dictionary.get("correct"))
                + " out of "
                + str(dictionary.get("correct") + dictionary.get("wrong"))
                + " for "
                + dictionary.get("name")
            )
        response = input("Do you want to play again? ")
        if response.upper() != "YES":
            is_game_over = True


play_game()
