#Harry Potter Money: Update after learning if statements

print("""Enter 1 or 2 to choose what to convert:
1: USD to Harry Potter money
2: Harry Potter money to USD""")
user_choice = input(">")

if "1" in user_choice:
    USD = float(input("How much money do you have in US dollars? \n"))

    Just_Knuts = round(USD * 67.049)

    print(f"Ok, so if you only have knuts, you have {Just_Knuts} knuts.  That's nuts!")

    Galleons = Just_Knuts // 493
    Kn_minus_Gal = Just_Knuts % 493

    print(f"So that means you have {Galleons} Galleons with {Kn_minus_Gal} knuts left over.")
    print("But wait, we forgot about Sickles!")

    Sickles = Kn_minus_Gal // 17
    Kn_final = Kn_minus_Gal % 17

    print(f"So that means {USD}$ is about {Galleons} Galleons, {Sickles} Sickles, and {Kn_final} Knuts. ")

elif "2" in user_choice:
    def Gal_to_Kn(g):
        print("Converting Galleons to Knuts....")
        return g * 493

    def Sick_to_Kn(s):
        print("Converting Sickles to Knuts....")
        return s * 29

    def Kn_to_USD(k):
        print("Converting to USD....")
        return k / 67.05

    G_Knuts = Gal_to_Kn(int(input("How many Galleons do you have? \n >")))
    S_Knuts = Sick_to_Kn(int(input("How many Sickles do you have? \n >")))
    Just_Knuts = int(input("How many Knuts do you have? \n >"))
    Total_Knuts = G_Knuts + S_Knuts + Just_Knuts
    Total_USD = Kn_to_USD(Total_Knuts)

    print(f"So, you have {Total_Knuts} Knuts.\n Wow! That's a lot of knuts!")
    print(f"So that means you have about {Total_USD: .2f} USD in the muggle world.")
else:
    print("Not valid, program will now shut down, please try again")

print("Thanks for playing!")
