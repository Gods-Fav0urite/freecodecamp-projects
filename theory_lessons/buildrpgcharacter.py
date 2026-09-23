full_dot = '●'
empty_dot = '○'

def create_character(name, str_strength, int_intelligence, cha_charisma):

    if type(name) is not str:
        return "The character name should be a string"

    if name == "":
        return "The character should have a name"

    if len(name) > 10:
        return "The character name is too long"

    if " " in name:
        return "The character name should not contain spaces"

    stats = [str_strength, int_intelligence, cha_charisma]
    if any(type(stat) is not int for stat in stats):
        return "All stats should be integers"
    
    if any(stat < 1 for stat in stats):
        return "All stats should be no less than 1"
    
    if any(stat > 4 for stat in stats):
        return "All stats should be no more than 4"

    if sum(stats) != 7:
        return "The character should start with 7 points"

    str_full = full_dot * str_strength + empty_dot * (10 - str_strength)
    int_full = full_dot * int_intelligence + empty_dot * (10 - int_intelligence)
    char_full = full_dot * cha_charisma + empty_dot * (10 - cha_charisma)

    return f"{name}\nSTR {str_full}\nINT {int_full}\nCHA {char_full}"

print(create_character('ren', 4, 2, 1))