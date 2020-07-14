class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height

    def set_width(self,width):
        self.width=width
    
    def set_height(self,height):
        self.height=height
    
    def get_area(self):
        return(self.width*self.height)

    def get_perimeter(self):
        return(2*(self.width+self.height))

    def get_diagonal(self):
        return((self.width**2+self.height**2)**.5)

    def get_picture(self):
        pattern=''
        if self.width > 50 or self.height >50:
            return("Too big for picture.")
        else:
            for i in range(self.height):
                pattern+="*"*self.width+'\n'
        return(pattern)

    def get_amount_inside(self,shape):
        vertical = self.width//shape.width
        horizontal = self.height//shape.height
        amount = vertical * horizontal
        return amount

    def __str__(self):
        string = "Rectangle(width={}, height={})".format(self.width, self.height)
        return string


class Square(Rectangle):
    def __init__(self,side):
        self.side=side
        self.width=side
        self.height=side

    def __str__(self):
        return("Square(side={})".format(self.width, self.height))

    def set_side(self, side):
        self.height = side
        self.width = side

rect=Rectangle(3,6)
rect.set_width(7)
rect.set_height(3)
actual = rect.get_picture()
expected = "*******\n*******\n*******\n"
print(actual==expected)