def familyGenerator():
    import random

    # Asking for the amount of family members
    abro = input("Do you want to have a brother(s) (Yes or No, case sensitve)")
    asis = input("Do you want to have a sister(s) (Yes or No, case sensitve)")
    aaunt = input("Do you want to have an aunt(s) (Yes or No, case sensitve)")
    aunc = input("Do you want to have an uncle(s) (Yes or No, case sensitve)")
    apet = input("Do you want to have a pet(s) (Yes or No, case sensitve)")

    # Generating the amount of family member(s)
    if abro == ("Yes"):
        ambro = random.randit(1, 5)
        abros = random.randint(1, ambro)

    else:
      abros = ("0")

    if asis == ("Yes"):
        amsis = random.randint(1, 5)
        asiss = random.randint(1, amsis)

    else:
      asiss = ("0")

    if aaunt == ("Yes"):
        amaunt = random.randint(1, 3)
        aaunts = random.randint(1, amaunt)

    else:
      aaunts = ("0")

    if aunc == ("Yes"):
        amauncs = random.randint(1, 3)
        auncs = random.randint(1, amauncs)
    
    else:
      auncs = ("0")

    if apet == ("Yes"):
        ampets = random.randint(1, 4)
        apets = random.randint(1, ampets)

    else: 
        apets = ("0")

    # Adding all of these values together

    final = ("You have ", abros, "brother(s), and", asiss, "sister(s). You also have ", aaunts, "aunt(s) and ", auncs, "uncle(s). Ontop of all of that, you have ", apets, "pet(s)!!")
    return final
