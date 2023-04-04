#From Exercise 21: Converting USD to Harry Potter Money

USD = float(input("How much money do you have in US dollars? \n"))

Just_Knuts = round(USD * 67.049)

print(f"Ok, so if you only have knuts, you have {Just_Knuts} knuts.  That's nuts!")

Galleons = Just_Knuts // 493
Kn_minus_Gal = Just_Knuts % 493

#the command divmod(a,b) can do both.  in this case, it would be divmod(Just_Knuts, 493) to return both values.
#However, I'm not sure at this point how to seperate the values back out into their own variables to use them later

print(f"So that means you have {Galleons} Galleons with {Kn_minus_Gal} knuts left over.")
print("But wait, we forgot about Sickles!")

Sickles = Kn_minus_Gal // 17
Kn_final = Kn_minus_Gal % 17

print(f"So that means {USD}$ is about {Galleons} Galleons, {Sickles} Sickles, and {Kn_final} Knuts. ")
