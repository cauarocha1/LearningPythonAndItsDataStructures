majority = 18
special_majority = 15

age = int(input("State your age: "))

#if age >= majority:
   #print("Majority, you can do your Driver License")

#if age < majority:
    #print("You cannot do your Driver License")
    
#if age >= majority:
    #print("Majority, you can do your Driver License")
#else:
    #print("You cannot do your Driver License")
    
if age >= majority:
    print("Majority, you can do your Driver License")
elif age == special_majority:
    print("You can do only teoric classes")
else: 
    print("You cannot do your Driver License")