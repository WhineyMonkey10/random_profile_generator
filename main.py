import random

middle_name = input("Do you want your name to include a middle name? (Yes or No?, Case sensitive). ")

if middle_name == ("Yes"):
  first_names = ["Tom", "Maya", "Jean", "Samerition", "Singual", "Bob", "Samantha", "Bart"]
  random_number = random.randint(0, len(first_names) - 1 )
  random_first_name = (''.join(first_names[random_number]))  

  middle_names = ["John", "Maxwell", "Kane", "Charles", "Louis", "Marley", "Drew", "Sam"]
  random_number_2 = random.randint(0, len(first_names) - 1 )
  random_middle_name = (''.join(middle_names[random_number_2]))

  last_names = last_names = ["Holland", "Dominic", "Samertons", "Simpson", "Zinkovic", "McDonald", "Sabet", "Vertez"]
  random_number_1 = random.randint(0, len(last_names) - 1 )
  random_last_name = (''.join(last_names[random_number_1]))

  final_name = (random_first_name + " " + random_middle_name + " "+ random_last_name)
  print(final_name)

else:
  first_names = ["Tom", "Maya", "Jean", "Samerition", "Singual", "Bob", "Samantha", "Bart"]
  random_number = random.randint(0, len(first_names) - 1 )
  random_first_name = (''.join(first_names[random_number]))  
  last_names = last_names = ["Holland", "Dominic", "Samertons", "Simpson", "Zinkovic", "McDonald", "Sabet", "Vertez"]
  random_number_1 = random.randint(0, len(last_names) - 1 )
  random_last_name = (''.join(last_names[random_number_1]))

  final_name = (random_first_name + " " + random_last_name)
  print(final_name)
