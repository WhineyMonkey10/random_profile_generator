def ageGenerator():
  import random
  
  # Creating the random age
  probagenum = random.randint(1, 3)
  
  if probagenum == 1:
    age = random.randint(1, 99)
  else:
    if probagenum == 2:
      age = ("Unborn (Ignore years old)")
     else:
       age = ("Dead (Ignore years old)")
  
  return age
