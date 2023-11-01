#Program that gives and calculates communication of the month

#function which takes as parameter a duration of communication of the month and returns a list
def telecom(duration):
    Tab = []
    Tab.append(duration*2)
    OP1 = minutes - 30
    if OP1 >= 0 :
        cal1 = 20 + OP1 * 1.5
        Tab.append(cal1)
    else :
        Tab.append(20)
    OP2 = minutes - 60
    if OP2 >= 0 :
        cal2 = 50 + OP2 * 1
        Tab.append(cal2)
    else :
        Tab.append(50)
    OP3 = minutes - 120
    if OP3 >= 0 :
        cal3 = 100 + OP3 * 0.5
        Tab.append(cal3)
    else :
        Tab.append(100)
    return Tab


#proposal of offers
duration = int(input("enter the number of hours :"))
minutes = int(input("enter the number of minutes :"))
minutes = duration * 60 + minutes
print(f"Votre minutes {minutes}")
print("Please see our four plans :")
Tab = telecom(duration)
T2 = [0,20,50,100]
for i in range (4):
    print(f"This is the plans {i+1} has an amount of {Tab[i]}DH if you are subscribed  :",T2[i],"DH")
for i in range(4):
    for j in range(i+1,4):
        if (Tab[j] < Tab[i]):
             minimum = Tab[j]
print(f"the best for you when you well pay :{minimum} MAD")
print("We have another plan this plan is the best so the plan is you pau 200 DH and you get infinity time to speak")