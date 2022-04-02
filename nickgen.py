def nickGen():
  import random
  ########## MAKING A LIST OF NICKNAMES #################
  nicknames = ["Kicker", "Gab", "FrayFray", "Burpy", "Nerdy", "Quintessential", "Kicker", "Gabitos", "Chrunou", "Michal", "Mr.Fries", "Quickbot", "Bud", "HogeFoot"]
  randomnicknum = (random.randint(1, len(nicknames)))
  print (randomnicknum)
  nickname = (nicknames[randomnicknum])
  return nickname
  
  

  
