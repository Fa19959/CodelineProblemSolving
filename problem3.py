
print('Menu:')
print('1.Display a right-angle triangle of ones')
print('2.Display a Palindromic Triangle')
print('3.Help')
print('4.Exit')
choice=input('Enter your choice: ')

if choice == '1' :
    n= int( input("enter the number of lines: "))
    for i in range(n):
        for j in range(n-i-1):
            print("",end="")
        for j in range(i+1):
            print(1,end="")
        print()

elif choice == '2':
    n = int( input("enter the number of lines: "))
    for i in range(1, n+1):
        print([0, 1,11, 121, 12321, 1234321, 123454321][i])

elif choice == '3' :
     print('Help:\n A Palindromic Triangle is a triangular array of numbers where each row forms a palindrome.\nThe first few lines of a Palindromic Triangle are:\n1\n11\n121\n12321\n12321\n1234321\nYou can use this pattern to draw a Palindromic Triangle for any number of lines.')




elif choice == '4':
     print('Exiting the program.')
