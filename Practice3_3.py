#Author :- Jaymin Patel
#Description :- Hotel Management System using Python

#Declaring Global Variable
import random
from datetime import datetime
import re

#Dictionary of Room Numbers Booked for Categories 1,2,3,4
room_no={1:[],2:[],3:[],4:[]}
room_price=[]
#Dictionary of bill amount with Customer Id as Key
billamounts={}
#Dictionary Containing all the booking records for every Customer Id
records={}

#Booking Function-----
#Validates date input with datetime and ensures that checkin date isn't after checkout date
#Uses RegEx to validte and ensure that name and phone number are entered in correct format
#Randomly generates a customer id and allocates a room number
#Creates a record once a booking is made

def Booking():
    print("When do you want to Book")
    ci=input("Check In-->")
    ci=[int(i) for i in ci.split("/")]
    ci=datetime(ci[2],ci[1],ci[0])
    print(ci)
    co=input("Check Out-->")
    co=[int(i) for i in co.split("/")]
    co=datetime(co[2],co[1],co[0])
    print(co)
    print((co-ci).days)
    print("SELECT ROOM TYPE")
    print(" 1. Standard Non-AC \t\t3500")
    print(" 2. Standard AC     \t\t4000")
    print(" 3. 3-Bed Non-AC    \t\t4500")
    print(" 4. 3-Bed AC        \t\t5000")
    #This Dict contains the prices of hotels
    prices={1:3500,2:4000,3:4500,4:5000}
    type=int(input("Enter Room Type-->"))
    try:
        #checks if Check Out Date is before Check In Date
        print("in try",(co-ci).days>0)
        if((co-ci).days>0):
            if len(room_no[type])<50:
                print("Available")
            else:
                print("Unavailble")
        else:
            print("Check Out Date can't be before Check In Date")
    except:
        print("Incorrect Date format. Re-enter values")
        Booking()

    cname=input("Name->")
    #checks if name entered in correct format
    if(not(bool(re.match('[a-zA-Z\s]+$',cname)))):
        print('Name is Incorrect Format')
        Booking()
    cphone=input("Phone Number->")
    if not(bool(re.match('^[6-9]{1}[0-9]{9}$', cphone))):
        print("Phone is Incorrect Format")
        Booking()
    caddress=input("Address->")


    #generates random non repetitive room_no
    def room_no_generator():
        n=type*100+random.randrange(50)
        if(n in room_no[type]):
            room_no_generator()
        return n
    #generates random non repetitive cust id
    def cid_generator():
        n=type*1000+random.randrange(999)
        if(n in records.keys()):
            cid_generator()
        return n
    rn=room_no_generator()
    cid=cid_generator()
    billamounts[cid]=prices[type]*(co-ci).days
    room_no[type].append(rn)
    print("Room Booked Successfully")
    print(cname,cphone)
    print("Room:",rn,"CustID:",cid)
    print("Bill Amount=",billamounts[cid])
    records[cid]="Room No"+str(rn)+" "+str(cname)+" "+str(cphone)

#Room information function
#Enables the customers to view the types of rooms available in the hotel
#Allow the customer to check the availability of given types of rooms
#Room information and checcking availability
def Rooms_Info():
    print("1)Single Non-AC Room(1 Single Bed,Small almirah,1 Tea Table,Telephone)\n")
    print("2)Double-Bed Non-AC Room(1 Double Bed,Television,Large almirah,2 Tea Table,Telephone)\n")
    print("3)Triple Bed Non-AC Room(3 Single Bed,Television,Large Almirah,3 Tea Table,Telephone,Balcony)\n")
    print("4)Double-Bed AC Room(1 Double Bed,Television,Large Almirah,Air-Conditioner,Balcony,2 Tea Table,Telephone)\n")
    x=int(input("Please Enter your choice--->"))

    if ((x==1) and len(room_no[x])<50)  :
        print("Available")
        print("You have opted Single-Bed Non-AC Room ")
        room_price=2000
        print("Your room price per Day=",room_price,"\n")
    elif ((x==2) and len(room_no[x])<50):
        print("Available")
        print("You have opted Double-Bed Non-AC Room ")
        room_price=3000
        print("Your room price per Day=",room_price,"\n")
    elif ((x==3) and len(room_no[x])<50):
        print("Available")
        print("You have opted Triple-Bed Non-AC Room ")
        room_price=4000
        print("Your room price per Day=",room_price,"\n")
    elif ((x==4) and len(room_no[x])<50):
        print("Available")
        print("You have opted Double-Bed AC Room ")
        room_price=5000
        print("Your room price per Day=",room_price,"\n")
    else:
        print("Unavailable")

