import random
def borngen():
  list_of_places = ["England","Scotland", "Ireland", "Whales", "France", "Germany", "Netherlands", "Belgium","Afghanistan","	Albania", "	Algeria", "	Andorra", "Angola", "Antigua", "Barbuda", "Argentina", "Armenia", "Australia", "Austria", "	Azerbaijan"]

  random_bornnum = random.randint(0 ,len(list_of_places) -1)
  

  list_of_places1 = (''.join((list_of_places[random_bornnum])))

  list_of_places = (list_of_places1)


  return list_of_places
