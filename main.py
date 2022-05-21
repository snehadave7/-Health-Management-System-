import datetime
def getdate():
    import datetime
    return datetime.datetime.now()

def log(a):
    if a==1:
         c=int(input("What you want to log- Diet(1) or Exercise(2)"))
         if c==1:
             value=input("type here\n")
             f=open("Person_1_food","a")
         f.write(str(str(getdate()))+":"+value+ "\n")
         print("successfully written")
         if c==2:
             value = input("type here\n")
             f = open("Person_1_exercise", "a")
             f.write(str(str(getdate())) + ":" + value + "\n")
             print("successfully written")
    elif a==2:
         c = int(input("What you want to log- Diet(1) or Exercise(2)"))
         if c == 1:
             value = input("type here\n")
             f = open("Person_2_food", "a")
         f.write(str(str(getdate())) + ":" + value + "\n")
         print("successfully written")
         if c == 2:
             value = input("type here\n")
             f = open("Person_2_exercise", "a")
             f.write(str(str(getdate())) + ":" + value + "\n")
             print("successfully written")
    elif a==3:
         c = int(input("What you want to log- Diet(1) or Exercise(2)"))
         if c == 1:
             value = input("type here\n")
             f = open("Person_3_food", "a")
         f.write(str(str(getdate())) + ":" + value + "\n")
         print("successfully written")
         if c == 2:
             value = input("type here\n")
             f = open("Person_3_exercise", "a")
             f.write(str(str(getdate())) + ":" + value + "\n")
             print("successfully written")

def retrieve(k):
    if k==1:
        c=int(input("enter 1 for food and 2 for exercise"))
        if(c==1):
            with open("Person_1_food") as op:
                for i in op:
                    print(i,end="")
        elif(c==2):
            with open("Person_1_exercise") as op:
                for i in op:
                    print(i, end="")
    elif(k==2):
        c = int(input("enter 1 for food and 2 for exercise"))
        if (c == 1):
            with open("Person_2_food") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("Person_2_exercise") as op:
                for i in op:
                    print(i, end="")
    elif(k==3):
        c = int(input("enter 1 for food and 2 for exercise"))
        if (c == 1):
            with open("Person_3_food") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("Person_3_exercise") as op:
                for i in op:
                    print(i, end="")


print("health management system: ")
a=int(input("Press 1 for log the value and 2 for retrieve "))
if a == 1:
    b = int(input("Press 1 for person1 2 for person2 3 for person3 "))
    log(b)
else:
    b = int(input("Press 1 for person1 2 for person2 3 for person3 "))
    retrieve(b)
