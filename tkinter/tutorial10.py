## Canvas widget creation
import tkinter as tk

root = tk.Tk()

canvas_width = 600
canvas_height = 400

root.geometry(f"{canvas_width}x{canvas_height}")
root.title("MY GUI")

canvas_widget = tk.Canvas(root, width=canvas_width, height=canvas_height)
canvas_widget.pack()

# The line starts form x1,y1 to x2,y2
canvas_widget.create_line(0, 200, 600, 0, fill='red')

# Co-ordinates starts from top x, y to botton right left
canvas_widget.create_rectangle(3, 5, 400, 300, fill='blue')


# Create a text, The co-ordinates are center coordinate of the text
canvas_widget.create_text(200, 200, text="Python")

# The oval is created inside an rectangle hence we are passing in the coordinates.
canvas_widget.create_oval(300, 300, 200, 200)


root.mainloop()