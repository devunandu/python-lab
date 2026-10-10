import numpy as np
def create_ones_array():
    shape=tuple(map(int,input("enter dimensions separated by space (e.g 2 3 for 2*3):").split()))
    arr = np.ones(shape)
    print("array filled with 1,s:\n",arr)

def find_max_min():
    arr=np.array(list(map(int,input("enter array elements separated by space: ").split())))
    print("array: ",arr)
    print("maximum value",np.max(arr))
    print("minimum value",np.min(arr))

def dot_product():
    arr1=np.array(list(map(int,input("enter elements of first array: ").split())))
    arr2=np.array(list(map(int,input("enter elements of second array: ").split())))
    if arr1.size!=arr2.size:
        print("array must be of the same size for dot product. ")
    else:
        print("dot product:",np.dot(arr1,arr2))

def reshape_array():
    arr= np.array(list(map(int,input("enter elements of 1-D array: ").split())))
    rows=int(input("enter number of rows: "))
    cols=int(input("enter number of columns: "))
    if rows * cols!=arr.size:
        print("cannot reshape array: total elements do not match")
    else:
        reshaped=arr.reshape((rows,cols))
        print("reshaped 2-D array: \n",reshaped)

while True:
    print("\nMenu:")
    print("a. Create an array filled with 1's")
    print("b. Find maximum and minimum values from an array")
    print("c. Dot product of 2 arrays")
    print("d. Reshape a 1-D array to 2-D array")
    print("e. Exit")

    choice = input("Enter your choice (a/b/c/d/e): ").lower()

    if choice == 'a':
        create_ones_array()
    elif choice == 'b':
        find_max_min()
    elif choice == 'c':
        dot_product()
    elif choice == 'd':
        reshape_array()
    elif choice == 'e':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
