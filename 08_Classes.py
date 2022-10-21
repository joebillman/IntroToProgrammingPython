from unicodedata import name
import Team

teamA = Team.Team()
teamB = Team.Team()

teamA.name = "49ers"
teamB.name = "Giants"

teamA.members.append("Joe Montana")
teamA.members.append("Jerry Rice")
teamA.members.append("Ronnie Lott")

teamB.members.append("Joey Bart")
teamB.members.append("Lewis Brinson")

teamA.getMemberByName("Joe Montana")
print(f"The total member count for Team A is: {teamA.getTotalMemberCount()}")
