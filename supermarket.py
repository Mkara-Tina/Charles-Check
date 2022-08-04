'''
MKARA NATIVIDAD
149911
I did the work alone through research from the internet.
'''

# import random module for returning a random float
# import random.choice to return a randomly selected element from a specified sequence
import random
from secrets import choice
import sys

# defining variables : unit price of an individual lottery ticket, bread, milk and soda
ticket = int(200)
bread = int(95)
milk = int(75)
soda = int(60)

# defining initial money user has and how much has been spent
totalMoney = int(400)
totalMoneySpent = 0

# variable defining amounts purchased for lottery ticket, bread, milk, soda and money won. Initial is all Zero.
amtTicket = 0
amtBread = 0
amtMilk = 0
amtSoda = 0
wonAmount = 0

# source file for printing output in a text file
sourceFile = open('demo.txt', 'w')

# ask user their name and print a welcome message
customerName = input("Please enter your name: ")

# welcome message for the customer to a supermarket called Chakara.
print("Welcome", customerName,
      "!, to Chakara Supermarket.\nWe sell bread @ 95ksh, milk @ 70Ksh,soda @ 60Ksh and lottery tickets @ 200Ksh each", file=sourceFile)


# inform user how much cash they have and inquire if they want to buy a lottery ticket.
print("You have 400Ksh.", file=sourceFile)


ticketPurchase = input(
    "would you like to buy a lottery ticket? (Y for Yes and N for No): ")

# message to customer if no ticket is purchased
if ticketPurchase.lower() != "y":
    print("No lottery tickets were purchased", file=sourceFile)

# deduct ticket purchase cash from total shopping money and adds number of tickets by 1
# system randomly selects a number, the winning number is 2
else:
    totalMoney = totalMoney-ticket
    amtTicket = +1
    print("Great! You stand a chance to win a lottery through random selection", file=sourceFile)
    rand = random.choice([0, 1, 2])
    print("random number selected is: " + str(rand), file=sourceFile)

    # system randomly selects a number between 2 and 10
    # each winning is placed at 100Ksh, hence winning number is multiplied by 100
    if rand == 2:
        print("You are our lucky winner", file=sourceFile)
        winnings = random.randint(2, 10)
        wonAmount = winnings * 100
        print("WonAmount: " + str(wonAmount), file=sourceFile)
        totalMoney = totalMoney+wonAmount

        # prints congratulatory message for the customer informing them how much they have after winning
        print("Congratulations " + str(customerName) + "\n You won" + str(wonAmount) + "Ksh",
              "and now you have" + str(totalMoney) + "Ksh", "for your shopping", file=sourceFile)
    else:
        print("sorry! Better Luck next time", file=sourceFile)
        print("You have " + str(totalMoney) +
              " Ksh for your shopping.", file=sourceFile)

# Till number one for buying bread: ask customer if they would like some.
breadTill = input("Would you like to buy bread? Y or N : ")
if breadTill.lower() != "y":
    print("No bread purchased. Thanks, You can move to the next till.", file=sourceFile)
elif breadTill.lower() == "y":
    print("Thanks for purchasing bread.", file=sourceFile)

    # ask customer how many loaves of bread they want and ensure they input an integer for their choice
    try:
        numBread = int(input("How many loaves of Bread Would You Like?: "))
    except ValueError:
        numBread = int(input("Please input an integer?: "))

    # inform customer of the total cost of bread for their selection and access if they have enough money for it.
    totalCostOfBread = numBread * bread
    print("The total cost for purchasing the loaf(ves) of bread is",
          totalCostOfBread, "Ksh", file=sourceFile)
    if totalCostOfBread > totalMoney:
        print("You do not have enough money to make this purchase. Please move to the next Till", file=sourceFile)
    elif totalCostOfBread <= totalMoney:
        totalMoney = totalMoney-totalCostOfBread
        amtBread = amtBread + numBread
        totalMoneySpent = totalMoneySpent + totalCostOfBread
        # print out message for customer for the total purchase made.
        print("You have purchased", numBread,
              "loaf(ves) of bread for", totalCostOfBread, "Ksh", file=sourceFile)

# Till number two for buying milk: ask customer if they would like some.
milkTill = input("Would you like to buy milk? Y or N : ")
if milkTill.lower() != "y":
    print("No milk purchased. Thanks, You can move to the next till.", file=sourceFile)
