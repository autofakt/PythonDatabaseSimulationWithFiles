# import mysql.connector
#
# cnx = mysql.connector.connect(user='root', password='blue5555',
#                               host='127.0.0.1',
#                               database='sakila')
#
# mycursor = cnx.cursor()
# '''
# creates table
# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
# '''
#
# #Print all available tables
# mycursor.execute("SHOW TABLES")
#
# for x in mycursor:
#   print(x)

from datetime import datetime
from random import seed
from random import randint
# seed random number generator
seed(datetime.now())

class Node1(object):

    def __init__(self, id=0, fName="", lName="", gender="", n=None):
        self.id = id
        self.fName = fName.upper()
        self.lName = lName.upper()
        self.gender = gender.upper()
        self.next_node = n

    def get_next(self):
        return self.next_node

    def set_next(self, n):
        self.next_node = n

    def get_id(self):
        return self.id

    def get_fName(self):
        return self.fName

    def get_lName(self):
        return self.lName

    def get_gender(self):
        return self.gender

    def set_fName(self, fName):
        self.fName = fName.upper()

    def set_lName(self, lName):
        self.lName = lName.upper()

    def set_gender(self, gender):
        self.gender = gender.upper()

    def has_next(self):
        if self.get_next() is None:
            return False
        return True

class Node2(object):

    def __init__(self, id=0, address1="", address2="", apt="", city="", state="", zip="", country="",n=None):
        self.id = id
        self.address1 = address1.upper()
        self.address2 = address2.upper()
        self.apt = apt.upper()
        self.city = city.upper()
        self.state = state.upper()
        self.zip = zip
        self.country = country.upper()
        self.next_node = n

    def get_next(self):
        return self.next_node

    def set_next(self, n):
        self.next_node = n

    def get_id(self):
        return self.id

    def get_address1(self):
        return self.address1

    def get_address2(self):
        return self.address2

    def get_apt(self):
        return self.apt

    def get_city(self):
        return self.city

    def get_state(self):
        return self.state

    def get_zip(self):
        return self.zip

    def get_country(self):
        return self.country

    def set_address1(self, address1):
        self.address1 = address1.upper()

    def set_address2(self, address2):
        self.address2 = address2.upper()

    def set_apt(self, apt):
        self.apt = apt.upper()

    def set_city(self, city):
        self.city = city.upper()

    def set_state(self, state):
        self.state = state.upper()

    def set_zip(self, zip):
        self.zip = zip

    def set_country(self, country):
        self.country = country.upper()

    def has_next(self):
        if self.get_next() is None:
            return False
        return True

class LinkedList1(object):
    def __init__(self, root=None):
        self.root = root
        self.size = 0

    def get_size(self):
        return self.size

    def add(self, id=0, fName="", lName="", gender=""):
        new_node = Node1(id, fName, lName, gender.upper()) #Makes gender uppercase
        if self.root is None:
            self.root = new_node
            self.size += 1
            return
        last = self.root
        while last.next_node:
            last = last.next_node
        last.next_node = new_node
        self.size += 1

    def remove(self, id):
        this_node = self.root
        prev_node = None
        while this_node is not None:
            if this_node.get_id() == id:
                if prev_node is not None:
                    prev_node.set_next(this_node.get_next())
                else:
                    self.root = this_node.get_next()
                self.size -= 1
                return True
            else:
                prev_node = this_node
                this_node = this_node.get_next()
        return False

    def findByID(self, inputID):
        this_node = self.root
        while this_node is not None:
            if this_node.get_id() == inputID:
                print(f"ID: {this_node.get_id()}  {this_node.get_fName()}  {this_node.get_lName()}  {this_node.get_gender()}")
                return True
            else:
                this_node = this_node.get_next()
        return False

    def findByFirstName(self, fName):
        this_node = self.root
        while this_node is not None:
            if this_node.get_fName() == fName:
                print(f"ID: {this_node.get_id()}  {this_node.get_fName()}  {this_node.get_lName()}  {this_node.get_gender()}")
                this_node = this_node.get_next()
            else:
                this_node = this_node.get_next()

    def findByLastName(self, lName):
        this_node = self.root
        while this_node is not None:
            if this_node.get_lName() == lName:
                print(f"ID: {this_node.get_id()}  {this_node.get_fName()}  {this_node.get_lName()}  {this_node.get_gender()}")
                this_node = this_node.get_next()
            else:
                this_node = this_node.get_next()

    def findByGender(self, gender):
        this_node = self.root
        while this_node is not None:
            if this_node.get_gender() == gender:
                print(f"ID: {this_node.get_id()}  {this_node.get_fName()}  {this_node.get_lName()}  {this_node.get_gender()}")
                this_node = this_node.get_next()
            else:
                this_node = this_node.get_next()

    def editByID(self, inputID):
        this_node = self.root
        while this_node is not None:
            if this_node.get_id() == inputID:
                fNameNew = input("Enter new first name: ")
                lNameNew = input("Enter new last name: ")
                genderNew = input("Enter new gender m/f: ")
                this_node.set_fName(fNameNew)
                this_node.set_lName(lNameNew)
                this_node.set_gender(genderNew)
                print(f"ID: {this_node.get_id()}  {this_node.get_fName()}  {this_node.get_lName()}  {this_node.get_gender()}")
                return True
            else:
                this_node = this_node.get_next()
        return False

    def print_list(self):
        print("[Print List]")
        if self.root is None:
            return
        this_node = self.root
        print(f"ID: {this_node.get_id()}  {this_node.get_fName()}  {this_node.get_lName()}  {this_node.get_gender()}")
        while this_node.has_next():
            this_node = this_node.get_next()
            print(f"ID: {this_node.get_id()}  {this_node.get_fName()}  {this_node.get_lName()}  {this_node.get_gender()}")
        print("[-----------]")

