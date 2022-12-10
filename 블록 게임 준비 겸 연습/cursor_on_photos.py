import tkinter

cursor_x = 0
cursor_y = 0
mouse_x = 25
mouse_y = 25

def mouse_move(e):
    global mouse_x, mouse_y
    mouse_x = e.x
    mouse_y = e.y

def game_main():
    global cursor_x, cursor_y
    if 24 <= mouse_x and mouse_x < 24 + 72 * 8 and 24 <= mouse_y and mouse_y < 24 + 72 * 10:
        cursor_x = int((mouse_x - 24) / 72)
        cursor_y = int((mouse_y - 24) / 72)
    cvs.delete("CURSOR")
    cvs.create_image(cursor_x*72 + 60, cursor_y*72 + 60, image=cursor, tag="CURSOR")
    root.after(1, game_main)

neko = [
    [7, 7, 0, 0, 0, 0, 7, 7],
    [7, 7, 0, 0, 2, 0, 7, 7],
    [0, 0, 3, 0, 2, 1, 0, 0],
    [0, 0, 4, 3, 2, 1, 0, 0],
    [0, 5, 4, 3, 2, 1, 0, 0],
    [0, 5, 4, 3, 0, 6, 0, 0],
    [0, 5, 4, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [7, 7, 0, 0, 0, 0, 7, 7],
    [7, 7, 1, 2, 3, 4, 7, 7]
    ]

def draw_neko():
    for y in range(10):
        for x in range(8):
            if neko[y][x] > 0:
                cvs.create_image(x * 72 + 60, y * 72 + 60, image=img_neko[neko[y][x]])


root = tkinter.Tk()
root.title("배치한 그림 위 커서 표시")
root.resizable(False, False)
cvs = tkinter.Canvas(root, width=912, height=768)
cvs.pack()
root.bind("<Motion>",mouse_move)
bg = tkinter.PhotoImage(file = "neko_bg.png")
cursor = tkinter.PhotoImage(file="neko_cursor.png")
img_neko = [
    None,
    tkinter.PhotoImage(file="neko1.png"),
    tkinter.PhotoImage(file="neko2.png"),
    tkinter.PhotoImage(file="neko3.png"),
    tkinter.PhotoImage(file="neko4.png"),
    tkinter.PhotoImage(file="neko5.png"),
    tkinter.PhotoImage(file="neko6.png"),
    tkinter.PhotoImage(file="neko_niku.png")
    ]

cvs.create_image(456, 384, image=bg)
draw_neko()
game_main()
root.mainloop
