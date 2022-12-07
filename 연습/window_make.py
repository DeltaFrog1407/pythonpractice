import tkinter
import tkinter.font

def click_btn():
    button["font"] = "궁서체", 24
root = tkinter.Tk()
root.title("화이팅")
root.geometry("800x600")
button = tkinter.Button(root, text="아무것도 없는 버튼",
font=("궁서체", 24), command=click_btn)
button.place(x=200, y=100)
root.mainloop()