class LinkedList2(object):
    def __init__(self, root=None):
        self.root = root
        self.size = 0

    def get_size(self):
        return self.size

    def add(self, id=0, address1="", address2="", apt="", city="", state="", zip ="",country=""):
        new_node = Node2(id, address1.upper(), address2.upper(), apt.upper(), city.upper(),state.upper(), zip.upper(), country.upper()) #Makes gender uppercase
        if self.root is None:
            self.root = new_node
            self.size += 1
            return
        last = self.root
        while last.next_node:
            last = last.next_node
        last.next_node = new_node
        self.size += 1

    def remove(self, id):
        this_node = self.root
        prev_node = None
        while this_node is not None:
            if this_node.get_id() == id:
                if prev_node is not None:
                    prev_node.set_next(this_node.get_next())
                else:
                    self.root = this_node.get_next()
                self.size -= 1
                return True
            else:
                prev_node = this_node
                this_node = this_node.get_next()
        return False

    def findByID(self, inputID):
        this_node = self.root
        while this_node is not None:
            if this_node.get_id() == inputID:
                print(f"ID: {this_node.get_id()}  {this_node.get_address1()}  {this_node.get_address2()}  {this_node.get_apt()}  {this_node.get_city()}  {this_node.get_state()}  {this_node.get_zip()}  {this_node.get_country()}")
                return True
            else:
                this_node = this_node.get_next()
        return False

    def findByFirstName(self, fName):
        this_node = self.root
        while this_node is not None:
            if this_node.get_fName() == fName:
                print(f"ID: {this_node.get_id()}  {this_node.get_fName()}  {this_node.get_lName()}  {this_node.get_gender()}")
                this_node = this_node.get_next()
            else:
                this_node = this_node.get_next()

    def findByLastName(self, lName):
        this_node = self.root
        while this_node is not None:
            if this_node.get_lName() == lName:
                print(f"ID: {this_node.get_id()}  {this_node.get_fName()}  {this_node.get_lName()}  {this_node.get_gender()}")
                this_node = this_node.get_next()
            else:
                this_node = this_node.get_next()

    def findByGender(self, gender):
        this_node = self.root
        while this_node is not None:
            if this_node.get_gender() == gender:
                print(f"ID: {this_node.get_id()}  {this_node.get_fName()}  {this_node.get_lName()}  {this_node.get_gender()}")
                this_node = this_node.get_next()
            else:
                this_node = this_node.get_next()

    def editByID(self, inputID):
        this_node = self.root
        while this_node is not None:
            if this_node.get_id() == inputID:
                fNameNew = input("Enter new first name: ")
                lNameNew = input("Enter new last name: ")
                genderNew = input("Enter new gender m/f: ")
                this_node.set_fName(fNameNew)
                this_node.set_lName(lNameNew)
                this_node.set_gender(genderNew)
                print(f"ID: {this_node.get_id()}  {this_node.get_fName()}  {this_node.get_lName()}  {this_node.get_gender()}")
                return True
            else:
                this_node = this_node.get_next()
        return False

    def print_list(self):
        print("[Print List]")
        if self.root is None:
            return
        this_node = self.root
        print(f"ID: {this_node.get_id()}  {this_node.get_address1()}  {this_node.get_address2()}  {this_node.get_apt()}  {this_node.get_city()}  {this_node.get_state()}  {this_node.get_zip()}  {this_node.get_country()}")
        while this_node.has_next():
            this_node = this_node.get_next()
            print(f"ID: {this_node.get_id()}  {this_node.get_address1()}  {this_node.get_address2()}  {this_node.get_apt()}  {this_node.get_city()}  {this_node.get_state()}  {this_node.get_zip()}  {this_node.get_country()}")
        print("[-----------]")

