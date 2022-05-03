import random
def namegen(arrayd: list):
  randnum = random.randint(0,len(arrayd) - 1)
  return arrayd[randnum]
  