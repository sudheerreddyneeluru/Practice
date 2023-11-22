#by using for loop for pyramid patterns
def pyramid_stars(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "* " * i)

# Call the function with the desired number of rows
pyramid_stars(5)

#by using while loop
def pyramid_stars_while(n):
    i = 1
    while i <= n:
        print(" " * (n - i) + "* " * i)
        i += 1

# Call the function with the desired number of rows
pyramid_stars_while(5)
