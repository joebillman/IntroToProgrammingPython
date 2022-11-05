import Classes

# Create two teams
teamA = Classes.Team()
teamA.name = "SF 49ers"
teamA.location = "San Francisco"
teamA.sport = "Football"

teamB = Classes.Team()
teamB.name = "SF Giants"
teamB.location = "San Francisco"
teamB.sport = "Baseball"

# Create players for Team A
playerA = Classes.Player()
playerA.firstName = "Jimmy"
playerA.lastName = "Garoppolo"
playerA.number = 10
playerA.position = "Quarterback"

playerB = Classes.Player()
playerB.firstName = "Deebo"
playerB.lastName = "Samuel"
playerB.number = 19
playerB.position = "Wide Receiver"

teamA.members.append(playerA.getFullName())
teamA.members.append(playerB.getFullName())

playerList = [playerA, playerB]
for player in playerList:
    print(player.firstName)

# Print players on Team A
print("Players on Team A:")
for player in teamA.members:
    print(player)

# Create players for Team B
teamB.members.append("Joey Bart")
teamB.members.append("Lewis Brinson")

# See if Joe Montana is on Team A
print("Is Joe Montana on Team A?")
teamA.getMemberByName("Joe Montana")
print("Is Jimmy Garoppolo on Team A?")
teamA.getMemberByName("Jimmy Garoppolo")

# Print the total numbers of players on Team A
print("How many players are on Team A?")
print(f"The total member count for Team A is: {teamA.getTotalMemberCount()}")
