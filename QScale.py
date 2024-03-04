###QUANTUM SCALE NATURE
'''
CODE IS LICENSED UNDER CC BY-NC-ND
'''

import jdk
import jpype
import os


jdk.install('17', jre=True)

java_home = "/home/appuser/.jre/jdk-17.0.10+7-jre"
os.environ['JAVA_HOME'] = java_home
os.environ['PATH'] = f"{os.environ.get('PATH')}:{os.environ.get('JAVA_HOME')}/bin"

jvm_shared_library_path = os.path.join(java_home, "lib", "server", "libjvm.so")
jpype.startJVM(jvm_shared_library_path, "-Djava.awt.headless=false")

import py5
import numpy as np


sphere_radius = 260
rectangles_count = 169
ringcount = np.sqrt(rectangles_count)
qarray = np.random.randint(0, 17, size=rectangles_count)
w = 888
h = 888
R = 0


def setup():
    py5.size(w, h, py5.P3D)
    py5.smooth()
    global gwavesummer
    global mag 
    global yellowstonepng 
    yellowstonepng = py5.load_image('NaturalDataPlots/yellowstonesum.png')
    gwavesummer = py5.load_image('NaturalDataPlots/gwavesummer1.png')
    mag = py5.load_image('NaturalDataPlots/magsum.png')
    global matrix
    matrix = py5.get_matrix()

def draw():
    py5.set_matrix(matrix)
    py5.background(255)  
    py5.push_matrix()
    py5.translate(0,0, -3*w)
    draw_layers()
    py5.pop_matrix()
    py5.translate(py5.width / 2, py5.height / 2, -sphere_radius * 2)
    py5.rotate_y(py5.frame_count*.01)
    py5.rotate_x(py5.frame_count*.0111)
    py5.rotate_z(py5.frame_count*.013)
    draw_sphere()
    draw_rectangles()

    #FOR MAKING A GIF, SAVING FRAMES
    # if py5.frame_count <= 240:
    #         # Save the frame
    #         py5.save_frame(f"./GIF/frame_{py5.frame_count}.png")

def draw_sphere():
    py5.stroke(255)
    py5.no_fill()
    py5.sphere_detail(30)
    py5.sphere(sphere_radius)

def draw_rectangles():
    py5.no_stroke()
    for i, value in enumerate(qarray):
        color = py5.remap(value, 0, 17, 100, 255)
        qcolor = py5.remap(qrandom(), 0, 17, 100, 500)
        qfill = py5.color(65+color*qcolor, 53+color*qcolor, 72+color*qcolor)
        py5.color_mode(py5.HSB)
        qfill = py5.color(py5.remap(py5.hue(qfill)+30, 0, 360, 170, 330), py5.saturation(qfill), py5.brightness(qfill))
        if py5.is_mouse_pressed and py5.mouse_button == py5.LEFT:
            py5.fill(py5.hue(qfill)+9*value-72, py5.saturation(qfill)*.3-value, py5.brightness(qfill)*.5)
        else: 
            py5.fill(py5.hue(qfill), py5.saturation(qfill)*.4, py5.brightness(qfill)*.5)
            py5.color_mode(py5.RGB)
            py5.fill(py5.red(qfill)*np.random.uniform(1,(value+1)/17),py5.green(qfill)*np.random.uniform(1,(value+1)/17),py5.blue(qfill)*np.random.uniform(1,(value+1)/17))
        angle = py5.TWO_PI / ringcount * i
        x = sphere_radius * py5.cos(angle)
        y = sphere_radius * py5.sin(angle)
        z = 0
        rotate_angle = py5.atan2(y, x)
        py5.push_matrix()
        py5.translate(x, y, z)
        py5.rotate_z(rotate_angle)
        draw_rectangle(value)
        py5.pop_matrix()
        k=0
        if i%8 == 3 and i != 0:
            py5.rotate_y(py5.TWO_PI/ringcount)
            py5.rotate_x(py5.TWO_PI/(2*ringcount))
            k+=1

def draw_rectangle(value):
    py5.box(value*value, value+7, value+7)

def draw_layers():
    py5.image_mode(py5.CENTER)

    py5.push()
    py5.scale(1.6)
    py5.translate(-650,-650)
    py5.image(mag, w, h)
    py5.pop()

    py5.push()
    py5.scale(.54)
    py5.translate(-180,0)
    py5.image(gwavesummer, w, h)
    py5.pop()

    py5.push()
    py5.scale(3)
    py5.translate(-700,-600)
    py5.image(yellowstonepng, w, h)
    py5.pop() 

def qrandom():
    global R
    R+=1
    R = R%(rectangles_count-1)
    R = int(R)
    return qarray[R]

def mouse_pressed():
    py5.no_loop()  # Pause the draw loop 
    py5.set_matrix(matrix)
    py5.background(255)  
    py5.push_matrix()
    py5.translate(0,0, -3*w)
    draw_layers()
    py5.pop_matrix()
    if qrandom() > 8:
        py5.push_matrix()
        py5.translate(py5.width / 2, py5.height / 2, -sphere_radius * 2)
        py5.rotate_y(py5.PI)
        draw_sphere()
        draw_rectangles()
        py5.pop_matrix()
    py5.translate(py5.width / 2, py5.height / 2, -sphere_radius * 2)
    draw_sphere()
    draw_rectangles()

def mouse_released():
    py5.loop()


py5.run_sketch()