elif milkTill.lower() == "y":
    print("Thanks for purchasing milk.", file=sourceFile)

   # ask customer how many packets of milk they want and ensure they input an integer for their choice
   # code that enters an error if user doesnt input integer
    try:
        numMilk = int(input("How many packets of milk would You Like?: "))
    except ValueError:
        numMilk = int(input("Please input an integer?: "))

     # inform customer of the total cost of milk for their selection and access if they have enough money for it.
    totalCostOfMilk = numMilk * milk
    print("The total cost for purchasing the packet(s) of milk is",
          totalCostOfMilk, "Ksh", file=sourceFile)
    if totalCostOfMilk > totalMoney:
        print("You do not have enough money to make this purchase. Please move to the next Till", file=sourceFile)
    elif totalCostOfMilk <= totalMoney:
        totalMoney = totalMoney-totalCostOfMilk
        amtMilk = amtMilk + numMilk
        totalMoneySpent = totalMoneySpent + totalCostOfMilk
        # print out message for customer for the total purchase made.
        print("You have purchased", numMilk,
              "packet(s) of milk for", totalCostOfMilk, "Ksh", file=sourceFile)

# to check if customer qualifies for BlueBand Promotion
    if amtBread >= 2 and amtMilk >= 1:
        print("Congratulations! You qualify for our BlueBand Promo", file=sourceFile)
        rand = random.choice([0, 1, 2, ])
        print("the random number selected is", rand, file=sourceFile)

    # random winning number is 1
    # the winnings are selected randomly among integers (2.5 - 10)
    # the winnings are multiplied by a constant, 20, so that the maximum win is 200
        if rand == 1:
            print(
                "Congratulations! You are our lucky BlueBand Promo winner", file=sourceFile)
            winnings = random.randint(2.5, 10)
            wonAmountBlueband = winnings * 20
            totalMoney = totalMoney+wonAmountBlueband
            print("The amount won in the Blue Band Promo is: ",
                  wonAmountBlueband, "Ksh", file=sourceFile)
        else:
            print("Oops!,the winning number is 1, better luck next time.",
                  file=sourceFile)

# Till number two for buying soda: ask customer if they would like some.
sodaTill = input("Would you like to buy soda? Y or N : ")
if sodaTill.lower() != "y":
    print("No soda purchased. Thanks, You have finished your shopping.", file=sourceFile)
elif sodaTill.lower() == "y":
    print("Thanks for purchasing soda.", file=sourceFile)

    # ask customer how many bottlesof soda they want and ensure they input an integer for their choice
    # code that enters an error if user doesnt input integer
    try:
        numSoda = int(input("How many bottles of soda would you like?: "))
    except ValueError:
        numSoda = int(input("Please input an integer?: "))

    # inform customer of the total cost of soda for their selection and access if they have enough money for it.
    totalCostOfSoda = numSoda * soda
    print("The total cost for purchasing the bottle(s) of soda is",
          totalCostOfSoda, "Ksh", file=sourceFile)

    if totalCostOfSoda > totalMoney:
        print("You do not have enough money to make this purchase. You have finished your shopping", file=sourceFile)
    elif totalCostOfSoda <= totalMoney:
        totalMoney = totalMoney-totalCostOfSoda
        amtSoda = +numSoda
        totalMoneySpent = totalMoneySpent + totalCostOfSoda
        # print out message for customer for the total purchase made.
        print("You have purchased", numSoda,
              "bottle(s) of soda for", totalCostOfSoda, "Ksh", file=sourceFile)

# PRINT OUT STATEMENT AT THE END OF SHOPPING
print("You have finished your shopping! \nYou have spent", totalMoneySpent, "Ksh and your balance is", totalMoney, "Ksh. \nYou purchased", amtTicket, "lottery ticket(s) and won",
      wonAmount, "Ksh. \nYou purchased", amtBread, "loaf(ves) of bread,", amtMilk, "packet(s) of milk and", amtSoda, "bottle(s) of soda.", file=sourceFile)

# 50% DISCOUNT ON ENTIRE SHOPPING
print("We have a guessing game for a chance to get 50% discount off your shopping. You get 3 guesses.", file=sourceFile)
numOfGuesses = 3
i = 1
attendantNumber = 11
guessOne = int(input("Whats your first guess? : "))
while i <= numOfGuesses:
    if guessOne == 11:
        print("Correct! Congratulations, you get 50% off your shopping. You will pay",
              totalMoneySpent * 0.5, "Ksh instead of", totalMoneySpent, "Ksh", file=sourceFile)

    elif guessOne != 11:
        if guessOne > attendantNumber and i != 3:
            print(
                "Your guess is higher than the winning number. Try Again", file=sourceFile)
            guessOne = int(
                input("Enter your guess number" + str(i+1) + " : "))
        elif guessOne < attendantNumber and i != 3:
            print("Your guess is lower than the winning number. Try Again", file=sourceFile
                  )
            guessOne = int(
                input("Enter your guess number" + str(i+1) + " : "))
        else:
            print("Oops! Better Luck next time. Goodbye.", file=sourceFile)
    i += 1
sourceFile.close()
