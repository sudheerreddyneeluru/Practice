#hollow pyramid patterns by using for loop
def hollow_pyramid_stars(n):
    for i in range(1, n + 1):
        if i == 1 or i == n:
            print(" " * (n - i) + "* " * i)
        else:
            print(" " * (n - i) + "* " + "  " * (i - 2) + "*")

# Call the function with the desired number of rows
hollow_pyramid_stars(5)


#by using while loop
def hollow_pyramid_stars_while(n):
    i = 1
    while i <= n:
        if i == 1 or i == n:
            print(" " * (n - i) + "* " * i)
        else:
            print(" " * (n - i) + "* " + "  " * (i - 2) + "*")
        i += 1

# Call the function with the desired number of rows
hollow_pyramid_stars_while(5)
