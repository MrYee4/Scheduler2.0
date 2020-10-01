# Spencer Nettles
# CS 246
# This program will ask about what you want in your week
# It will also ask when you wnat to do it
# Then it will schedule out your week in a nice day to day list

def printList(l):
    index = 0
    count = 1
    while index < (len(l) - 1):
        print('\t', count, ': ', l[index])
        count += 1
        index += 1

def main():
    #all the lists for everyday
    mon = list()
    tue = list()
    wed = list()
    thur = list()
    fri = list()
    sat = list()
    sun = list()

#MONDAYS Block
    print("What do you need to do on Monday:  (press n for next day)")
    mon.append(input("\t"))
    while mon[-1] != 'n':
        mon.append(input("\t"))

#TUESDAYS Block
    print("What do you need to do on Tuesday:  (press n for next day)")
    tue.append(input("\t"))
    while tue[-1] != 'n':
        tue.append(input("\t"))

#WEDNESDAYS Block
    print("What do you need to do on Wednesday:  (press n for next day)")
    wed.append(input("\t"))
    while wed[-1] != 'n':
        wed.append(input("\t"))

#THURSDAYS Block
    print("What do you need to do on Thurday:  (press n for next day)")
    thur.append(input("\t"))
    while thur[-1] != 'n':
        thur.append(input("\t"))

#FRIDAYS Block
    print("What do you need to do on Friday:  (press n for next day)")
    fri.append(input("\t"))
    while fri[-1] != 'n':
        fri.append(input("\t"))

#SATURADYS Block
    print("What do you need to do on Saturday:  (press n for next day)")
    sat.append(input("\t"))
    while sat[-1] != 'n':
        sat.append(input("\t"))

#SUNDAYS Block
    print("What do you need to do on Sunday:  (press n for next day)")
    sun.append(input("\t"))
    while sun[-1] != 'n':
        sun.append(input("\t"))

#Print My list
    print("\nHere is a list of things to do Monday:")    
    printList(mon)
    print("-----------------------------------------")
    print("\nHere is a list of things to do Tuesday:")    
    printList(tue)
    print("-----------------------------------------")
    print("\nHere is a list of things to do Wednesday:")    
    printList(wed)
    print("-----------------------------------------")
    print("\nHere is a list of things to do Thursday:")    
    printList(thur)
    print("-----------------------------------------")
    print("\nHere is a list of things to do Friday:")    
    printList(fri)
    print("-----------------------------------------")
    print("\nHere is a list of things to do Saturday:")    
    printList(sat)
    print("-----------------------------------------")
    print("\nHere is a list of things to do Sunday:")    
    printList(sun)

if __name__ == "__main__":
    main()