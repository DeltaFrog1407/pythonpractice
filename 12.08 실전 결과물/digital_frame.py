import tkinter

pnum = 0
def photograph():
    global pnum
    canvas.delete("PH")
    canvas.create_image(521, 384, image=photo[pnum], tag="PH")
    pnum = pnum + 1
    if pnum >= len(photo):
        pnum = 0
    root.after(7000, photograph)

root = tkinter.Tk()
root.title("디지털 액자")
canvas = tkinter.Canvas(width=1024, height=768)
canvas.pack()
photo = [
    tkinter.PhotoImage(file="bg00.png"),
    tkinter.PhotoImage(file="bg01.png"),
    tkinter.PhotoImage(file="bg02.png"),
    tkinter.PhotoImage(file="bg03.png")
    ]
photograph()
root.mainloop()
