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
    canvas.draw_circle((cx/2, cy/2), cx/2 - 50, 5, "#FA8072", "#FA8072")
    canvas.draw_circle([cx/2.75, cy/2 - 100], 10, 5, "Black", "White")
    canvas.draw_circle([cx - cx/2.75, cy/2 - 100], 10, 5, "Black", "White")
    canvas.draw_line((cx/3, cy/2 - 150),(cx/3 + 50, cy/2 - 125), 2.5, "Black")
    canvas.draw_line((cx - cx/3, cy/2 - 150),(cx - cx/3 - 50, cy/2 - 125), 2.5, "Black")
    canvas.draw_polygon([(cx/2, cy - cy/4), (cx/2 - 50, cy - cy/4 + 25), 
                        (cx/2 - 10, cy - cy/4 - 30), (cx/2 + 10, cy - cy/4 - 30), 
                        (cx/2 + 50, cy - cy/4 + 25)], 5, "Black", "White")
    canvas.draw_line((cx/2 - 30, cy - cy/4 - 10), (cx/2 + 30, cy - cy/4 - 10),2.5, "Black")
def draw_face3(canvas, cx, cy, size):
    #draw the shape
# Function to draw the happy face
def draw_face1(canvas, cx, cy, size):
    # Face outline (salmon-colored circle)
    canvas.draw_circle((cx, cy), size, 10, "#FA8072", "#FA8872")
    
    # Left eye (white circle with black border)
    canvas.draw_circle((cx - size / 4, cy - size / 4), size / 10, 2, "Black", "White")
    
    # Right eye (white circle with black border)
    canvas.draw_circle((cx + size / 4, cy - size / 4), size / 10, 2, "Black", "White")
    
    # Left eyebrow (curved upward for a happy expression)
    canvas.draw_line((cx - size / 3, cy - size / 3), 
                     (cx - size / 5, cy - size / 3 - 10), 3, "Black")
    
    # Right eyebrow (curved upward for a happy expression)
    canvas.draw_line((cx + size / 3, cy - size / 3), 
                     (cx + size / 5, cy - size / 3 - 10), 3, "Black")
    
    # Mouth outline (smiling curve with a polygon for the lips)
    canvas.draw_polygon([(cx - size / 4, cy + size / 4),
                         (cx - size / 8, cy + size / 3),
                         (cx + size / 8, cy + size / 3),
                         (cx + size / 4, cy + size / 4)],
                        2, "Black", "White")
    
    # Smile line (adding a gentle smile curve under the lips)
    canvas.draw_line((cx - size / 6, cy + size / 4 + 5), 
                     (cx + size / 6, cy + size / 4 + 5), 3, "Black")



def draw_face4(canvas, cx, cy, size):
    #draw the shape
    half_size = size / 2
    canvas.draw_circle((width/2, height/2), width/2 - 50, 10, "#FFECA1", "#FFECA1")
        canvas.draw_circle((209, 215), 41, 2, "black", "black")
        canvas.draw_line((width - width/4, height/2 - 134),(width - width/3 - 50, height/2 - 125), 5, "Black")
        canvas.draw_line((width - width/4, height/2 - 200),(width - width/3 - 50, height/2 - 125), 5, "Black")
        canvas.draw_line((width - width/4, height/1.2 - 150),(width - width/1.9 - 50, height/1.2 - 150), 5, "Black")
        canvas.draw_line((width - width/1.5, height/1.3 - 150),(width - width/1.9 - 50, height/1.2 - 150), 5, "Black")
        canvas.draw_line((width - width/4, height/1.2 - 150),(width - width/7 - 50, height/1.4 - 150), 5, "Black") 
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
    frame = simplegui.create_frame("Four Faces", frame_width, frame_height)
    frame.set_canvas_background("white")
    frame.add_button("Bored", toggle_face1, 150)
    frame.set_draw_handler(draw)
    frame.start()
    
create_frame()
