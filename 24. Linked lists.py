class Node:
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next = next

    def __str__(self):
        return str(self.cargo)


node = Node("pac")
print(node)

node1 = Node("unu")
node2 = Node("doi")
node3 = Node("trei")
node4 = Node("patru")
node5 = Node("cinci")
node6 = Node("sase")

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6


# Ex 1


def print_list(node):
    print("[", end="")
    while node is not None:
        print(node, end="")
        node = node.next
        if node is not None:
            print(",", end=" ")
    print("]")


def remove_second(list):
    if list is None:
        return
    first = list
    try:
        second = list.next
        first.next = second.next
        second.next = None
    except AttributeError:
        print("Your list do not contains any node. Can't procede!")
    return second

# Q: What happens if you pass the empty list as an argument?
# A: Will return None.

# Q: What happens if you invoke this method and pass a list with only one element (a singleton)?
# A: You will get an exception.


removed = remove_second(node1)
print_list(node1)
