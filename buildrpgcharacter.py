full_dot = '●'
empty_dot = '○'

def create_character(name, strength, intelligence, charisma):
    if name != name.str():
        return("The character name should be a string")
    elif name = "":
        return("The character should hav a name")
    elif len(name) > 10:
        return("The character name is too long")
    elif len(name)