#by using for loop
def inverted_right_triangle(n):
    for i in range(n, 0, -1):
        for j in range(i):
            print("* ", end="")
        print()

# Call the function with the desired size
inverted_right_triangle(5)

#by using while loop
def inverted_right_triangle_while(n):
    i = n
    while i > 0:
        j = 0
        while j < i:
            print("* ", end="")
            j += 1
        print()
        i -= 1

# Call the function with the desired size
inverted_right_triangle_while(5)

