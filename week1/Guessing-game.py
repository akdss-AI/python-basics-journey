
num=9
while True:
 i=int(input("enter your guess:"))
 if(i<num):
    print("too low")
 elif(i>num):
    print("too high")
 else:
    print("guess is correct")
    break
