import shape_calculator
import circleArea
import triangleArea


class main_program():
    def __init__(self):
        pass

    def get_input(self):
        print("Get Input")

    def callRectangle(self):
        rectangle = shape_calculator.Rectangle(5, 10)
        print(f"Area of Rectangle is : {rectangle.get_area()}" )
        rectangle.set_width(3)
        print(f"Perimater of Rectangle is : {rectangle.get_perimeter()}" )
        print(f"Length of Diagonal is : {rectangle.get_diagonal()}")


    def callSquare(self):
        square = shape_calculator.Square(9)
        print(f"Area of Square is : {square.get_area()}")
        print(f"Perimeter of Square is : {square.get_perimeter()}")
        square.set_side(4)
        print(f"Length of Diagonal is : {square.get_diagonal()}" )

    def call_circle(self):
        circle = circleArea.circle(3)
        print(f"Area of Circle is : {circle.area()}" )
        print(f"Perimeter of Circle is : {circle.perimeter()}")

    def calltriangle(self):
        triangle = triangleArea.triangle(5, 5, 3, 10, 12)
        print(f"Area of Triangle by giving all 3 sides : {triangle.area_by_side()}")
        print(f"Area of Triangle by giving Height and Base : {triangle.areaByHeightBase()}")

    def callparallelogram(self):
        parallelogram = shape_calculator.parallelogram(5, 5)
        print(f"Area of parallelogram is : {parallelogram.get_area()}" )
        print(f"Perimeter of parallelogram is : {parallelogram.get_perimeter()}")

    def callreg_polygon(self):
        reg_polygon = shape_calculator.reg_polygon(3, 3)
        print(f"Area of Regular Polygon is :  {reg_polygon.get_area()}" )
        print(f"Perimeter of Regular Ploygon is {reg_polygon.get_perimeter()}")

    def errorhandler(self):
        print("Invalid Input")

    def menu(self):
        print("**** AREA AND PERIMETER CALCULATOR ****")
        print("\t 1: Rectangle")
        print("\t 2: Square")
        print("\t 3: circle")
        print("\t 4: triangle")
        print("\t 5: parallelogram")
        print("\t 6: regular_polygon")
        choice = int(input("Enter choice "))

        operations = {
            1: self.callRectangle,
            2: self.callSquare,
            3: self.call_circle,
            4: self.calltriangle,
            5: self.callparallelogram,
            6: self.callreg_polygon
        }

        operations.get(choice, self.errorhandler)()


a = main_program()
a.menu()
