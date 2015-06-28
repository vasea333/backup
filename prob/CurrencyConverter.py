from pip._vendor.distlib.compat import raw_input
def currencyConverter():
    userChoice = raw_input("what do you wont to convert? \n1)USD > Euro \n2)Euro > USD \n")
    if userChoice == "1":
        userUSD = raw_input("Enter the amount in USD you wish to convert \n")
        Euro = int(userUSD) * 0.88
        print("$", userUSD, "= ", Euro, "Euro")
        print("-------------------------------------------------------------")
        doAgain()
    elif userChoice == "2":
        userEuro = raw_input("Enter the amount in Euro you wish to convert \n")
        USD = int(userEuro) / 0.88
        print("Euro", userEuro, "= ", USD, "$")
        print("-------------------------------------------------------------")
        doAgain()
    else:
        print("Error: You entered invalid information. Please try again")
        print("-------------------------------------------------------------")
        currencyConverter()
def doAgain():
    userDoAgain = raw_input ("Would you like convert again? \n1) Yes \n2) No \n")
    if userDoAgain == "1":    
        currencyConverter()
    elif userDoAgain == "2": 
        print("Thank you for using this program")
    else:
        print ("Error: You entered invalid information. Please try again")   
        doAgain()
currencyConverter()