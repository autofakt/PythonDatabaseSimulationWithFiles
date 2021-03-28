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



class Node1(object): #contact node

    id: int

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

class Node2(object): #address node

    def __init__(self, id=0, aid=0, address1="", address2="", apt="", city="", state="", zip="", country="",n=None):
        self.id = id
        self.aid = aid
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

    def get_aid(self):
        return self.aid

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

class Node3(object): #phone node

    def __init__(self, id=0, pid=0, type="", number="",n=None):
        self.id = id
        self.pid = pid
        self.type = type.upper()
        self.number = number
        self.next_node = n

    def get_next(self):
        return self.next_node

    def set_next(self, n):
        self.next_node = n

    def get_id(self):
        return self.id

    def get_pid(self):
        return self.pid

    def get_type(self):
        return self.type

    def get_number(self):
        return self.number

    def set_type(self, type):
        self.type = type.upper()

    def set_number(self, number):
        self.number = number

    def has_next(self):
        if self.get_next() is None:
            return False
        return True

class LinkedList1(object): #contact linkedlist
    def __init__(self,counter=1,root=None):
        self.root = root
        #self.size = 0
        self.counter = counter

    # def get_size(self):
    #     return self.size

    def get_counter(self):
        return self.counter

    def add(self, id=0, fName="", lName="", gender=""):
        new_node = Node1(id, fName, lName, gender.upper()) #Makes gender uppercase
        self.counter = self.counter + 1
        if self.root is None:
            self.root = new_node
            # self.size += 1
            return
        last = self.root
        while last.next_node:
            last = last.next_node
        last.next_node = new_node
        # self.size += 1

    def addNoCounter(self, id=0, fName="", lName="", gender=""):
        new_node = Node1(id, fName, lName, gender.upper())  # Makes gender uppercase
        if self.root is None:
            self.root = new_node
            # self.size += 1
            return
        last = self.root
        while last.next_node:
            last = last.next_node
        last.next_node = new_node
        # self.size += 1

    def remove(self, id):
        this_node = self.root
        prev_node = None
        while this_node is not None:
            if this_node.get_id() == id:
                if prev_node is not None:
                    prev_node.set_next(this_node.get_next())
                else:
                    self.root = this_node.get_next()
                # self.size -= 1
                #self.counter -= 1
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

