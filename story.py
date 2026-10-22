
def forest_result(player):
    if player["styrka"] >= 6:
        text = (
            "Ett vildsvin dyker upp! "
            "Tack vare din styrka skrämmer du bort det."
        )
    else:
        player["health"] -= 2
        text = (
            "Ett vildsvin anfaller! "
            "Du flyr och förlorar 2 hälsa."
        )

    player["har_map"] = True
