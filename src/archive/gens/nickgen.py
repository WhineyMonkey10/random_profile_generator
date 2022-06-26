def nickGen():
  import random
  ########## MAKING A LIST OF NICKNAMES #################
  nicknames = ["Kicker", "Gab", "FrayFray", "Burpy", "Nerdy", "Quintessential", "Kicker", "Gabitos", "Chrunou", "Michal", "Quickbot", "Hogefoot", "Bud"]
  randomnicknum = (random.randint(0, len(nicknames)) -1)
  nickname = (nicknames[randomnicknum])
  return nickname
  
  

  
