#!/usr/bin/env python3
'''
now in an actual program error handling is 
lets say REALLY REALLY IMPORTANT, but in these
basic excersises im going to lazy, as intened.

in this one the model solution prompts for dimensions inside the 
shape_area functions, which i think is better than how i did this.
i should know better and i do know, but yes, keeping your main function 
clean is good practice.
'''
import math

def triangle_area(base, height):
    return base*height/2

def rectangle_area(width, height):
    return width*height

def circle_area(radius):
    return math.pi*radius**2

def area_print(area):   #this feels extra, but its used 3 times so i guess itd be good practice
    print(f"The area is {area:6f}")

def main():
    while True:
        shape = input("Choose a shape (triangle, rectangle, circle): ")

        if shape.lower() == "circle":
            radius = int(input("Give radius of the circle: "))
            area = circle_area(radius)
            area_print(area)

        elif shape.lower() == "triangle":
            base = int(input("Give base of the triangle: "))
            height = int(input("Give height of the triangle: "))
            area = triangle_area(base, height)
            area_print(area)

        elif shape.lower() == "rectangle":
            width = int(input("Give width of the rectangle: "))
            height = int(input("Give height of the rectangle: "))
            area = rectangle_area(base, height)
            area_print(area)            
        
        elif shape == "":
            break

        else:
            print("Unknown shape!")


if __name__ == "__main__":
    main()
