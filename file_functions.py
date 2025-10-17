from tkinter import *
from widget_registry import get_widget
from tkinter.filedialog import asksaveasfilename,askopenfilename
import sys
import os

file_path=None
save_location=None
font_name='Agave Nerd Font' #default font
font_size=21 #default font size
color_hex_bg_code='#FFFFED' #default bg color
color_hex_fg_code='black' #default fg color
rep_word=None

def update_title(root):
    global file_path
    if file_path:
        filename = os.path.basename(file_path)
        root.title(f"『Tk』Ed - {filename}")
    else:
        root.title("『Tk』Ed - Untitled")


def Fetch_file_path(root, event=None):
    T=get_widget('text_widget') 
    def Open_file(file_path):
        if file_path:
            with open(file_path, "r") as fileobj:
                content = fileobj.read()
                print("file read succesfully")
                T.delete("1.0",END)
                T.insert("1.0",content)
                update_title(root)
                notification("Opened file successfully",700)
                

    global file_path
    if(len(sys.argv) == 2):
        file_path = sys.argv[1]
        Open_file(file_path)

    else:
        print("opening an existing file")
        file_path = askopenfilename()
        Open_file(file_path)

def Save(root, event=None):
    #print("a")
    global file_path
    T=get_widget('text_widget')
    # file_path = askopenfilename()
    print("Saving the file")
    if not file_path:
        saveAs(root)
    else:
        with open(file_path,"w") as file1:
            t = T.get("1.0",END)
            file1.write(t)
        print(f"File saved to location: {file_path}")
        update_title(root)
        notification("File saved successfully",700)
        

def saveAs(root, event=None):
    T=get_widget('text_widget')
    t=T.get("1.0","end-1c")
    global save_location
    global file_path
    print("Save As")
    save_location=asksaveasfilename()
    if save_location:
        with open(save_location,"w+") as file1:
            file1.write(t)
            print(f"File saved to location: {save_location}")
        file_path=save_location
        update_title(root)
        notification("File saved successfully",700)
        
    else:
        print("enter save location")


def notification(message,disp_time):
    root_destroy=Tk()
    root_destroy.geometry("300x100")

    root_destroy.attributes('-topmost',True)
    root_destroy.overrideredirect(True)

    notification_label=Label(root_destroy,text=message,font=("Helvetica",12,"bold"),fg="white",bg="black",padx=10,pady=10)
    notification_label.pack(expand=True,fill='both')

    root_destroy.update_idletasks()
    width=root_destroy.winfo_width()
    height=root_destroy.winfo_height()
    x = (root_destroy.winfo_screenwidth() // 2) - (width // 2)
    y=50
    root_destroy.geometry(f'{width}x{height}+{x}+{y}')

    root_destroy.after(disp_time,root_destroy.destroy)
    #root_destroy.mainloop()

def close_window(window):
    window.destroy()

def clear_all(event=None):
    T=get_widget('text_widget')
    T.delete("1.0",END)
