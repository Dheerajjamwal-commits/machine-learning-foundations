class invalidcount (Exception):
    def __init__(self):
        super().__init__("You entered invalid number for marks")
import json
sname=[]
sroll_no=[]
smarks=[]
c =[]
def adds ():
    n = int (input("Enter the number of students to add : "))
    for i in range(n):
        print(f"Enter details for {i} Student")
        sname.append(input("Enter Student name: "))
        sroll_no.append(int((input(f"Enter roll no. for {sname[i]} : "))))
        raw=input("Enter marks seperated by spaces : ")
        c.append([int(m) for m in raw.split()])
        # f = open ("Student.json",'r')
        # data = json.load(f)
        if i > 0:
            if len(c[i]) != len(smarks[0]):
                raise invalidcount
        smarks.append(c)
            
    d={
    "Student": [{
        "name" : name,
        "roll no." : r,
        "marks":mark }
        for name ,r, mark in zip(sname,sroll_no,smarks)]
}

    with open ("Student.json",'a') as s:
        j=json.dump(d,s,indent=2)
   
def avg ():
    s = open ('Student.json','r') 
    q=int(input("Do you wish to calculate average of one student marks or the whole class?\n enter 1 for one student marks \n enter 2 for entire class average \n 3 average of entire class individually : "))
    data = json.load(s)
    if q == 1:
        e = int(input("Enter the roll no of the student you wish to calculate average for : "))
        for i in data['Student']:
            if i['roll no.'] == e:
                print(f"Average of student {i['name']} is {sum(i['marks'])/len(i['marks'])}")
    elif q == 2:
        su =0
        for i in data['Student']:
            su += sum(i['marks'])
        print(f" Total average of combined students is : {su/len(data['Student'])}")
    elif q == 3:
        for i in data['Student']:
            print(f"Average of student {i['name']} is {sum(i['marks'])/len(i['marks'])}")

def menu():
    a=int(input ("Welcome to Student Grade manager What would you like to do \n 1. Add students \n 2. calculate Average : "))
    if a == 1:
        try :
            adds()
        except invalidcount as e:
            print(e)
            print("Try Again !!")
            adds()
    elif a == 2:
        avg()
    else:
        print("Enter a valid value")
menu()
c = input ("if you wish to continue enter anything else leave blank : ")
while c:
    menu()
    c = input ("if you wish to continue enter anything else leave blank : ")
