def ageGenerator():
  import random
  
  # Creating the random age
  probagenum = random.randint(1, 10)
  
  if probagenum == 1 or 3 or 4 or 6 or 7 or 8 or 9 or 10:
    age = random.randint(1, 99)
  else:
    if probagenum == 2:
      age = ("Unborn (Ignore years old)")
    else:
      if probagenum == 5:
        age = ("Dead (Ignore years old)")
  
  return age
