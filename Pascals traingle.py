#by using for loop
def generate_pascals_triangle(n):
    for i in range(n):
        # Each row starts with 1
        coefficient = 1
        for j in range(1, i + 2):
            print(coefficient, end=" ")
            coefficient = coefficient * (i + 1 - j) // j
        print()

# Call the function with the desired number of rows
generate_pascals_triangle(5)

#by using while loop
def generate_pascals_triangle_while(n):
    i = 0
    while i < n:
        coefficient = 1
        j = 0
        while j < i + 1:
            print(coefficient, end=" ")
            coefficient = coefficient * (i - j) // (j + 1)
            j += 1
        print()
        i += 1

# Call the function with the desired number of rows
generate_pascals_triangle_while(5)
