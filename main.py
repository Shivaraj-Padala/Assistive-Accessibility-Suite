from tkinter import *
from automation import COORDINATES
import threading
from server import app

root = Tk()
screen_width = str(root.winfo_screenwidth())
screen_height = str(root.winfo_screenheight())
root.geometry(screen_width+'x'+screen_height)
root.wm_state('zoomed')
root.title('Assistive Accessibility Suite')
root.iconbitmap('./static/assets/accessability.ico')
root.attributes('-alpha',0.4)
topKey = visibleKey = labelText = bottomKey = 0
bottomRow = (int(screen_height)-10)//25

threading.Thread(target=app.run).start()

for labelPosy in range(0, int(screen_height)-10, 25):
    for labelPosx in range(0, int(screen_width)-10, 29):
        labelText +=1
        if labelPosy == 0:
            topKey +=1
            COORDINATES[f'top {topKey}'] = (labelPosx+6, labelPosy)
        elif labelPosy == bottomRow*25:
            bottomKey +=1
            COORDINATES[f'bottom {bottomKey}'] = (labelPosx+6, labelPosy)
        else:
            visibleKey +=1
            COORDINATES[str(visibleKey)] = (labelPosx+6, labelPosy)
        Label(root,text=str(labelText),width=3,fg='red',font='Helvetica 8 bold').place(x=labelPosx,y=labelPosy)
        
if __name__ == "__main__":
    root.mainloop()