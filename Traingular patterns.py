#right angle traingle by for loop
def right_triangle(n):
    for i in range(1, n + 1):
        for j in range(i):
            print("* ", end="")
        print()

# Call the function with the desired size
right_triangle(5)
#by using while loop
def right_triangle_while(n):
    i = 1
    while i <= n:
        j = 0
        while j < i:
            print("* ", end="")
            j += 1
        print()
        i += 1

# Call the function with the desired size
right_triangle_while(5)

