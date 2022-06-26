import random
import genlib
def allergiesGen():
  list_of_allergies = ["peanuts", "chickpeas", "cats", "horses", "bees", "wasps", "peas", "lupins", "potatoes", "tomatoes", "glutin", "lactose", "cheese", "dust", "hay feaver", "chickens", "ducks", "cows", "crabs", "shrimp", "apples", "oranges", "bananas", "kiwis", "dogs"]


  random_allergienum = random.randint(0, len(list_of_allergies))
   

  if random_allergienum == 15:
   allergie = ("Your allergy is hay fever")


  else:
    allergie1 = (''.join(genlib.namegen(list_of_allergies)))

    allergie = (f"You are allergic to {allergie1}")


  return allergie