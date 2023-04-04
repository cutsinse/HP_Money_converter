#Ex 21 Study Drills: Harry Potter Knuts

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
