arr_size = int(input("Enter The Size of the Queue:"))
front = -1
rare = -1
arr = [None]*arr_size
def Enqueue():
    global front, rare, arr_size, arr
    if rare == arr_size-1:
        return "Queue is Full"
    else:
        x = int(input("Enter which element do you want to insert:"))
        if front == rare == -1:
            rare += 1
            front += 1
            arr[rare] = x
            return "Successfully element inserted"
        else:
            rare += 1
            arr[rare] = x
            return "Successfully element inserted"
def Dequeue():
    global front, rare, arr
    if front == rare == -1:
        return "Queue is Empty"
    elif front == rare:
        front, rare = -1, -1
        return "Successfully Removed"
    else:
        front += 1
        return "Successfully Removed"
def Display():
    global front, rare
    if front == rare:
        return "Queue is Empty"
    else:
        for i in range(front, rare+1):
            print(i, end=" ")
while True:
    print("1.Enqueue\n2.Dequeue\n3.Peep\n4.Exit")
    operation = int(input("Enter Which following operation do you want to Perform:"))
    if operation == 1:
        result = Enqueue()
        print(result)
    elif operation == 2:
        result_1 = Dequeue()
        print(result_1)
    elif operation == 3:
        result_3 = Display()
        print(result_3)
    else:
        exit()