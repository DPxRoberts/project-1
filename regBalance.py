#This is a basic register balancing program/app

coins = {
	"q":0, 
	"d":0, 
	"n":0, 
	"p":0
}

rolledCoins = {
	"rQ":0, 
	"rD":0, 
	"rN":0, 
	"rP":0
}

bills = {
	"ones":0, 
	"fives":0, 
	"tens":0, 
	"twenties":0, 
	"fifties":0, 
	"hundreds":0
}


coinsTotal = 0
rolledTotal = 0
billsTotal = 0
total = 0

# def coinCalc

#lose coins
print("""
First the Lose Coins: 
 """)
coins["q"] = int(input("How many Quarters are there? "))
qTotal = coins["q"] * 0.25 
print(float(qTotal))

coins["d"] = int(input("How many Dimes are there? "))
dTotal = coins["d"] * 0.10
print(float(dTotal))

coins["n"] = int(input("How many Nickles are there? "))
nTotal = coins["n"] * 0.05
print(float(nTotal))

coins["p"] = int(input("How many Pennies are there? "))
pTotal = coins["p"] * 0.01
print(float(pTotal))

coinsTotal = qTotal + dTotal + nTotal + pTotal
print("Your total amount in lose coins is $", coinsTotal)

# rolled coins
print("")
print("Next will be the Rolled Coins: ")
rolledCoins["rQ"] = int(input("How many  Rolls of Quarters are there? "))
rqTotal = rolledCoins["rQ"] * 10.0
print(float(rqTotal))

rolledCoins["rD"] = int(input("How many Rolls of Dimes are there? "))
rdTotal = rolledCoins["rD"] * 5.0
print(float(rdTotal))

rolledCoins["rN"] = int(input("How many Rolls of Nickles are there? "))
rnTotal = rolledCoins["rN"] * 2.0
print(float(rnTotal))

rolledCoins["rP"] = int(input("How many rolls of Pennies are there? "))
rpTotal = rolledCoins["rP"] * 0.5
print(float(rpTotal))

rolledTotal = rqTotal + rdTotal + rnTotal + rpTotal
print("Your total amount in rolls is $", rolledTotal)

#bills 

print("""
Last we will count the Bills: 
 """)
bills["ones"] = int(input("How many $1s are there? "))
onesTotal = bills["ones"] * 1.0
print(float(onesTotal))

bills["fives"] = int(input("How many $5s are there? "))
fivesTotal = bills["fives"] * 5.0
print(float(fivesTotal))

bills["tens"] = int(input("How many $10s are there? "))
tensTotal = bills["tens"] * 10.0
print(float(tensTotal))

bills["twenties"] = int(input("How many $20s are there? "))
twentyTotal = bills["twenties"] * 20.0
print(float(twentyTotal))

bills["fifties"] = int(input("How many $50s are there? "))
fiftiesTotal = bills["fifties"] * 50.0
print(float(fiftiesTotal))

bills["hundreds"] = int(input("How many $100s are there? "))
hundredsTotal = bills["hundreds"] * 100.0
print(float(hundredsTotal))

billsTotal = onesTotal + fivesTotal + tensTotal + twentyTotal + fiftiesTotal + hundredsTotal
print("Your total amount in cash is $", billsTotal)

total = coinsTotal + rolledTotal + billsTotal

print("")
print("Your grand total for this drawer is. $", total)