def readContactsFileIntoList():
    with open("contacts.txt","r") as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    f.close()
    return content

def readAddressFileIntoList():
    with open("address.txt","r") as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    f.close()
    return content

def fillLinkedList1():
    tempLinkedList = LinkedList1()
    readList = readContactsFileIntoList()
    for x in readList:
        splitFile = x.split()
        tempLinkedList.add(int(splitFile[0]),splitFile[1],splitFile[2],splitFile[3])
    return tempLinkedList

def fillLinkedList2():
    tempLinkedList = LinkedList2()
    readList = readAddressFileIntoList()
    for x in readList:
        splitFile = x.split()
        tempLinkedList.add(int(splitFile[0]),splitFile[1],splitFile[2],splitFile[3],splitFile[4],splitFile[5],splitFile[6],splitFile[7])
    return tempLinkedList

def writeLinkedListIntoContactsFile(myList1):
    tempList = []
    this_node = myList1.root
    while this_node:
        tempList.append(str(this_node.get_id()) +" "+ this_node.get_fName() +" "+ this_node.get_lName() +" "+ this_node.get_gender())
        this_node = this_node.get_next()
    with open("contacts.txt","w") as f:
        for x in tempList:
            f.write(x+"\n")
    f.close()
    # print(tempList)

def writeLinkedListIntoAddressFile(myList1):
    tempList = []
    this_node = myList2.root
    while this_node:
        tempList.append(str(this_node.get_id()) +" "+ this_node.get_address1() +" "+ this_node.get_address2() +" "+ this_node.get_apt() +" "+ this_node.get_city() +" "+ this_node.get_state()+" "+ this_node.get_zip()+" "+ this_node.get_country())
        this_node = this_node.get_next()
    with open("address.txt","w") as f:
        for x in tempList:
            f.write(x+"\n")
    f.close()
    # print(tempList)

def createContact():
    id = randint(100000,999999)
    fName = input("Please enter first name: ")
    lName = input("Please enter last name: ")
    gender = input("Please enter gender: ")
    myList1.add(id, fName, lName, gender)
    myList1.print_list()

    address1 = input("Please enter address1: ")
    address2 = input("Please enter address2(blank if none): ")
    apt = input("Please enter apt(blank if none): ")
    city = input("Please enter city: ")
    state = input("Please enter state: ")
    zip = input("Please enter zip: ")
    country = input("Please enter country: ")
    myList2.add(id, address1, address2, apt, city, state, zip, country)
    myList2.print_list()


def searchContact():
    option = 0
    while option != 5:
        if option == 1:
            inputID = input("Enter id number: ")
            myList1.findByID(int(inputID))
        if option == 2:
            inputName = input("Enter first name: ")
            myList1.findByFirstName(inputName.upper())
        if option == 3:
            inputName = input("Enter last name: ")
            myList1.findByLastName(inputName.upper())
        if option == 4:
            inputGender = input("Enter gender m/f: ")
            myList1.findByGender(inputGender.upper()) #makes gender uppercase

        print("1 - Search by ID")
        print("2 - Search by First Name")
        print("3 - Search by Last Name")
        print("4 - Search by Gender")
        print("5 - Exit Search")
        option = int(input("Please select search option: "))

def deleteContact():
    inputID = input("Enter id for delete: ")
    myList1.remove(int(inputID))
    myList2.remove(int(inputID))

def editContact():
    inputID = input("Enter id for edit: ")
    myList1.editByID(int(inputID))


myList1 = fillLinkedList1()
myList2 = fillLinkedList2()

option = 0
while option != 7:
    if option == 1:
        createContact()
    if option == 2:
        editContact()
    if option == 3:
        searchContact()
    if option == 4:
        deleteContact()
    if option == 5:
        myList1.print_list()
    if option == 6:
        myList2.print_list()

    print("1 - Create Contact")
    print("2 - Edit Contact")
    print("3 - Search Contact")
    print("4 - Delete Contact")
    print("5 - Print List1")
    print("6 - Print List2")
    print("7 - Exit")
    option = int(input("Please select an option: "))

writeLinkedListIntoContactsFile(myList1)
writeLinkedListIntoAddressFile(myList2)
