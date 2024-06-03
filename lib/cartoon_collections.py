def roll_call_dwarves(names):
    # for i in range(1, len(names)):
        i = 1
        for name in names:
            # print (str(i) + ". ", name)
            print(f"{i}. {name}")
            i += 1

def summon_captain_planet(calls):
    result = []
    for call in calls:
        new_word = call.capitalize() + "!"
        result.append(new_word)
        print(new_word)
    return result

def long_planeteer_calls(words):
    for word in words:
        if len(word) > 4:
            return True   
    return False
        
def find_the_cheese(cheeses):
    for cheese in cheeses:
        CHEESES = ["camembert", "gouda", "cheddar"]
        if cheese in CHEESES:
            return cheese
    return None