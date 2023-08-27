# This program allows the user to choose various
# geometry calculations from a menu. This program
# imports the circle and rectangle modules.
import circle
import rectangle
import triangle

# Constants for the menu choices
AREA_CIRCLE_CHOICE = 1
CIRCUMFERENCE_CHOICE = 2
AREA_RECTANGLE_CHOICE = 3
PERIMETER_RECTANGLE_CHOICE = 4
AREA_TRIANGLE_WITH_BASE_AND_HEIGHT_CHOICE = 5
AREA_TRIANGLE_HERONS_FORMULA_CHOICE = 6
PERIMETER_TRIANGLE_USING_THREE_SIDES_CHOICE = 7
QUIT_CHOICE = 8

# The main function.
def main():
    # The choice variable controls the loop
    # and holds the user's menu choice.
    choice = 0

    while choice != QUIT_CHOICE:
        # display the menu.
        display_menu()

        # Ensure the user's choice is a valid integer within the menu options.
        while True:
            try:

                # Get the user's choice.
                choice = int(input('Enter your choices: '))

                if AREA_CIRCLE_CHOICE <= choice <= QUIT_CHOICE:
                    break  # Exit the inner while loop if choice is valid
                else:
                    print("Please choose a valid option from the menu.", '\n')
                    display_menu() # Display the menu again after an invalid input

            except ValueError:
                print("\nPlease enter a valid integer.", '\n')
                display_menu () # Display the menu again after an invalid input

        # Perform the selected action.
        if choice == AREA_CIRCLE_CHOICE:
            radius = float(input("Enter the circle's radius: "))
            print('The area is', circle.area(radius), '\n')
        elif choice == CIRCUMFERENCE_CHOICE:
            radius = float(input("Enter the circle's radius: "))
            print('The circumference is',
                circle.circumference(radius), '\n')
        elif choice == AREA_RECTANGLE_CHOICE:
            width = float(input("Enter the rectangle's width: "))
            length = float(input("Enter the rectangle's length: "))
            print('The area is', rectangle.area(width, length), '\n')
        elif choice == PERIMETER_RECTANGLE_CHOICE:
            width = float(input("Enter the rectangle's width: "))
            length = float(input("Enter the rectangle's length: "))
            print('The perimeter is',
                rectangle.perimeter(width, length), '\n')
        elif choice == AREA_TRIANGLE_WITH_BASE_AND_HEIGHT_CHOICE:
            base = float(input("Enter the triangle's base: "))
            height = float(input("Enter the triangle's height: "))
            print("Area (using base and height):",
                triangle.area_with_base_and_height(base, height), '\n')
        elif choice == AREA_TRIANGLE_HERONS_FORMULA_CHOICE:
            a = float(input("Enter the triangle's 'a' side: "))
            b = float(input("Enter the triangle's 'b' side: "))
            c = float(input("Enter the triangle's 'c' side: "))
            print("Area (using Heron's formula):", triangle.area_with_herons_formula(a, b, c), '\n')
        elif choice == PERIMETER_TRIANGLE_USING_THREE_SIDES_CHOICE:
            a = float(input("Enter the triangle's 'a' side: "))
            b = float(input("Enter the triangle's 'b' side: "))
            c = float(input("Enter the triangle's 'c' side: "))
            print("Perimeter:", triangle.perimeter(a, b, c), '\n')            
        elif choice == QUIT_CHOICE:
            print('Exiting the program...')
        else:
            print('Error: invalid selection.', '\n')
        
# The display_menu function displays a menu.
def display_menu():
    print('MENU')
    print('1) Area of a circle')
    print('2) Circumference of a circle')
    print('3) Area of a rectangle')
    print('4) Perimeter of a rectangle')
    print('5) Area of a triangle using base and height')
    print("6) Area of a triangle using Heron's formula (three sides)")
    print('7) Perimeter of a triangle using three sides')
    print('8) Quit')

# Call the main function.
main()
