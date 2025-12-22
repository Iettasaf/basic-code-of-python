mark1=int(input("Enter mark: "))
mark2=int(input("Enter mark: "))
mark3=int(input("Enter mark: "))

#calculate Total Persentage
total_persentage = (100*(mark1+mark2+mark3)/300)

if(total_persentage>=40):
    print("You are passed in:",total_persentage)

else:
    print("You are failed in:",total_persentage)