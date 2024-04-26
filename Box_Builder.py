import arcade
SW = 600
SH = 600
class Box:
    def __init__(self, left, right, top, bottom, dx, dy, col):
        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom
        self.dx = dx
        self.dy = dy
        self.col = col

    def draw_box(self):
        arcade.draw_lrtb_rectangle_filled(self.left, self.right, self.top, self.bottom, self.col)

    def update_box(self):
        self.top += self.dy
        self.bottom += self.dy

        self.left += self.dx
        self.right += self.dx

        #bounce off edge of screen

        if self.left <= 30:
            self.dx *= -1
            self.col = arcade.color.RED
        elif self.right >= SW - 30:
            self.dx *= -1
            self.col = arcade.color.BLUE
        if self.top >= SH - 30:
            self.dy *= -1
            self.col = arcade.color.YELLOW
        elif self.bottom <= 30:
            self.dy *= -1
            self.col = arcade.color.GREEN

