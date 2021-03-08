totFloor = 20
passIndex = 1

class Elevator:
    direction = "up" #Going up
    floor = 0 #All lifts are at ground

def getElev(passenger,el1,el2):
    global passIndex
    fInf = passenger.split(",")
    try:
        curr = int(fInf[0])
        dest = int(fInf[1])
        for i in fInf:
            if int(i) > totFloor:
                print("\nInvalid Enteries.(Floors cannot exceed building size 20)...")
                exit
    except:
        print("\nInvalid Inputs, Please try again...\n")
        exit
    print("\nPassenger " + str(passIndex) + ":")
    passIndex += 1
    print("\tCurrent Floor: ",curr,"\n\tDestination Floor: ",dest)
    
    if curr > dest:
        direc = "down"
    elif curr < dest:
        direc = "up"
    else:
        print("\tLift: None")
        return

    '''If any Elevator is on User's floor, call it'''
    if el1.floor == curr:
        el1.floor = dest
        el1.direction = direc
        print("\tLift: Elevator1\n\tDirection: ",el1.direction)
        return
    if el2.floor == curr:
        el2.floor = dest
        el2.direction = direc
        print("\tLift: Elevator2\n\tDirection: ",el2.direction)
        return

    '''Elevator not on user's floor, call the closesrt one going in user's direction'''
    if abs(el1.floor - curr) > abs(el2.floor - curr):
        el2.floor = dest
        el2.direction = direc
        print("\tLift: Elevator2\n\tDirection: ",el2.direction)
        return
    else:
        el1.floor = dest
        el1.direction = direc
        print("\tLift: Elevator1\n\tDirection: ",el1.direction)
        return

    

def main():
    e1 = Elevator()
    e2 = Elevator()
    print("\t\tELEVATOR\n\n")
    ip = input("Enter passanger info (floor,destination floor,destination ... for multiple passangers)\n")
    pas = ip.split(" ")
    for p in pas:
        getElev(p,e1,e2)

if __name__ == "__main__":
    main()