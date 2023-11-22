#inverted hollow pyramid stars by using for loop
def inverted_hollow_pyramid_stars(n):
    for i in range(n, 0, -1):
        if i == n or i == 1:
            print(" " * (n - i) + "* " * i)
        else:
            print(" " * (n - i) + "* " + "  " * (i - 2) + "*")

# Call the function with the desired number of rows
inverted_hollow_pyramid_stars(5)

#by using while loop
def inverted_hollow_pyramid_stars_while(n):
    i = n
    while i > 0:
        if i == n or i == 1:
            print(" " * (n - i) + "* " * i)
        else:
            print(" " * (n - i) + "* " + "  " * (i - 2) + "*")
        i -= 1

# Call the function with the desired number of rows
inverted_hollow_pyramid_stars_while(5)
