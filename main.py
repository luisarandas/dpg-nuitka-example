

# luis arandas 16-02-2023
# very simple two button dpg project compiling for nuitka on all platforms
# supposed to be used as a fork to other app projects

import os

current_dir = os.path.dirname(os.path.abspath(__file__))
dist_folder = current_dir + os.sep + "dist"

if not os.path.exists(dist_folder):
    os.mkdir(dist_folder)

# setup application

import dearpygui.dearpygui as dpg

def save_callback():
    print("Save Clicked")

dpg.create_context()
dpg.create_viewport(title=' ', width=350, height=200, resizable=False)

def dpg_exit_callback():
    dpg.stop_dearpygui()
dpg.set_viewport_pos([0,0])
dpg.setup_dearpygui()

with dpg.window(tag="mainwindow", pos=(0,0)):
    dpg.add_text("simple dpg nuitka example")
    dpg.add_button(label="Save", callback=save_callback)
    dpg.add_input_text(label="string")
    dpg.add_slider_float(label="float")

dpg.show_viewport()
dpg.set_exit_callback(dpg_exit_callback)
dpg.set_global_font_scale(1)
# dpg.maximize_viewport()
dpg.set_primary_window("mainwindow", True)
dpg.set_viewport_resizable(False)
dpg.start_dearpygui()
dpg.destroy_context()