print("Today we will build a cleaning robot together. 🤖")


room = ["D", "C", "D", "D", "C"]
def show_room(room):
    picture = ""
    for spot in room:
        if spot == "D":
            picture += " 🤢 "
        else:
            picture += " 👌 "
    print(picture)

print("Our room right now:")
show_room(room)


def clean_spot(spot):
    if spot == "D":
        return "C"
    else:
        return "C"


cleaned_spot_result = clean_spot("D")
print("The robot looked at a dirty spot 🤢 and made it:", cleaned_spot_result,
      "(C means clean ✨)")

print("BEFORE - the dirty room:")
show_room(room)


for i in range(len(room)):
    room[i] = clean_spot(room[i])
    print("After cleaning spot number", i + 1, ":")
    show_room(room)

print()
print("AFTER - all done! ✨🤖")