class LinkedList2(object): #address linkedlist
    def __init__(self,counter=1,aid=1,root=None):
        self.root = root
        # self.size = 0
        self.counter = counter
        self.aid = aid

    # def get_size(self):
    #     return self.size

    def get_counter(self):
        return self.counter

    def get_aid(self):
        return self.aid

    def add(self, id=0, aid=0, address1="", address2="", apt="", city="", state="", zip ="",country=""):
        new_node = Node2(id, aid, address1.upper(), address2.upper(), apt.upper(), city.upper(),state.upper(), zip.upper(), country.upper()) #Makes gender uppercase
        self.counter += 1
        if self.root is None:
            self.root = new_node
            # self.size += 1
            return
        last = self.root
        while last.next_node:
            last = last.next_node
        last.next_node = new_node
        # self.size += 1

    def addNoCounter(self, id=0, aid=0, address1="", address2="", apt="", city="", state="", zip="", country=""):
        new_node = Node2(id,aid, address1.upper(), address2.upper(), apt.upper(), city.upper(), state.upper(), zip.upper(),
                         country.upper())  # Makes gender uppercase
        if self.root is None:
            self.root = new_node
            # self.size += 1
            return
        last = self.root
        while last.next_node:
            last = last.next_node
        last.next_node = new_node
        # self.size += 1

    def remove(self, id):
        this_node = self.root
        prev_node = None
        while this_node is not None:
            if this_node.get_id() == id:
                if prev_node is not None:
                    prev_node.set_next(this_node.get_next())
                else:
                    self.root = this_node.get_next()
                # self.size -= 1
                #self.counter -= 1
                return True
            else:
                prev_node = this_node
                this_node = this_node.get_next()
        return False

    def remove2(self, id):
        temp = self.root
        prev = None

        while temp != None and temp.get_id() == id:
            self.root = temp.get_next()
            temp = self.root
        while temp != None:

            while(temp != None and temp.get_id() != id):
                prev = temp
                temp = temp.get_next()
            if temp == None:
                return False
            prev.set_next(temp.get_next())
            temp = prev.get_next()
        return True

    def removeByAID(self, aid):
        temp = self.root
        prev = None

        while temp != None and temp.get_aid() == aid:
            self.root = temp.get_next()
            temp = self.root
        while temp != None:

            while(temp != None and temp.get_aid() != aid):
                prev = temp
                temp = temp.get_next()
            if temp == None:
                return False
            prev.set_next(temp.get_next())
            temp = prev.get_next()
        return True




    def findByID(self, inputID):
        this_node = self.root
        while this_node is not None:
            if this_node.get_id() == inputID:
                print(f"AD: {this_node.get_id()}  {this_node.get_address1()}  {this_node.get_address2()}  {this_node.get_apt()}  {this_node.get_city()}  {this_node.get_state()}  {this_node.get_zip()}  {this_node.get_country()}")
                this_node = this_node.get_next()
            else:
                this_node = this_node.get_next()


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

    def editByAID(self, inputAID):
        this_node = self.root
        while this_node is not None:
            if this_node.get_aid() == inputAID:

                address1New = input("Please enter new address1: ")
                address2New = input("Please enter new address2(blank if none): ")
                aptNew = input("Please enter new apt(blank if none): ")
                cityNew = input("Please enter new city: ")
                stateNew = input("Please enter new state: ")
                zipNew = input("Please enter new zip: ")
                countryNew = input("Please enter new country: ")

                this_node.set_address1(address1New)
                this_node.set_address2(address2New)
                this_node.set_apt(aptNew)
                this_node.set_city(cityNew)
                this_node.set_state(stateNew)
                this_node.set_zip(zipNew)
                this_node.set_country(countryNew)
                print(f"AD: {this_node.get_id()}  {this_node.get_address1()}  {this_node.get_address2()}  {this_node.get_apt()}  {this_node.get_city()}  {this_node.get_state()}  {this_node.get_zip()}  {this_node.get_country()}")
                return True
            else:
                this_node = this_node.get_next()
        return False

    def print_list(self):
        print("[Print List]")
        if self.root is None:
            return
        this_node = self.root
        print(f"AD: {this_node.get_id()}  {this_node.get_aid()}  {this_node.get_address1()}  {this_node.get_address2()}  {this_node.get_apt()}  {this_node.get_city()}  {this_node.get_state()}  {this_node.get_zip()}  {this_node.get_country()}")
        while this_node.has_next():
            this_node = this_node.get_next()
            print(f"AD: {this_node.get_id()}  {this_node.get_aid()}  {this_node.get_address1()}  {this_node.get_address2()}  {this_node.get_apt()}  {this_node.get_city()}  {this_node.get_state()}  {this_node.get_zip()}  {this_node.get_country()}")
        print("[-----------]")

