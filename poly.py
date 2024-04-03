"""polynomials"""
# Name 1: Sanjitha Venkata
# EID 1: sv28325

# Name 2: Swati Misra
# EID 2: SM83264

class Node:
    """
    A modified version of the Node class for linked lists (using proper class
    coding practices). Instead of a data attribute, this node class has both 
    a coefficient and an exponent attribute, which is used to represent each 
    term in a polynomial.
    """
    def __init__(self, coeff, exp, link=None):
        """
        Node Constructor for polynomial linked lists.

        Args:
        - coeff: The coefficient of the term.
        - exp: The exponent of the term.
        - link: The next node in the linked list.
        """
        self.coeff = coeff
        self.exp = exp
        self.next = link

    @property
    def coeff(self):
        """
        Getter method for the coefficient attribute.
        """
        return self.__coeff

    @coeff.setter
    def coeff(self, value):
        """
        Setter method for the coefficient attribute.
        """
        if value is None or isinstance(value, int):
            self.__coeff = value
        else:
            raise ValueError("Coefficient must be an integer or None.")

    @property
    def exp(self):
        """
        Getter method for the exponent attribute.
        """
        return self.__exp

    @exp.setter
    def exp(self, value):
        """
        Setter method for the exponent attribute.
        """
        if value is None or isinstance(value, int):
            self.__exp = value
        else:
            raise ValueError("Exponent must be an integer or None.")

    @property
    def next(self):
        """
        Getter method for the next attribute.
        """
        return self.__next

    @next.setter
    def next(self, value):
        """
        Setter method for the next attribute.
        """
        if value is None or isinstance(value, Node):
            self.__next = value
        else:
            raise ValueError("Next must be a Node instance or None.")

    def __str__(self):
        """
        String representation of each term in a polynomial linked list.
        """
        return f"({self.coeff}, {self.exp})"


