import random
def eyecolourgen():
  list_of_colours = ["Blue", "Green", "Brown", "Red", "Purple", "Black"]

  random_eyecolournum = random.randint (0, len(list_of_colours) - 1)

  list_of_colours1 = (''.join((list_of_colours[random_eyecolournum])))

  list_of_colours = (list_of_colours1)

  return list_of_colours