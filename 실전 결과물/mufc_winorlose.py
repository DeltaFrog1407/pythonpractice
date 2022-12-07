import tkinter
import random

def click_btn():
    label["text"] = random.choice(["승리", "패배", "무승부"])
    if label["text"] == "승리" or label["text"] == "패배":
        label["font"] = "System", 100
        label.place(x=510, y=60)
    else:
        label["font"] = "System", 80
        label.place(x = 490, y = 80)
    label.update()
root = tkinter.Tk()
root.title("맨유 승패 예측 프로그램")
root.resizable(False, False)
canvas = tkinter.Canvas(root, width=800, height=450)
canvas.pack()
background = tkinter.PhotoImage(file="박지성3.png")
canvas.create_image(400, 225, image = background)
label = tkinter.Label(root, text="-----", font=("System", 100), bg="white")
label.place(x=600, y=60)
button = tkinter.Button(root, text="결과 예측", font=("System", 36),
command=click_btn, fg ="black")
button.place(x=520, y = 270)
root.mainloop()
