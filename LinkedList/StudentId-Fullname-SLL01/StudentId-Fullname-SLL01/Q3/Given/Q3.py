class Drink:
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
        new_node = Node(Drink(code, make, amount, volume, price))
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
        S1 = Drink('2C014', 'Coca-Cola', 10, '600ml', 12)
        # ------------------------------------------------------------------------------
        # -------------------------- Start your code here ------------------------------
        new_node = Node(S1)
        self.tail.next = new_node


        # -------------------------- End your code here --------------------------------
        # ------------------------------------------------------------------------------
        self.display()

    # This function is used for Question 2
    def f2(self):
        # Initialize a new node that will be used in Question 2
        new_node = Node(Drink('NEWNODE', 'Sprite', 15, '390ml', 12))
        # ------------------------------------------------------------------------------
        # -------------------------- Start your code here ------------------------------
        pcurrent = self.head
        while pcurrent.next.next:
            pcurrent = pcurrent.next
        
        pcurrent.next = new_node
        new_node.next = self.tail


        # -------------------------- End your code here --------------------------------
        # ------------------------------------------------------------------------------
        self.display()

    # This function is used for Question 3
    def f3(self):
        # We use t to store the Drink object with maximum amount
        t = None
        # ------------------------------------------------------------------------------
        # -------------------------- Start your code here ------------------------------
        pmin = self.head.data.price
        pcurrent = self.head.next
        while pcurrent:            
            if pcurrent.data.price <= pmin:
                pmin = pcurrent.data.price
                t = pcurrent.data
            pcurrent = pcurrent.next
        
        # -------------------------- End your code here --------------------------------
        # ------------------------------------------------------------------------------
        print(t or self.tail.data, end=' ')

    # This function is used for Question 4
    def f4(self):
        # ------------------------------------------------------------------------------
        # -------------------------- Start your code here ------------------------------
        pcurrent = self.head
        while pcurrent.next.next:
            pcurrent = pcurrent.next

        pcurrent.next = None
        self.tail = pcurrent
        
        pcurrent = self.head
        while pcurrent.next:
            pnext = pcurrent.next
            while pnext:
                if pnext.data.price > pcurrent.data.price:
                    pnext.data, pcurrent.data = pcurrent.data, pnext.data
                pnext = pnext.next
            pcurrent = pcurrent.next


        # -------------------------- End your code here --------------------------------
        # ------------------------------------------------------------------------------
        self.display()

    # This function is used for Question 5
    def f5(self):
        # We use t to store the Drink object satisfying the requirement
        t = None
        mvalue = None
        # ------------------------------------------------------------------------------
        # -------------------------- Start your code here ------------------------------
        pcurrent = self.head
        while pcurrent:
            lcurrent = self.head
            lvalue = 0            
            while lcurrent != pcurrent:
                lvalue += lcurrent.data.price * lcurrent.data.amount
                lcurrent = lcurrent.next
            
            rcurrent = pcurrent.next
            rvalue = 0
            while rcurrent:
                rvalue += rcurrent.data.price * rcurrent.data.amount
                rcurrent = rcurrent.next
            
            value = abs(lvalue - rvalue)
            if not mvalue:
                mvalue = value
            elif value < mvalue:
                mvalue = value
                t = pcurrent.data
            pcurrent = pcurrent.next
        
        
        # -------------------------- End your code here --------------------------------
        # ------------------------------------------------------------------------------
        print(t, end=' ')


# ========================DO NOT EDIT GIVEN STATEMENTS IN THE MAIN FUNCTION.============================
# ===IF YOU CHANGE, THE GRADING SOFTWARE CAN NOT FIND THE OUTPUT RESULT TO SCORE, THUS THE MARK IS 0.===
def main():
    print("Do you want to run Q1?")
    print("1. Run f1()")
    print("2. Run f2()")
    print("3. Run f3()")
    print("4. Run f4()")
    print("5. Run f5()")

    n = int(input("Enter a number : "))

    lst = LinkedList()
    size = int(input("Input the size of list (amount of nodes - from 1 to 10):\nsize =   "))
    while (size < 1 or size > 10):
        size = int(input("Please input the size of list (amount of nodes - from 1 to 10):\nsize =   "))
    lst.loadData(size)

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