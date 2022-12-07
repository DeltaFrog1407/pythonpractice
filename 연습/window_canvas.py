import tkinter
root = tkinter.Tk()
root.title("캔버스")
canvas = tkinter.Canvas(root, width=1600, height=900, bg="white")
canvas.pack()
gazou = tkinter.PhotoImage(file='박지성3.png')
canvas.create_image(800, 450, image=gazou)
root.mainloop()