class LinkedList:
    """linked list"""
    def __init__(self):
        # You are also welcome to use a sentinel/dummy node!
        # It is definitely recommended. If you choose to use
        # a dummy node, you can comment out the self.head = None
        # and comment in the below line. We use None to make sure
        # if there is an error where you accidentally include the
        # dummy node in your calculation, it will throw an error.
        self.dummy = Node(None, None)

        # self.head = None

    # Insert the term with the coefficient coeff and exponent exp into the polynomial.
    # If a term with that exponent already exists, add the coefficients together.
    # You must keep the terms in descending order by exponent.
    def insert_term(self, coeff, exp):
        """insert term"""
        current=self.dummy

        while current.next is not None and exp < current.next.exp:
            current=current.next
        if current.next is not None and exp == current.next.exp:
            current.next.coeff += coeff
            #might need to remove coeffs if =0
            current=current.next
        else:
            newnode=Node(coeff,exp,link=current.next)
            current.next=newnode

    # Add a polynomial p to the polynomial and return the resulting polynomial as a new linked list.
    def add(self, p):
        """add"""
        # fix code to have these:
        # x^2 + x = x^2 + x
        # (2x +2) + (2x+2) = 4x+4
        output = LinkedList()
        poly1=self.dummy.next
        poly2=p.dummy.next

        while poly1 is not None:
            output.insert_term(poly1.coeff, poly1.exp)
            poly1=poly1.next

        while poly2 is not None:
            output.insert_term(poly2.coeff, poly2.exp)
            poly2=poly2.next

        newlist=LinkedList()
        currentnode=output.dummy.next
        while currentnode is not None:
            if currentnode.coeff !=0:
                newlist.insert_term(currentnode.coeff, currentnode.exp)
            currentnode=currentnode.next
        return newlist
        # while poly1 is not None and poly2 is not None:
        #     if poly1.exp<poly2.exp:
        #         output.insert_term(poly2.coeff,poly2.exp)
        #         output.insert_term(poly1.coeff,poly1.exp)
        #         # output.next=poly2
        #         poly2=poly2.next
        #     elif poly2.exp<poly1.exp:
        #         output.insert_term(poly1.coeff,poly1.exp)
        #         output.insert_term(poly2.coeff,poly2.exp)
        #         # output.next=poly1
        #         poly1=poly1.next
        #     else:
        #         total_coeff=poly1.coeff+poly2.coeff
        #         if total_coeff != 0:
        #             output.insert_term(total_coeff,poly1.exp)
        #         poly1=poly1.next
        #         poly2=poly2.next
        #             #output.coeff.next=total_coeff #what

        # while poly1 is not None:
        #     # output.next=poly1
        #     output.insert_term(poly1.coeff,poly1.coeff)
        #     poly1=poly1.next
        # while poly2 is not None:
        #     # output.next=poly2
        #     output.insert_term(poly2.coeff,poly2.coeff)
        #     poly2=poly2.next


        # return output


    # Multiply a polynomial p with the polynomial and return the product as a new linked list.
    def mult(self, p):
        """mult"""
        #nested loop multiplying node from poly1 with everything from poly2
        #if same exp, add coeffs
        temp=LinkedList()
        poly1=self.dummy.next
        poly2=p.dummy.next

        # for _ in range(len(poly1)):
        #     for _ in range(len(poly2)):
        while poly1 is not None:
            poly2=p.dummy.next #resetting poly2
            while poly2 is not None:
                # temp.coeff.next= #change to temp.insert_word
                # temp.exp.next=
                # print(poly2.coeff, poly2.exp)
                temp.insert_term(poly1.coeff*poly2.coeff,poly1.exp+poly2.exp)
                poly2=poly2.next
            poly1=poly1.next

        # print("here")

        newlist=LinkedList()
        currentnode=temp.dummy.next
        while currentnode is not None:
            if currentnode.coeff !=0:
                newlist.insert_term(currentnode.coeff, currentnode.exp)
            currentnode=currentnode.next
        return newlist

        # output=LinkedList
        # poly1=self.dummy.next
        # poly2=p.dummy.next

        # # for _ in range(len(temp)):
        # #     for _ in range(len(temp)):
        # while poly1 is not None:
        #     while poly2 is not None:
        #         #can replace all code with output.add(temp) if add is correct
        #         output.add(output,temp)
        #         poly1=poly1.next
        #         poly2=poly2.next

        #         # if poly1.exp == poly2.exp:
        #         #     totalcoeff=poly1.coeff+poly2.coeff
        #         #     new_node=Node(totalcoeff,poly1.exp,None)
        #         #     output.next=new_node
        #         # else:
        #         #     new_node=Node(temp.coeff,temp.exp,None) #help
        #         #     output.next=new_node

        # return temp


    # Return a string representation of the polynomial.
    def __str__ (self):
        #iterate through length of poly
        #separate each coeff and exp into pairs -> varname.coeff, varname.exp
        #format into "(coeff, exp) +" until last node (ignore +)
        currentnode=self.dummy.next
        # output=[]
        # while currentnode is not None:
        #     output.append(f"({currentnode.coeff}, {currentnode.exp})")
        #     currentnode=currentnode.next
        # return " + ".join(output)
        output=""
        if currentnode is not None:
            output+=f"({currentnode.coeff}, {currentnode.exp})"
            currentnode=currentnode.next
        while currentnode is not None:
            output+=f" + ({currentnode.coeff}, {currentnode.exp})"
            currentnode=currentnode.next
        return output

def main():
    """main"""
    p=LinkedList()
    q=LinkedList()
    # read data from stdin and create polynomial p
    num = int(input())
    for _ in range(num):
        numlist = input()
        # split numlist into list w both elements
        numlist=numlist.split()
        # assign coeff to 0th element and exp to 1st
        coeff = int(numlist[0])
        exp = int(numlist[1])
        p.insert_term(coeff, exp)

    input() #newline separating p and q

    # read data from stdin and create polynomial q
    num2 = int(input())
    for _ in range(num2):
        numlist = input()
        # split numlist into list w both elements
        numlist=numlist.split()
        # assign coeff to 0th element and exp to 1st
        coeff = int(numlist[0])
        exp = int(numlist[1])
        q.insert_term(coeff, exp)

    # get sum of p and q as a new linked list and print sum
    sumpq=str(p.add(q))
    print(sumpq)

    # get product of p and q as a new linked list and print product
    productpq=str(p.mult(q))
    # print("out here")
    print(productpq)

if __name__ == "__main__":
    main()
