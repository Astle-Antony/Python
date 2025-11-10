# # Functions with input
#
# def greet_with_name(name: str, location: str) -> None:
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
#     print(f"what is it like in {location}")
#
#
# greet_with_name("Astle", "Zoho")
#
#
# # Positional Arguments
# greet_with_name("Zoho", "Astle")
# # now it doesn't make sense right? To overcome this
#
# # Key Arguments
# greet_with_name(location='Zoho',name ="Astle")
#
# hello = 1
# my = 2
#
# print (f"{hello}{my}")


def calculate_love_score(name1, name2):
    TRUE = 0
    LOVE = 0

    full_name = name1 + name2
    for i in full_name:
        if(i == "T" or i == "t"or i == "R" or i == "r"or i == "U" or i == "u"or i == "E"or i == "e"):
            TRUE += 1

    for i in full_name:
        if(i == "L" or i == "l" or i == "O" or i == "o"or i == "V" or i == "v"or i == "E"or i == "e"):
            LOVE += 1
    print(f"Love Score = {TRUE}{LOVE}")


calculate_love_score("Kanye West", "Kim Kardashian")