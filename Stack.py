
num = int(input("Enter a size of the stack:"))
stack = []
while True:
    print("1.Push\n2.Pop\n3.Peep\n4.Exit")
    response = int(input("Enter Your Choice:"))
    if response == 1:
        if num == len(stack):
            print("Stack is Full")
        else:
            element = int(input("Enter The Element Which element do you want to insert:"))
            stack.insert(0, element)
            print("Element Successfully Inserted")
        print()
    elif response == 2:
        if len(stack) == 0:
            print("Stack is Empty")
        else:
            value = stack[0]
            stack.remove(value)
            print("Element Successfully Removed")
            for i in stack:
                print(i, end=" ")
        print()
    elif response == 3:
        if len(stack) == 0:
            print(f"Your Stack Is Empty {stack}")
        else:
            for i in stack:
                print(i, end=" ")
        print()
    else:
        if len(stack) == 0:
            print(f"Your Stack Is Empty {stack}")
        else:
            for i in stack:
                print(i, end="")
        break