class LinkedList3(object): #phone linkedlist
    def __init__(self,counter=1,pid=1,root=None):
        self.root = root
        # self.size = 0
        self.counter = counter
        self.pid = pid

    # def get_size(self):
    #     return self.size

    def get_counter(self):
        return self.counter

    def get_pid(self):
        return self.pid

    def add(self, id=0, pid=0, type="", number=""):
        new_node = Node3(id, pid, type.upper(), number)
        self.counter += 1
        if self.root is None:
            self.root = new_node
            # self.size += 1
            return
        last = self.root
        while last.next_node:
            last = last.next_node
        last.next_node = new_node
        # self.size += 1

    def addNoCounter(self, id=0, pid=0, type="", number=""):
        new_node = Node3(id,pid, type.upper(), number)
        if self.root is None:
            self.root = new_node
            # self.size += 1
            return
        last = self.root
        while last.next_node:
            last = last.next_node
        last.next_node = new_node
        # self.size += 1

    def remove(self, id):
        this_node = self.root
        prev_node = None
        while this_node is not None:
            if this_node.get_id() == id:
                if prev_node is not None:
                    prev_node.set_next(this_node.get_next())
                else:
                    self.root = this_node.get_next()
                # self.size -= 1
                #self.counter -= 1
                return True
            else:
                prev_node = this_node
                this_node = this_node.get_next()
        return False

    def remove2(self, id):
        temp = self.root
        prev = None

        while temp != None and temp.get_id() == id:
            self.root = temp.get_next()
            temp = self.root
        while temp != None:

            while(temp != None and temp.get_id() != id):
                prev = temp
                temp = temp.get_next()
            if temp == None:
                return False
            prev.set_next(temp.get_next())
            temp = prev.get_next()
        return True

    def removeByPID(self, pid):
        temp = self.root
        prev = None

        while temp != None and temp.get_pid() == pid:
            self.root = temp.get_next()
            temp = self.root
        while temp != None:

            while(temp != None and temp.get_pid() != pid):
                prev = temp
                temp = temp.get_next()
            if temp == None:
                return False
            prev.set_next(temp.get_next())
            temp = prev.get_next()
        return True

    def findByID(self, inputID): #used to find/print phones in contact search. Uses ID to search not PID.
        this_node = self.root
        while this_node is not None:
            if this_node.get_id() == inputID:
                print(f"PH: {this_node.get_id()}  {this_node.get_pid()}  {this_node.get_type()}  {this_node.get_number()}")
                this_node = this_node.get_next()
            else:
                this_node = this_node.get_next()


    def editByPID(self, inputPID): #used to edit phones in fron edit phones option. Uses PID to edit not ID.
        this_node = self.root
        while this_node is not None:
            if this_node.get_pid() == inputPID:
                typeNew = input("Enter new phone type: ")
                numberNew = input("Enter new phone number(9 digit format): ")
                this_node.set_type(typeNew)
                this_node.set_number(numberNew)
                print(f"PH: {this_node.get_id()}  {this_node.get_pid()}  {this_node.get_type()}  {this_node.get_number()}")
                return True
            else:
                this_node = this_node.get_next()
        return False

    def print_list(self):
        print("[Print List]")
        if self.root is None:
            return
        this_node = self.root
        print(f"PH: {this_node.get_id()}  {this_node.get_pid()}  {this_node.get_type()}  {this_node.get_number()}")
        while this_node.has_next():
            this_node = this_node.get_next()
            print(f"PH: {this_node.get_id()}  {this_node.get_pid()}  {this_node.get_type()}  {this_node.get_number()}")
        print("[-----------]")

def loadCounters():
    with open("counters.txt","r") as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    content = content[0].split()
    f.close()
    return content

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

def readPhonesFileIntoList():
    with open("phones.txt","r") as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    f.close()
    return content

def fillLinkedList1(counter, activeID): #counter gives the last recorded id value
    tempLinkedList = LinkedList1(counter)
    readList = readContactsFileIntoList()
    if len(readList)!= 0: #checks to see if file is empty
        for x in readList:
            splitFile = x.split()
            activeID.append(int(splitFile[0])) #adds active IDs into list to input validation
            tempLinkedList.addNoCounter(int(splitFile[0]),splitFile[1],splitFile[2],splitFile[3])
    return tempLinkedList

def fillLinkedList2(counter):
    tempLinkedList = LinkedList2(counter)
    readList = readAddressFileIntoList()
    if len(readList) != 0:  # checks to see if file is empty
        for x in readList:
            splitFile = x.split()
            tempLinkedList.addNoCounter(int(splitFile[0]),int(splitFile[1]),splitFile[2],splitFile[3],splitFile[4],splitFile[5],splitFile[6],splitFile[7],splitFile[7])
    return tempLinkedList

