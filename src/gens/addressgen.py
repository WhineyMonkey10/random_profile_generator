def addrGenerator():

  # Importing packages.
  import random

  # Define lists
  countrycode = [",U.S.A", ",E.U", ",C.A"]
  streetnames = ["Main Street", "Church Street", "Main Street North", "Main Street South", "Elm Street", "High Street", "Main Street West", "Washington Street", "Forster Close", "Alfred Street", "Allington Street", "Alma Road", "Somertrees Avenue", "Batson Street", "Bentinck Street", "George Street", "Benifician Avenue", "Hoge Lane"]

  # Assign each list their randomly generated number.
  housenum = [str(random.randint(1,2)), str(random.randint(1, 9))]

  streetnum = random.randint(1, len(streetnames) -1)

  countrycodenum = random.randint(1, len(countrycode) -1)

  # Take the randomly generated number(s), then assign them to variables attached to the lists.
  streetnames = (streetnames[streetnum])
  countrycode = (countrycode[countrycodenum])

  # Join all/the of the variables and list together.
  inthousenum = (''.join(housenum))
  finaladdr = (inthousenum + " " + streetnames + " " + countrycode)

  return finaladdr
