userInput= input("Please Enter Item Code:") # take the input from user
i=list(userInput.upper()) # convert user input into capital letters so that user can give input in lower case also

countA = i.count("A") # find counts of individuals items
countB = i.count("B")
countC = i.count("C")
countD = i.count("D")


#calculations for special price
offerA = countA//3
withoutOfferA = countA%3
offerB = countB//2
withoutOfferB = countB%2


priceA = ((offerA*130)+(withoutOfferA*50))
priceB = ((offerB*45)+(withoutOfferB*30))
priceC = (countC*20)
priceD = (countD*15)

#total price
totalAmount= (priceA+priceB+priceC+priceD)
print("You have to pay",totalAmount, "for", userInput)