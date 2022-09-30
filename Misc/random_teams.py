import random

peeps = [
    "Richard",
    "Jake"
]

print("Winner: "+peeps[random.randint(0, len(peeps)-1)])
