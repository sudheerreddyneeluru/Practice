#using for loop
#square pattern
def solid_square(n):
    for i in range(n):
        for j in range(n):
            print("* ", end="")
        print()

# Call the function with the desired size
solid_square(5)
#by using while loop
def solid_square_while(n):
    i = 0
    while i < n:
        j = 0
        while j < n:
            print("* ", end="")
            j += 1
        print()
        i += 1

# Call the function with the desired size
solid_square_while(5)


#hollow square pattern by using for loop
def hollow_square(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                print("* ", end="")
            else:
                print("  ", end="")
        print()

# Call the function with the desired size
hollow_square(5)

#by using for loop
def hollow_square_while(n):
    i = 0
    while i < n:
        j = 0
        while j < n:
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                print("* ", end="")
            else:
                print("  ", end="")
            j += 1
        print()
        i += 1

# Call the function with the desired size
hollow_square_while(5)
