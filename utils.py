def getElement(text):
    compteur_deux_points = 0
    compteur = 1

    for i in text:
        if i == ":":
            compteur_deux_points += 1

        if compteur_deux_points == 2:
            return (text[:compteur], text[compteur:])

        compteur += 1

    return "", ""

def getName(text):
    result = ""
    testeur = False

    for i in text:
        if i == ":":
            testeur = not testeur

        elif i == "!":
            return result[1:]

        if testeur:
            result += i

    return ""

def preFormattage(user_and_message):
    if getName(user_and_message[0]) == "":
        return user_and_message[1]
    else:
        return f"[{getName(user_and_message[0])}]: {user_and_message[1]}"

def formattage(text):
    temp = ""
    result = ""

    for i in range(len(text)):
        if text[i] == "\n" or (i == (len(text) - 1)):
            result += f"{preFormattage(getElement(temp))}\n"
            temp = ""

        temp += text[i]

    return result