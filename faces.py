#group project

import simplegui

frame_width =  int(input("Initial width?"))
frame_height =  int(input("Initial height?"))

# Shape visibility toggles
show_face1 = True
show_face2 = True
show_face3 = True
show_face4 = True

frame = None # Global Reference to the frame

def toggle_face1():
    global show_face1
    show_face1 = not show_face1
def toggle_face2():
    global show_face2
    show_face2 = not show_face2
def toggle_face3():
    global show_face3
    show_face3 = not show_face3
def toggle_face4():
    global show_face4
    show_face4 = not show_face4


def draw_face1(canvas, cx, cy, size):
    half_size = size / 2
    canvas.draw_circle((cx/2, cy/2), cx/2 - size, 5, "Yellow", "Yellow")
    canvas.draw_line((cx/4.25, cy/3), (cx/2.25, cy/3), 15, "black")
    canvas.draw_line((cx/1.75, cy/3), (cx/1.25, cy/3), 15, "black")
    canvas.draw_line((cx/3, cy/2), (cx*0.66, cy/2), 15, "black")
    canvas.draw_circle((cx/3, cy*0.366), cx/8 - half_size, 10, "black", "black")
    canvas.draw_circle((cx/1.5, cy*0.366), cx/8 - half_size, 10, "black", "black")
    canvas.draw_circle((cx/3, cy/2), cx/8 - half_size, 10, "black", "black")
    canvas.draw_circle((cx/1.5, cy/2), cx/8 - half_size, 10, "black", "black")


def draw_face2(canvas, cx, cy, size):
    #draw the shape
   canvas.draw_circle((width/2, height/2), width/2 - 50, 10, "Yellow", "Yellow")
        # Eyes
        canvas.draw_circle([width/2 - 100, height/2 - 100], 30, 2, "Black", "White")
        canvas.draw_circle([width/2 + 100, height/2 - 100], 30, 2, "Black", "White")
        # Mouth (Confused)
        canvas.draw_polygon([(width/2 - 100, height/2 + 50), (width/2 - 50, height/2 + 80), 
                             (width/2 + 50, height/2 + 80), (width/2 + 100, height/2 + 50)], 5, "Black", "White")

def draw_face3(canvas, cx, cy, size):
    #draw the shape
    half_size = size / 2
    canvas.draw_polygon([(cx, cy - half_size),
                        (cx - half_size, cy + half_size), 
                        (cx + half_size, cy + half_size)],
                        2, "Blue", "blue") #blue triangle
def draw_face4(canvas, cx, cy, size):
    #draw the shape
    half_size = size / 2
    canvas.draw_polygon([(cx, cy - half_size),
                        (cx - half_size, cy + half_size), 
                        (cx + half_size, cy + half_size)],
                        2, "Blue", "blue") #blue triangle
    
def draw(canvas):
    quadrant_width = frame_width/2
    quadrant_height = frame_height/2
    
    if show_face1:
            draw_face1(canvas, quadrant_width * 1.5, frame_height - quadrant_height * 1.5, 100) #face1 in bottom left
    if show_face2:
            draw_face2(canvas, quadrant_width / 2, frame_height - quadrant_height / 2, 100) #face1 in bottom left
    if show_face3:
            draw_face3(canvas, quadrant_width / 2, frame_height - quadrant_height * 1.5, 100) #face1 in bottom left
    if show_face4:
            draw_face4(canvas, quadrant_width *1.5 , frame_height - quadrant_height / 2, 100) #face1 in bottom left
            
            
def create_frame():
    global frame
    frame = simplegui.create_frame("CFU #17", frame_width, frame_height)
    frame.set_canvas_background("green")
    frame.add_button("Bored", toggle_face1, 150)
    frame.set_draw_handler(draw)
    frame.start()
    
create_frame()
