import simplegui

frame_width = int(input("Initial width? "))
frame_height = int(input("Initial height? "))

# Shape visibility toggles
show_face1 = True
show_face2 = True
show_face3 = True
show_face4 = True

frame = None

# Toggle functions for each face
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

# Draw each face
def draw_face1(canvas, cx, cy, size):
    half_size = size / 2
    canvas.draw_circle((cx, cy), size, 5, "Yellow", "Yellow")
    canvas.draw_line((cx - half_size, cy - half_size*0.75), (cx + half_size, cy - half_size*0.75), 15, "black")
    canvas.draw_line((cx - half_size, cy + half_size*0.75), (cx + half_size, cy + half_size*0.75), 15, "black")
    canvas.draw_circle((cx - 25, cy - 25), 10, 10, "black", "black")
    canvas.draw_circle((cx + 25, cy - 25), 10, 10, "black", "black")
    

def draw_face2(canvas, cx, cy, size):
    canvas.draw_circle((cx, cy), size, 5, "#FA8072", "#FA8072")
    canvas.draw_circle([cx - 25, cy - 50], 10, 5, "Black", "White")
    canvas.draw_circle([cx + 25, cy - 50], 10, 5, "Black", "White")
    canvas.draw_line((cx - 50, cy - 50), (cx - 75, cy - 75), 2.5, "Black")
    canvas.draw_line((cx + 50, cy - 50), (cx + 75, cy - 75), 2.5, "Black")
    canvas.draw_polygon([(cx, cy + 25), (cx - 50, cy + 50), (cx + 50, cy + 50)], 5, "Black", "White")

def draw_face3(canvas, cx, cy, size):
    canvas.draw_circle((cx, cy), size, 10, "#FA8072", "#FA8872")
    canvas.draw_circle([cx - 25, cy - 50], 10, 10, "Black", "White")
    canvas.draw_circle([cx + 25, cy - 50], 10, 10, "Black", "White")
    canvas.draw_line((cx - 25, cy - 75), (cx - 50, cy - 50), 5, "Black")
    canvas.draw_line((cx + 25, cy - 75), (cx + 50, cy - 50), 5, "Black")
    canvas.draw_polygon([(cx, cy + 25), (cx - 50, cy + 50), (cx + 50, cy + 50)], 10, "Black", "White")

def draw_face4(canvas, cx, cy, size):
    canvas.draw_circle((cx, cy), size, 10, "#FFECA1", "#FFECA1")
    
    # Left eye (open)
    canvas.draw_circle([cx - 25, cy - 50], 10, 5, "Black", "White")
    
    # Right eye (wink, smaller or missing)
    canvas.draw_circle([cx + 25, cy - 50], 5, 5, "Black", "White")  # Smaller right eye to simulate wink
    
    # Eyebrows
    canvas.draw_line((cx - 25, cy - 60), (cx - 50, cy - 50), 5, "Black")  # Left eyebrow
    canvas.draw_line((cx + 25, cy - 60), (cx + 50, cy - 50), 5, "Black")  # Right eyebrow
    
    # Mouth
    canvas.draw_polygon([(cx, cy + 25), (cx - 50, cy + 50), (cx + 50, cy + 50)], 5, "Black", "White")

# Draw handler
def draw(canvas):
    quadrant_width = frame_width / 2
    quadrant_height = frame_height / 2

    if show_face1:
        # Place face1 in the top-left quadrant
        draw_face1(canvas, quadrant_width / 2, quadrant_height / 2, 100)
    if show_face2:
        # Place face2 in the top-right quadrant
        draw_face2(canvas, quadrant_width * 1.5, quadrant_height / 2, 100)
    if show_face3:
        # Place face3 in the bottom-left quadrant
        draw_face3(canvas, quadrant_width / 2, quadrant_height * 1.5, 100)
    if show_face4:
        # Place face4 in the bottom-right quadrant
        draw_face4(canvas, quadrant_width * 1.5, quadrant_height * 1.5, 100)

# Create frame and start the GUI
def create_frame():
    global frame
    frame = simplegui.create_frame("Four Faces", frame_width, frame_height)
    frame.set_canvas_background("white")
    frame.add_button("Bored", toggle_face1, 150)
    frame.add_button("Angry", toggle_face2, 150)
    frame.add_button("Happy", toggle_face3, 150)
    frame.add_button("Winking", toggle_face4, 150)
    frame.set_draw_handler(draw)
    frame.start()

create_frame()
