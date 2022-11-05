class Team:
    name = ""
    members = []
    location = ""
    sport = ""

    def getMemberByName(self, name):
        memberFound = False
        for curName in self.members:
            if(curName == name):
                memberFound = True
                break

        if(memberFound):
            print(f"{name} was found on this team.")
        else:
            print(f"{name} was NOT found on this team.")

    def getTotalMemberCount(self):
        return len(self.members)

class Player:
    firstName = ""
    lastName = ""
    position = ""
    number = 00

    def getFullName(self):
        return f"{self.firstName} {self.lastName}"
