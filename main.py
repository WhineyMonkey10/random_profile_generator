############### - Imports - ###############

from agegen import *

from namegen import *

from addressgen import *

import time


############### - Def Calls - ###############

# Defining the persons name
name = nameGenerator()

# Defining the persons age
age = ageGenerator()

# Defining the persons adddress
addr = addrGenerator()

# Priting the above in a sentence & Adding a disclaimer
print("DISCLAIMER: None of these credentials, addresses, names, ages or others are meant to replicate a person's actual personal credentials.")

# Adding time for the user to read the disclaimer
time.sleep(1)

# Actually printing the final product
print("Your name is:", name, ", you live in", addr, ", and you are:", age, "years old!")



