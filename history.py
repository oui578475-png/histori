
hero_name = input("Vad heter din hjälte? ")
hero_age = int(input("Hur gammal är hen? "))
gold = int(input("Hur många guldmynt har hen? "))
hero_strength = int(input("Hur stark är hen? (1-10): "))

hero_health = 10
has_sword = False
has_map = False

print("Det här är historien om", hero_name + ".")
print("Hen var", hero_age, "år gammal och redo för ett långt äventyr.")

hero_age = hero_age + 3
print("Tre år passerar under resans gång. Nu är", hero_name, hero_age, "år gammal.")

print(hero_name, "står vid kanten av en tät och mörk skog. En skylt varnar för vilddjur.")

choice1 = input("Vill du gå genom skogen eller ta omvägen runt? (skogen/omväg): ")

if choice1 == "skogen":
    print(hero_name, "stiger modigt in bland de mörka träden")

    if hero_strength >= 6:
        print("Ett vildsvin dyker upp! Men tack vare sin styrka skrämmer", hero_name, "bort det.")
    
    else:
        print("Ett vildsvin anfaller! Yngre och svagare tvingas", hero_name, "fly och tappar 2 hälsa.")
        hero_health = hero_health - 2

    print(hero_name, "hittar en gammal skattkarta på marken!")
    has_map = True
else:
    print(hero_name, "tar den säkra omvägen runt skogen. Det tar längre tid, men är säkert.")
