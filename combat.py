
def take_damage(health, damage):
    return max(0, health - damage)


def fight_boar(strength, weapon):

    total_strength = strength + weapon

    if total_strength >= 6:
        return True, 0

    return False, 2

