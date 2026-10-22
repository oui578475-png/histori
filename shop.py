
def buy_item(gold, price):
    if gold >= price:
        return gold - price, True

    return gold, False


def buy_sword(player):
    if player["has_sword"]:
        return False, "Du har redan ett svärd."

    new_gold, success = buy_item(player["gold"], 8)

