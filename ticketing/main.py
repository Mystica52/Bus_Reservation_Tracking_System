import pandas as pd

def admin():
    ch = str(input("Enter Admin Password "))
    if ch == "root":
        menu()
    else:
        print("Invalid Password, Try again! \n")
        admin()
def menu():

    print("Ticket")
    print("-------")
    print("1. Read File Bus")
    print("2. Add Bus to File")
    print("3. List Schedule")
    print("4. Sort Buses")
    print("5. bus Inquiry")
    print("6. Cancel Bus")
    print("7. ticket reservation")
    print("8. Add Passenger tickets details in file")
    print("9. LOGOUT")
    print()

    ch = int(input("Enter your choice: "))

    while (ch > 0):
        if ch == 1:
            read_buses()
            break
        elif ch == 2:
            new_bus()
            break
        elif ch == 3:
            schedule()
            break
        elif ch == 4:
            sort_buses()
            break
        elif ch == 5:
            enquiry()
            break
        elif ch == 6:
            cancelbus()
            break
        elif ch == 7:
            ticketreservation()
            break
        elif ch == 8:
            new_passenger()
            break
        elif ch == 9:
            login()
        else:
            print("Invalid selection")



def login():
    print("1. Admin Menu")
    print("2. User Menu")
    print("3. EXIT \n")
    ch = int(input())
    if ch == 1:
        admin()
    elif ch == 2:
        user()
    elif ch == 3:
        exit()
    else:
        print("Invalid Choice, Try again! \n")
        login()
def user():

    print("Ticket")
    print("-------")
    print("1. Read File Bus")
    print("2. List Schedule")
    print("3. Sort Buses")
    print("4. bus Inquiry")
    print("5. ticket reservation")
    print("6. Add Passenger tickets details in file")
    print("7. EXIT")
    print()

    ch = int(input("Enter your choice: "))

    while (ch > 0):
        if ch == 1:
            read_buses()
            break
        elif ch == 2:
            schedule()
            break
        elif ch == 3:
            sort_buses()
            break
        elif ch == 4:
            enquiry()
            break
        elif ch == 5:
            ticketreservation()
            break
        elif ch == 6:
            new_passenger()
            break
        elif ch == 7:
            exit()
        else:
            print("Invalid selection")


def retry():
    choice = str(input("Do you want to return to main menu? (Y/N) "))
    if choice.upper() == "Y" or choice.upper() == "YES":
        menu()
    elif choice.upper() == "N" or choice.upper() == "NO":
        exit()
    else:
        print("Invalid choice")




def read_buses():
    print("Reading Details of File bus")
    print()
    print()
    df = pd.read_csv("bus.csv", index_col = 0)
    print(df)
    print()
    retry()




def new_bus():
    print("Adding new Bus in File bus")

    df = pd.read_csv("bus.csv", index_col = 0)

    print(df)
    n=(input("Enter Bus No. : "))
    a=(input ("Enter Bus Name "))
    b=(input ("Enter Start "))
    c=(input ("Enter Stop "))
    d=str (input ("Enter Departure: "))
    e=str (input ("Enter Arrival. "))
    f = str(input("Enter Duration of Journey: "))
    r = int(input("Enter Frequency: "))
    df.loc[n] = [a, b, c, d, e, f, r]
    print(df)
    print()
    retry()



def schedule():
    print("Schedule of ALL Buses")
    print()

    df = pd.read_csv("bus.csv", usecols=['busno', 'busname', 'arrival', 'departure'])
    print(df)
    print()
    retry()


def sort_buses():
    print("sorting of Buses")
    print()
    df = pd.read_csv("bus.csv", index_col=0)
    df = df.sort_values('busno')
    print(df)
    print()
    retry()


def RAE13_fare():
    print("Show Fares of RAE13 Bus")
    print()
    df = pd.read_csv("RAE13.csv", usecols=['start', 'stop', 'fare'], index_col=0)
    print(df)
    print()
    retry()


