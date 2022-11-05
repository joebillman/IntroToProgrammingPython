class Player:
    firstName = ""
    lastName = ""
    position = ""
    number = 00

    def getFullName():
        global firstName
        global lastName
        return f"{firstName} {lastName}"