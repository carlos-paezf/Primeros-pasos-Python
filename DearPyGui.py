from dearpygui.dearpygui import *


def save_callback(sender, data):
    print("Save Clicked")


add_text("Hello world")
add_slider_float("float")
add_slider_int("int")
add_color_edit3("Color")
add_checkbox("Click")
add_button("Save", callback=save_callback)
set_main_window_title("Python Learning")
start_dearpygui()
