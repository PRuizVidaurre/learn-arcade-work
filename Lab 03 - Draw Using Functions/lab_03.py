import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def draw_road():
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 2, 0, arcade.color.BLACK)
    arcade.draw_line(0, 150, 150, 150, arcade.color.WHITE, 15)
    arcade.draw_line(250, 150, 500, 150, arcade.color.WHITE, 15)
    arcade.draw_line(600, 150, 800, 150, arcade.color.WHITE, 15)


def draw_car(x, y):
    arcade.draw_point(x, y, arcade.color.BLACK, 5)

    arcade.draw_rectangle_filled(0+x, 125+y, 250, 100, arcade.csscolor.DARK_RED)
    arcade.draw_rectangle_filled(0+x, 150+y, 175, 150, arcade.csscolor.DARK_RED)
    arcade.draw_arc_filled(5+x, 160+y, 130, 150, arcade.csscolor.GOLDENROD, 360, 450)
    arcade.draw_arc_filled(-13+x, 160+y, 130, 150, arcade.csscolor.GOLDENROD, 90, 180)
    arcade.draw_arc_filled(-125 + x, 125 + y, 50, 100, arcade.csscolor.DARK_RED, 90, 270)
    arcade.draw_arc_filled(115 + x, 125 + y, 80, 100, arcade.csscolor.DARK_RED, 270, 450)
    arcade.draw_arc_filled(0 + x, 225 + y, 175, 80, arcade.csscolor.DARK_RED, 0, 180)

    arcade.draw_circle_filled(50, 550, 60, arcade.csscolor.ANTIQUE_WHITE)
    arcade.draw_circle_filled(-70+x, 200, 45, arcade.csscolor.GRAY)
    arcade.draw_circle_filled(60 + x, 200, 45, arcade.csscolor.GRAY)
    arcade.draw_circle_filled(-70 + x, 200, 20, arcade.csscolor.BLACK)
    arcade.draw_circle_filled(60 + x, 200, 20, arcade.csscolor.BLACK)

def on_draw(delta_time):
    arcade.start_render()

    draw_road()
    draw_car(on_draw.car_x, 140)

    on_draw.car_x += 5

on_draw.car_x = 0

def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.DARK_BLUE)

    arcade.schedule(on_draw, 1/60)
    arcade.run()

main()