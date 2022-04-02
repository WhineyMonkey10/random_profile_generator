def ageGenerator():
  import random
  
  # Creating the random age
  probagenum = random.randint(1, 2)
  
  if probagenum == 1:
    age = random.randint(1, 99)
  else:
    age = ("Unborn")
  
  return age