def RAD12_fare():
    print("Show Fares of RAD12 Bus")
    print()
    df = pd.read_csv("RAD12.csv", usecols=['start', 'stop', 'fare'], index_col=0)
    print(df)
    print()
    retry()

def enquiry():
    print("Find out Time Table a Bus")
    df = pd.read_csv("bus.csv", index_col=0, usecols=['busname', 'start', 'arrival', 'duration'])
    print(df)
    print()
    retry()


def cancelbus():
    print("Deleting Cancelled Bus Detail")
    df = pd.read_csv("bus.csv", index_col='busname')
    print(df)

    tnum = (input("enter Bus Name. :"))

    df.drop(tnum,  axis=0, inplace=True)

    print("Record of Bus Temporarily deleted")
    print()
    print(df)
    print()
    retry()


def updateRAE13() :
    print("To increase fare and save")
    print('Previous Fares')
    print()
    df = pd.read_csv("RAE13.csv")
    print(df)
    print()
    print("increase fare by Frw 50")
    print()
    df = pd.read_csv("RAE13.csv")
    df['fare']+= 50
    print(df)
    print()
    retry()


def ticketreservation():
    print("WE HAVE THE FOLLOWING Buses FOR YOU:")
    print("Bus RAE13 To HUYE FROM KIGALI:")
    print("For RAE13---")
    print()

    print("1. If u want to get down at MUHANGA Pay Rwf. 2000")
    print("2. If u want to get down at NYANZA Pay Rwf. 2500")
    print("3. If u want to get down at HUYE Pay Rwf. 4000")
    print()
    print("Bus RAD12 To GISENYI FROM KIGALI: -")
    print()
    print("For RAD12..")
    print("1. If u want to get down at RULINDO Pay Rwf. 1500")
    print("2. If u want to get down at NYABIHU Pay Rwf. 2200")
    print("2. If u want to get down at GISENYI Pay Rwf. 3000")
    busname = (input("ENTER YOUR CHOICE of Bus No. PLEASE->"))
    print (busname)
    x = int(input("ENTER No. of YOUR CHOICE of Stop PLEASE"))
    n = int(input("HOW MANY TICKETS YOU NEED: "))

    if (busname =='RAE13'):
        if(x == 1):
            print("YOU HAVE Chosen 1st Stop MUHANGA")
            s = 2000 * n
        elif (x == 2):
            print("YOU HAVE Chosen 2nd Stop NYANZA")
            s = 2500 * n
        elif (x == 3):
            print("YOU HAVE Chosen 3rd Stop HUYE")
            s = 3000 * n
        else:
            print("Invalid option")
            print("PLEASE CHOOSE A Correct Bus No.")
        print("YOUR TOTAL TICKET PRICE is=",s, "\n")

    elif(busname =='RAD12'):
       if (x == 1):
          print("YOU HAVE Chosen 1st Stop RULINDO")
          s = 1500 * n
       elif (x == 2):
          print("YOU HAVE Chosen 2nd Stop NYABIHU")
          s = 2200 * n
       elif (x == 4):
          print("YOU HAVE Chosen Last Stop GISENYI")
          s = 3000 * n
       else:
            print("Invalid option")
            print("PLEASE CHOOSE A Correct Bus No.")
       print("your TOTAL TICKET PRICE is =", s,"\n")
    else:
        print("Bus Not AvaiLable")
    print()
    retry()

def new_passenger():
    print("Adding new Passenger Ticket Detail in File")
    print()
    df = pd.read_csv("RAE13.csv", index_col=0)
    print("RAE13 to HUYE")
    print(df)
    print()
    df = pd.read_csv("RAD12.csv", index_col=0)
    print("RAD12 to GISENYI")
    print(df)
    print()
    print()
    print("Record of Previous Sale of Tickets")
    df = pd.read_csv("passengers.csv")
    print(df)
    n = (input("Enter Bus No."))
    a = int(input("Enter tickets : "))
    b = (input("Enter Start : "))
    c = (input("Enter Stop : "))
    r = int(input("Fare : "))
    f = a * r
    df.loc[3] = [n, a, b, c, f]
    print(df)
    print()
    retry()

login()
