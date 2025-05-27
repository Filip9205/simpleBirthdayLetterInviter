
with open("./Input/Names/invited_names.txt", mode="r") as names:
    guests = names.readlines()

with open("./Input/Letters/starting_letter.txt", mode="r") as le:
    letter = le.read()

for guest in guests:
    new_guest = guest.strip()
    with open(f"./Output/ReadyToSend/{new_guest}.txt", mode="a") as file:
        file.write(letter.replace("[name]", new_guest))
