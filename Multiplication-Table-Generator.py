topic = "MULTIPLICATION TABLE CALCULATOR"
print(topic.center(50))



num = int(input("Enter the Number : "))
limit  = int(input("Enter your Limit number : "))
i=1
while i<= limit:
    mult = i*num
    print(mult)
    i+=1