def fillLinkedList3(counter):
    tempLinkedList = LinkedList3(counter)
    readList = readPhonesFileIntoList()
    if len(readList) != 0:  # checks to see if file is empty
        for x in readList:
            splitFile = x.split()
            tempLinkedList.addNoCounter(int(splitFile[0]),int(splitFile[1]),splitFile[2],splitFile[3])
    return tempLinkedList

def createContact(activeID): #activeID keeps track of live CID's for input validation
    id = myList1.get_counter()
    aid = myList2.get_counter()
    pid = myList3.get_counter()

    fName = input("Please enter first name: ")
    lName = input("Please enter last name: ")
    gender = input("Please enter gender: ")
    myList1.add(id, fName, lName, gender)
    myList1.print_list()

    activeID.append(id)
    print(f"ActiveID: {activeID}")

    address1 = input("Please enter address1: ")
    address2 = input("Please enter address2(blank if none): ")
    apt = input("Please enter apt(blank if none): ")
    city = input("Please enter city: ")
    state = input("Please enter state: ")
    zip = input("Please enter zip: ")
    country = input("Please enter country: ")
    myList2.add(id,aid, address1, address2, apt, city, state, zip, country)
    myList2.print_list()

    type = input("Please enter phone type: ")
    number = input("Please enter phone number(9 digit format): ")
    myList3.add(id, pid, type, number)
    myList3.print_list()


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

def writeLinkedListIntoAddressFile(myList2):
    tempList = []
    this_node = myList2.root
    while this_node:
        tempList.append(str(this_node.get_id()) +" "+ str(this_node.get_aid()) +" "+ this_node.get_address1() +" "+ this_node.get_address2() +" "+ this_node.get_apt() +" "+ this_node.get_city() +" "+ this_node.get_state()+" "+ this_node.get_zip()+" "+ this_node.get_country())
        this_node = this_node.get_next()
    with open("address.txt","w") as f:
        for x in tempList:
            f.write(x+"\n")
    f.close()
    # print(tempList)

def writeLinkedListIntoPhoneFile(myList3):
    tempList = []
    this_node = myList3.root
    while this_node:
        tempList.append(str(this_node.get_id()) +" "+ str(this_node.get_pid()) +" "+ this_node.get_type() +" "+ this_node.get_number())
        this_node = this_node.get_next()
    with open("phones.txt","w") as f:
        for x in tempList:
            f.write(x+"\n")
    f.close()
    # print(tempList)

def writeCounterValues(myList1,myList2,myList3):
    tempList = []
    contactsCounter = myList1.get_counter()
    addressCounter = myList2.get_counter()
    phoneCounter = myList3.get_counter()
    tempList.append(str(contactsCounter) +" "+ str(addressCounter) +" "+ str(phoneCounter))
    with open("counters.txt","w") as f:
        for x in tempList:
            f.write(x)
    f.close()
    print(tempList)

def searchContact():
    option = 0
    while option != 5:
        if option == 1:
            inputID = input("Enter id number: ")
            myList1.findByID(int(inputID))
            myList2.findByID(int(inputID))
            myList3.findByID(int(inputID))
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

def deleteContact(activeID):
    inputID = input("Enter id for delete: ")
    while inputID.isdigit() == False:
        inputID = input("Must be a digit. Enter id for edit: ")
    myList1.remove(int(inputID))
    myList2.remove2(int(inputID))
    myList3.remove2(int(inputID))

    if activeID:
        if inputID in activeID:
            activeID.remove(int(inputID))
        else:
            print("No such id found.")
    print(f"ActiveID: {activeID}")

def deleteAddress():
    inputAID = input("Enter a-id for delete: ")
    while inputAID.isdigit() == False:
        inputAID = input("Must be a digit. Enter a-id for edit: ")
    myList2.removeByAID(int(inputAID))

