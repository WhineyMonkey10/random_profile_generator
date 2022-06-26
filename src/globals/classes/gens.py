class Gens:
    """
    Generator Class
    """
    import random
    import genlib
    import colorama

    def __init__(self):
        pass

    def addrGenerator(self):

        countrycode = [",U.S.A", ",E.U", ",C.A"]
        streetnames = ["Main Street", "Church Street", "Main Street North", "Main Street South", "Elm Street",
                       "High Street", "Main Street West", "Washington Street", "Forster Close", "Alfred Street",
                       "Allington Street", "Alma Road", "Somertrees Avenue", "Batson Street", "Bentinck Street",
                       "George Street", "Benifician Avenue", "Hoge Lane"]

        # Assign each list their randomly generated number.
        housenum = [str(self.random.randint(1, 2)), str(self.random.randint(1, 9))]

        streetnum = self.random.randint(1, len(streetnames) - 1)

        countrycodenum = self.random.randint(1, len(countrycode) - 1)

        # Take the randomly generated number(s), then assign them to variables attached to the lists.
        streetnames = (streetnames[streetnum])
        countrycode = (countrycode[countrycodenum])

        # Join all/the of the variables and list together.
        inthousenum = (''.join(housenum))
        finaladdr = (inthousenum + " " + streetnames + " " + countrycode)

        return finaladdr

    def ageGenerator(self):

        # Creating the random age
        probagenum = self.random.randint(1, 10)

        age = "null"

        if probagenum == 1 or 3 or 4 or 6 or 7 or 8 or 9 or 10:
            age = self.random.randint(1, 99)
        else:
            if probagenum == 2:
                age = ("Unborn (Ignore years old)")
            else:
                if probagenum == 5:
                    age = ("Dead (Ignore years old)")

        return age

    def allergiesGen(self):
        list_of_allergies = ["peanuts", "chickpeas", "cats", "horses", "bees", "wasps", "peas", "lupins", "potatoes",
                             "tomatoes", "glutin", "lactose", "cheese", "dust", "chickens", "ducks",
                             "cows", "crabs", "shrimp", "apples", "oranges", "bananas", "kiwis", "dogs"]

        random_allergienum = self.random.randint(0, len(list_of_allergies))

        if random_allergienum == 15:
            allergie = ("Your allergy is hay fever")
        else:
            allergie1 = (''.join(self.genlib.namegen(list_of_allergies)))
            allergie = (f"You are allergic to {allergie1}")

        return allergie

    def your_best_friend(self):

        list_of_names = ["Tom", "Maya", "Jean", "Samerition", "Singual", "Bob", "Samantha", "Bart", "Stan", "Cobra",
                         "John", "Maxwell", "Kane", "Charles", "Louis", "Marley", "Drew", "Sam", "Stanley", "Kai",
                         "Holland", "Dominic", "Samertons", "Simpson", "Zinkovic", "McDonald", "Sabet", "Vertez",
                         "Lee", ]

        random_friendnum = self.random.randint(0, 29)
        list_of_names1 = ((list_of_names[random_friendnum]))
        list_of_names = (f"{list_of_names1}")

        return list_of_names

    def borngen(self):

        list_of_places = ["England", "Scotland", "Ireland", "Whales", "France", "Germany", "Netherlands", "Belgium",
                          "Afghanistan", "	Albania", "	Algeria", "	Andorra", "Angola", "Antigua", "Barbuda",
                          "Argentina", "Armenia", "Australia", "Austria", "	Azerbaijan"]

        random_bornnum = self.random.randint(0, len(list_of_places) - 1)
        list_of_places1 = (''.join((list_of_places[random_bornnum])))
        list_of_places = (list_of_places1)

        return list_of_places

    def eyecolourgen(self):

        list_of_colours = ["Blue", "Green", "Brown", "Red", "Purple", "Black"]

        random_eyecolournum = self.random.randint(0, len(list_of_colours) - 1)
        list_of_colours1 = (''.join((list_of_colours[random_eyecolournum])))
        list_of_colours = (list_of_colours1)

        return list_of_colours

    def familyGenerator(self):
        # Asking for the amount of family members
        abro = input("Do you want to have a brother(s) (Yes or No, case sensitve)")
        asis = input("Do you want to have a sister(s) (Yes or No, case sensitve)")
        aaunt = input("Do you want to have an aunt(s) (Yes or No, case sensitve)")
        aunc = input("Do you want to have an uncle(s) (Yes or No, case sensitve)")
        apet = input("Do you want to have a pet(s) (Yes or No, case sensitve)")

        # Generating the amount of family member(s)
        if abro == ("Yes"):
            ambro = self.random.randint(1, 5)
            abros = self.random.randint(1, ambro)
        else:
            abros = ("0")

        if asis == ("Yes"):
            amsis = self.random.randint(1, 5)
            asiss = self.random.randint(1, amsis)
        else:
            asiss = ("0")

        if aaunt == ("Yes"):
            amaunt = self.random.randint(1, 3)
            aaunts = self.random.randint(1, amaunt)
        else:
            aaunts = ("0")

        if aunc == ("Yes"):
            amauncs = self.random.randint(1, 3)
            auncs = self.random.randint(1, amauncs)
        else:
            auncs = ("0")

        if apet == ("Yes"):
            ampets = self.random.randint(1, 4)
            apets = self.random.randint(1, ampets)
        else:
            apets = ("0")

        # Adding all of these values together

        final = (
            "You have ", abros, "brother(s), and", asiss, "sister(s). You also have ", aaunts, "aunt(s) and ", auncs,
            "uncle(s). Ontop of all of that, you have ", apets, "pet(s)!!")

        return final

    def favouritefood(self):
        favfood = ["apples", "bananas", "oranges", "peanuts", "chickpeas", "peas", "potatoes", "tomatoes", "cheese",
                   "shrimp", "kiwis", "rice", "fish", "sushi", "pizza", "chips", "fries", "pancakes", "waffles"]

        random_foodnum = self.random.randint(0, len(favfood) - 1)
        favfood1 = (''.join((favfood[random_foodnum])))
        favfood = (f"Your favourite food are: {favfood1}")

        return favfood

    def nameGenerator(self, include_middle_name: str = "No"):

        first_names = ["Tom", "Maya", "Jean", "Samerition", "Singual", "Bob", "Samantha", "Bart", "Stan", "Cobra",
                       "Johnathon", "Jhon"]
        middle_names = ["John", "Maxwell", "Kane", "Charles", "Louis", "Marley", "Drew", "Sam", "Stanley", "Kai"]
        last_names = ["Holland", "Dominic", "Samertons", "Simpson", "Zinkovic", "McDonald", "Sabet", "Vertez", "Lee",
                      "Never-Dies"]

        middle_name_q = include_middle_name
        middle_name_q = (middle_name_q.casefold())

        # Randomly Pick First Name
        random_number = self.random.randint(0, len(first_names) - 1)
        random_first_name = (''.join(first_names[random_number]))

        # Randomly pick a last name
        random_number_1 = self.random.randint(0, len(last_names) - 1)
        random_last_name = (''.join(last_names[random_number_1]))

        final_name = "null"

        if middle_name_q == ("yes"):
            # Randomly Pick Middle Name
            random_number_2 = self.random.randint(0, len(middle_names) - 1)

            random_middle_name = (''.join(middle_names[random_number_2]))

            # Name addition
            final_name = (random_first_name + " " + random_middle_name + " " + random_last_name)

        if middle_name_q == ("no"):
            final_name = (random_first_name + " " + random_last_name)

        return final_name

    def nickGen(self):
        ########## MAKING A LIST OF NICKNAMES #################
        nicknames = ["Kicker", "Gab", "FrayFray", "Burpy", "Nerdy", "Quintessential", "Kicker", "Gabitos", "Chrunou",
                     "Michal", "Quickbot", "Hogefoot", "Bud"]
        randomnicknum = (self.random.randint(0, len(nicknames)) - 1)
        nickname = (nicknames[randomnicknum])
        return nickname
