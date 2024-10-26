import tkinter as tk
from shape_objects_editor import ShapeObjectsEditor

if __name__ == "__main__":
    root = tk.Tk()

    toolbar = tk.Frame(root)
    toolbar.pack(side=tk.TOP, fill=tk.X)

    canvas = tk.Canvas(root, bg="white")

    shapes = [None] * 112

    app = ShapeObjectsEditor(root, canvas, shapes, toolbar)
    root.mainloop()