def deletePhone():
    inputPID = input("Enter p-id for delete: ")
    while inputPID.isdigit() == False:
        inputPID = input("Must be a digit. Enter p-id for edit: ")
    myList3.removeByPID(int(inputPID))

def editContact():
    inputID = input("Enter id for edit: ")
    while inputID.isdigit() == False:
        inputID = input("Must be a digit. Enter id for edit: ")
    myList1.editByID(int(inputID))

def editAddress():
    inputAID = input("Enter a-id for edit: ")
    while inputAID.isdigit() == False:
        inputAID = input("Must be a digit. Enter a-id for edit: ")
    myList2.editByAID(int(inputAID))

def editPhone():
    inputPID = input("Enter p-id for edit: ")
    while inputPID.isdigit() == False:
        inputPID = input("Must be a digit. Enter p-id for edit: ")
    myList3.editByPID(int(inputPID))

def addAddress(activeID):
    inputID = input("Enter id for address add: ")  #need to be able to validate if ID exists
    while inputID.isdigit() == False or int(inputID) not in activeID: #checks if digit is entered and id found in activeID
        inputID = input("Invalid input. Enter id for address add: ")
    address1 = input("Please enter address1: ")
    address2 = input("Please enter address2(blank if none): ")
    apt = input("Please enter apt(blank if none): ")
    city = input("Please enter city: ")
    state = input("Please enter state: ")
    zip = input("Please enter zip: ")
    country = input("Please enter country: ")
    myList2.add(int(inputID), myList2.get_counter(),address1, address2, apt, city, state, zip, country)
    myList2.print_list()

def addPhone(activeID):
    inputID = input("Enter id for phone add: ")  #need to be able to validate if ID exists
    while inputID.isdigit() == False or int(inputID) not in activeID: #checks if digit is entered and id found in activeID
        inputID = input("Invalid input. Enter id for phone add: ")
    type = input("Please enter phone type: ")
    number = input("Please enter phone number(9 digit format): ")
    myList3.add(int(inputID), myList3.get_counter(), type, number)
    myList3.print_list()

counterList = loadCounters() # Grabs ID counters from txt file and loads each into the linkedlist

activeID = []

myList1 = fillLinkedList1(int(counterList[0]),activeID) #Convert contact counter string to int value, active ID tracks all live CID's
print(f"ActiveID: {activeID}")
myList2 = fillLinkedList2(int(counterList[1]))
myList3 = fillLinkedList3(int(counterList[2]))

option = 0
while option != 14:
    if option == 1:
        createContact(activeID)
    if option == 2:
        addAddress(activeID)
    if option == 3:
        addPhone(activeID)
    if option == 4:
        editContact()
    if option == 6:
        editPhone()
    if option == 5:
        editAddress()
    if option == 7:
        searchContact()
    if option == 8:
        deleteContact(activeID)
    if option == 9:
        deleteAddress()
    if option == 10:
        deletePhone()
    if option == 11:
        myList1.print_list()
    if option == 12:
        myList2.print_list()
    if option == 13:
        myList3.print_list()
    

    print("1 - Create Contact")
    print("2 - Add Address")
    print("3 - Add Phone")
    print("4 - Edit Contact")
    print("5 - Edit Address")
    print("6 - Edit Phone")
    print("7 - Search Contact")
    print("8 - Delete Contact")
    print("9 - Delete Address")
    print("10 - Delete Phone")
    print("11 - Print Contacts")
    print("12 - Print Address")
    print("13 - Print Phones")
    print("14 - Exit")
    option = input("Please select an option: ")
    while option.isdigit() == False:  #checks if digit is entered and id found in activeID
        option = input("Invalid input. Please select an option: ")
    option = int(option)

writeLinkedListIntoContactsFile(myList1)
writeLinkedListIntoAddressFile(myList2)
writeLinkedListIntoPhoneFile(myList3)
writeCounterValues(myList1,myList2,myList3)
