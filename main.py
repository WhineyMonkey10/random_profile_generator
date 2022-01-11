import random



first_names = ["Jakob", "Oded", "Fraser", "Gabriel", "Adrien", "Bob", "Martin", "Bart"]
random_number = random.randint(0, len(first_names) - 1 )
random_first_name = (''.join(first_names[random_number]))  


last_names = ["Mandel", "Dominic", "Samertons", "Simpson", "Nerd", "McDonald", "Pyjamas", "Pasta"]
random_number_1 = random.randint(0, len(last_names) - 1 )
random_last_name = (''.join(last_names[random_number_1]))

final_name = (random_first_name + " " + random_last_name)
print(final_name)
