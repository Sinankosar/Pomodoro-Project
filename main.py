import tkinter as tk
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW ="#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=1
#-------------------------TIMER RESET-------------------#
def reset_but():
    check_marks.config(text=" ")
    count_down(0)

#--------------------------TIMER MECHANISM------------------------
def start_timer():
    global reps
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60
    
    if reps %2 !=0:
        count_down(work_sec)
        check_marks.config(text="✔️"*reps)
        reps+=1
        
    elif reps%2 ==0 and reps!=8:
        count_down(short_break_sec)
        reps+=1
    else:
        count_down(long_break_sec)
        
        reps=0
    
    
    
    
    
#----------------------------------COUNTDOWN MECHANISM-----------------------
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec<10:
        count_sec = f"0{count_sec}"
        
    if count_min<10:
      count_min = f"0{count_min}"
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count>0:
        window.after(1000,count_down,count-1)



#--------------------------------UI SETUP------------------------------------
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW, highlightthickness=0)


 


canvas = tk.Canvas(width=200, height=224,bg=YELLOW)
img = tk.PhotoImage(file="tomato.png")
canvas.create_image(102,114, image=img)
timer_text =canvas.create_text(100,130,text="00:00",fill="white",font= (FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)

timer_label = tk.Label(text="Timer",fg=GREEN,font= (FONT_NAME,50,"bold"))
timer_label.grid(column=1,row=0)


start_button = tk.Button(text="Start",command=start_timer)
start_button.grid(column=0,row=2)


reset_button = tk.Button(text="Reset",command=reset_but)
reset_button.grid(column=2,row=2)

check_marks = tk.Label(text="✔️",fg=GREEN,bg=YELLOW)
check_marks.grid(column=1,row=3)


   
window.mainloop()
""" from PIL import Image

# Görüntü dosyasını açma
image = Image.open("tomato.png")

# Görüntü boyutlarını alma
width, height = image.size

print(f"Genişlik: {width} piksel")
print(f"Yükseklik: {height} piksel")
 """