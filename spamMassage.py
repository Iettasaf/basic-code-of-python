p1="buy this"
p2="click here"
p3="make a lots of money"
p4="suscribe now"

massage = input("Enter a massage: ")
if((p1 in massage) or (p2 in massage) or (p3 in massage) or (p4 in massage)):
    print("The massage is spam")
else:
    print("This massage is not spam")