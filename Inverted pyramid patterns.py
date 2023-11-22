#by using for loops
def inverted_pyramid_stars(n):
    for i in range(n, 0, -1):
        print(" " * (n - i) + "* " * i)

# Call the function with the desired number of rows
inverted_pyramid_stars(5)

#by using while loop
def inverted_pyramid_stars_while(n):
    i = n
    while i > 0:
        print(" " * (n - i) + "* " * i)
        i -= 1

# Call the function with the desired number of rows
inverted_pyramid_stars_while(5)

