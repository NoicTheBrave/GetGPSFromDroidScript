""" holder = "asdfasdfsafdasdf"
tst = "asdf1234" """

""" print(holder.isnumeric())
print(tst.isnumeric()) """


def checkForNumbers(inputString): #if numbers in string, returns TRUE
    tstCounter = 0 
    for i in range(len(inputString)): 
        if (inputString[i].isnumeric() or (inputString[i] == ".")) == True:
            tstCounter += 1
    if tstCounter != 0: #basically if its not a number OR float / double...
        #print("String has numbers inside! Proceed as normal")
        return True
    else: 
        #print("YO SHHHHHHHHTUFF IS FUCKED ! <3 uWu")
        return False
""" 
print("HOLDER CHECK")
checkForNumbers(holder)

print("----------")

print("tst CHECK")
checkForNumbers(tst) """