#Records
#Shows all the booking related records in the hotel
def Record():
    for i,j in records.items():
        print(i,j)

#Room Service
#Adds the additional amount of servies to total bill

def Room_Service():
    amount=0
    cid=input("Enter Customer ID-->")
    print("Select Service")
    print(" 1. Dining")
    print(" 2. Room Cleaning")
    print(" 3. Laundry")
    print(" 4. Other")
    choice=int(input("Choice Number:"))
    if choice==1:
        Restaurant_Menu()
        amount=amount+Pay_for_food()
    elif choice==2:
        print("Cleaning Requested")
    elif choice==3:
        itemcount=int(input("Enter Number of Items:"))
        amount=amount+itemcount*20
    else:
        other_amount=int(input("Enter amount if any:"))
        amount=amount+other_amount
    billamounts[cid]=billamounts[cid]+amount



#Restaurant menu function
#Display the menu of food items available with rates in the restaurant
def Restaurant_Menu():
    print("*****Restaurant Menu*****\n".center(25))

    print("     <---Bevrages--->\n")
    print("1)Tea...................10.00\n")
    print("2)Coffee................20.00\n")
    print("3)Cold Drink............30.00\n")
    print("4)Water.................20.00\n")
    print("     <---Breakfast--->\n")
    print("5)Samosa................10.00\n")
    print("6)Burger................30.00\n")
    print("7)Sandwitch.............25.00\n")
    print("8)Idli..................20.00\n")
    print("     <---Lunch--->\n")
    print("9)Combo Lunch...........200.00\n")
    print("     <---Dinner--->\n")
    print("10)DinnerCombo..........250.00\n")
    print("     <---Icecream--->\n")
    print("11)Vanilla icecream.....20.00\n")
    print("12)Choclate icecream....40.00\n")

#Pay for food function
#Stores the restaurant menu index wise in the dictionary
#Print the keys of dictionary in variable
#Request customer to lodge the food order with the restaurant
#Display total amount of bill of the ordered food by the customer

def Pay_for_food():
    sum=0
    # dictionary to save rate of food items indexwise
    dict={'1':10.00,'2':20.00,'3':30.00,'4':20.00,'5':30.00,'6':10.00,'7':25.00,'8':20.00,'9':200.00,'10':250.00,'11':20.00,'12':40.00}

    while(True):
        order=input("<---Please enter the code of food item--->")
        print("Please press E to exit the order")
        if order in dict.keys():
            sum=sum+dict[order]
        elif order=='E':
            break
        else:
            print("Please enter the right choice of food")
    print("***Restaurant Bill***")
    print("The total bill for food =",sum)
    return sum

#Payment
#Generates total bill of a customer and displays all the customer information
def Payment():
    cid=input("Enter CID->")
    print("Customer Details : ",records[cid])

    print("The Total Bill is : ",billamounts[cid])


def Home():
    choice=1
    while(choice!=0):
        print("*****Welcome to Hotel Bella Casa*****".center(127))
        print("\t\t 1 Booking\n")
        print("\t\t 2 Room Info\n")
        print("\t\t 3 Record\n")
        print("\t\t 4 Room Service\n")
        print("\t\t 5 Order Food\n")
        print("\t\t 6 Pay For Food\n")
        print("\t\t 7 Total Bill\n")
        print("\t\t 0 Exit\n")
        choice=int(input("Choose your option ->"))

        if choice == 1:
            Booking()
        elif choice == 2:
            Rooms_Info()
        elif choice == 3:
            Record()
        elif choice == 4:
            Room_Service()
        elif choice == 5:
            Restaurant_Menu()
        elif choice == 6:
            Pay_for_food()
        elif choice == 7:
            Payment()
        else:
            choice=0
        
Home()
