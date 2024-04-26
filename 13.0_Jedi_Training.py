'''
# 13.0 Jedi Training (10pts)  Name:________________

 BOX CLASS LIBRARY  (5pts)
 -----------------
For this test, take your 30 box program and remove the Box Class into a seperate file called Box_Builder.py. Now just
import the Box Class into your main program. Use if __name__ =="__main__":

'''
import random
from Box_Builder import *


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.ASH_GREY)
        self.box_list = []
        for i in range(30):
            left = random.randint(30, 520)
            right = left + random.randint(10, 50)
            bottom = random.randint(30, 520)
            top = bottom + random.randint(10, 50)
            x = random.randint(-5, 5)
            y = random.randint(-5, 5)
            if x == 0 or y == 0:
                x = random.randint(-5, 5)
                y = random.randint(-5, 5)
            self.box = Box(left, right, top, bottom, x, y, arcade.color.BLACK)
            self.box_list.append(self.box)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_rectangle_filled(585, 300, 30, 600, arcade.color.BLUE)
        arcade.draw_rectangle_filled(15, 300, 30, 600, arcade.color.RED)
        arcade.draw_rectangle_filled(300, 585, 600, 30, arcade.color.YELLOW)
        arcade.draw_rectangle_filled(300, 15, 600, 30, arcade.color.GREEN)
        for box in self.box_list:
            box.draw_box()

    def on_update(self, dt):
        for box in self.box_list:
            box.update_box()


def main():
    window = MyGame(SW, SH, "30 Boxes")
    arcade.run()


if __name__ == "__main__":
    main()


'''
FUNCTIONS LIBRARY  (5pts)
 -----------------
Paste all the functions that you submitted in the Functions chapter into a single file called my_library.py.
This should only include all of the (defs), not the inputs and function calls. 
Create a main program called my_program.py which will import the my_library module. 
In this program you will put the inputs and function calls. 
Use the import * so you don't have to use namespaces for each function call. 
Use if __name__ =="__main__":
You can just demonstrate this to your instructor when you have completed both of these tasks.
'''


# import my_functions
# import other_functions

# from my_functions import *
#
#
# def main():
#     yoda()
#
#
# print("The __name__ variable is:", __name__)
#
# if __name__ == "__main__":
#     main()
#     print("Jedi Training is being run directly")
# else:
#     print("Jedi Training is being imported")