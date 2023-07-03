def roll_call_dwarves(dwarf_list):
    i = 1
    for dwarf in dwarf_list:
        print(f'{i}. {dwarf}')
        i += 1

def summon_captain_planet(planeteer_calls):
    planeteer_calls = [f'{call.title()}!' for call in planeteer_calls]
    return planeteer_calls

def long_planeteer_calls(calls):
    for call in calls:
        if len(call) > 4:
            return True
    return False

cheeses = ["cheddar", "gouda", "camembert"]

def find_the_cheese(items):
    for item in items:
        if item in cheeses:
            return item
    return None
