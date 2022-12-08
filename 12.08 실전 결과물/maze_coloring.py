import tkinter
import tkinter.messagebox

key = ""
def key_down(e):
    global key
    key = e.keysym
def key_up(e):
    global key
    key = ""

mx = 1
my = 1
floor = 0
def main_proc():
    global mx, my, floor
    if key == "Shift_L" and floor > 1:
        canvas.delete("FLOOR")
        mx = 1
        my = 1
        floor = 0
        for y in range(7):
            for x in range(10):
                if maze[y][x] == 2:
                    maze[y][x] = 0
    if key == "Up" and maze[my - 1][mx] == 0:
        my = my - 1
    if key == "Down" and maze[my + 1][mx] == 0:
        my = my + 1
    if key == "Left" and maze[my][mx - 1] == 0:
        mx = mx - 1
    if key == "Right" and maze[my][mx + 1] == 0:
        mx = mx + 1
    if maze[my][mx] == 0:
            maze[my][mx] = 2
            floor = floor + 1
            canvas.create_rectangle(mx*80, my*80, mx*80 + 79, my*80 + 79, fill="yellow", width=0, tag ="FLOOR")
    canvas.delete("MYCHR")
    canvas.create_image(mx*80 + 40, my*80 + 40, image=img, tag="MYCHR")
    if floor == 30:
        canvas.update()
        tkinter.messagebox.showinfo("축하합니다!", "호날두는 성공적으로 한붓그리기를 마쳤습니다!")
    else:
        root.after(100, main_proc)

root = tkinter.Tk()
root.title("호날두의 한붓그리기(왼쪽 시프트로 다시 시작)")
root.bind("<KeyPress>", key_down)
root.bind("<KeyRelease>", key_up)
canvas = tkinter.Canvas(width=800, height=560, bg="white")
canvas.pack()
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]
for y in range(7):
    for x in range(10):
        if maze[y][x] == 1:
            canvas.create_rectangle(x*80, y*80, x*80+79, y*80+79, fill = "red", width=0)

img = tkinter.PhotoImage(file="한반두.png")
canvas.create_image(mx*80+40, my*80 + 40, image=img, tag="MYCHR")
main_proc()
root.mainloop()
