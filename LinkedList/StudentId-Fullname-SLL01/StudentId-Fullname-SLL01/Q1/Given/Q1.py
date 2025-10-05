class SoftDrink:
    def __init__(self, code, make, amount, volume, price):
        self.code = code
        self.make = make
        self.amount = amount
        self.volume = volume
        self.price = price

    def __repr__(self):
        return f"{self.code}, {self.make}, {self.amount}, {self.volume}, {'%.3f' % self.price}"


class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addLast(self, code, make, amount, volume, price):
        new_node = Node(SoftDrink(code, make, amount, volume, price))
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
            print()

    def loadData(self, size):
        data = ['PS021', 'Pepsi', 10, '390ml', 10,
                'MD033', 'Mirinda', 45, '320ml', 12,
                'SP005', 'Schweppes', 8, '320ml', 10,
                '2C017', 'Coca-Cola', 20, '600ml', 15,
                'MD029', 'Mirinda', 14, '390ml', 18,
                'SP002', 'Bohuc', 18, '320ml', 12,
                '2C014', 'Teaplus', 23, '600ml', 12,
                'MD026', 'Soda', 16, '390ml', 15,
                '2C018', 'C2', 23, '600ml', 12,
                'MD020', 'Lavie', 16, '330ml', 6]
        for i in range(size):
            self.addLast(data[5*i], data[5*i+1], data[5*i+2], data[5*i+3], data[5*i+4])

    # This function is used for Question 1
    def f1(self):
        # ------------------------------------------------------------------------------
        # -------------------------- Start your code here ------------------------------
        # new_node = Node()
        new_node = Node(SoftDrink('NEWNODE', '7-Up', 12, '330ml', 8.000))
        new_node.next = self.head
        self.head = new_node
        
        
        # -------------------------- End your code here --------------------------------
        # ------------------------------------------------------------------------------
        self.display()

    # This function is used for Question 2
    def f2(self):
        # Initialize a new node that will be used in Question 2
        new_node = Node(SoftDrink('NEWNODE', 'Sprite', 15, '390ml', 12))
        # ------------------------------------------------------------------------------
        # -------------------------- Start your code here ------------------------------
        pindex = 0
        pcurrent = self.head
        while pcurrent and pindex < 2:
            pcurrent = pcurrent.next
            pindex += 1

        new_node.next = pcurrent.next
        pcurrent.next = new_node
        
        # -------------------------- End your code here --------------------------------
        # ------------------------------------------------------------------------------
        self.display()

    # This function is used for Question 3
    def f3(self):
        # ------------------------------------------------------------------------------
        # -------------------------- Start your code here ------------------------------
        pcurrent = self.head
        while pcurrent:
            if 'M' in pcurrent.data.make:
                pcurrent.data.price  = 999.000
            pcurrent = pcurrent.next
        
        
        # -------------------------- End your code here --------------------------------
        # ------------------------------------------------------------------------------
        self.display()

    # This function is used for Question 4
    def f4(self):
        # ------------------------------------------------------------------------------
        # -------------------------- Start your code here ------------------------------
        self.head = self.head.next        
        pcurrent  = self.head
        while pcurrent:
            pnext = pcurrent.next
            flag  = True
            while pnext:
                if pnext.data.price < self.head.data.price:
                    pnext.data, pcurrent.data = pcurrent.data, pnext.data
                    flag = False
                pnext = pnext.next
            if flag:
                break
            pcurrent = pcurrent.next             
        

        # -------------------------- End your code here --------------------------------
        # ------------------------------------------------------------------------------
        self.display()

    # This function is used for Question 5
    def f5(self):
        # ------------------------------------------------------------------------------
        # -------------------------- Start your code here ------------------------------
        pcurrent = self.head
        if pcurrent.data.make == 'Mirinda':
            self.head = self.head.next

        while pcurrent:
            if pcurrent.next != None and pcurrent.next.data.make == 'Mirinda':
                pcurrent.next = pcurrent.next.next
                if pcurrent.next == self.tail:
                    self.tail = pcurrent
            pcurrent = pcurrent.next


        # -------------------------- End your code here --------------------------------
        # ------------------------------------------------------------------------------
        self.display()


# ========================DO NOT EDIT GIVEN STATEMENTS IN THE MAIN FUNCTION.============================
# ===IF YOU CHANGE, THE GRADING SOFTWARE CAN NOT FIND THE OUTPUT RESULT TO SCORE, THUS THE MARK IS 0.===
def main():
    lst = LinkedList()
    size = int(input("Input the size of tree (amount of nodes - from 1 to 10):\nsize =   "))
    while (size < 1 or size > 10):
        size = int(input("Please input the size of tree (amount of nodes - from 1 to 10):\nsize =   "))
    lst.loadData(size)
    print("Do you want to run Q1?")
    print("1. Run f1()")
    print("2. Run f2()")
    print("3. Run f3()")
    print("4. Run f4()")
    print("5. Run f5()")

    n = int(input("Enter a number : "))

    if n == 1:
        print("OUTPUT:")
        lst.f1()

    if n == 2:
        print("OUTPUT:")
        lst.f2()

    if n == 3:
        print("OUTPUT:")
        lst.f3()

    if n == 4:
        print("OUTPUT:")
        lst.f4()

    if n == 5:
        print("OUTPUT:")
        lst.f5()


# End main
# --------------------------------
if __name__ == "__main__":
    main()
# ============================================================