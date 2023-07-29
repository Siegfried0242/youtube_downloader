from tkinter import *
from PIL import ImageTk, Image
from tkinter.filedialog import *
from tkinter import messagebox
import customtkinter
import yt_dlp
import sys

class Main_app:

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.root = Tk()
        self.root.title("Youtube Downloader")
        self.root.geometry("800x300")
        Color_ = "#3F3F3F"
        text_color_ = "white"
        self.root['bg']= Color_
        self.root.resizable(False,False)
        self.root.iconbitmap("yt_icon.ico")
        ####


        ####
        frame_1 = Frame(self.root,bg="red")
        url_label = LabelFrame(frame_1,text="Link URL",bd=0,font = ("Context Rounded SSi",18),bg=Color_,fg=text_color_)
        self.entry_input = Entry(url_label,width=35,font=("Beagle",12,"bold"))
        self.entry_input.grid(row=1,column=0,pady=5)
        self.entry_input.bind("<Button-3>",self.do_popup)
        url_label.grid(row=0)
        frame_1.place(x=400,y=10)
        ####
        frame_1_1 = Frame(self.root,bg=Color_)
        file_path_label = LabelFrame(frame_1_1,text="Save Location",bd=0,font = ("Context Rounded SSi",18),bg=Color_,fg=text_color_)
        self._path = StringVar()
        self.file_path = customtkinter.CTkEntry(file_path_label,width=300,fg_color='white',border_color='black'
        ,border_width=1,text_color="black",text_font=("Beagle",12,"bold"),textvariable=self._path)
        file_path_label.grid(row=0,column=0,pady=5)
        self.file_path.grid(row=1,column=0,pady=5)
        frame_1_1.place(x=400,y=80)
        ####
        frame_2 = Frame(self.root)
        format_label = LabelFrame(frame_2,text="Select Format",font = ("Context Rounded SSi",18),bg=Color_,bd=0,fg=text_color_)
        self.option_id = IntVar()
        self.option_mp3 = Radiobutton(format_label,text = "MP3",variable=self.option_id,value=0,font = ("Context Rounded SSi",14,"italic")
        ,bg = Color_,activebackground=Color_)
        self.option_mp4 = Radiobutton(format_label,text = "MP4",variable=self.option_id,value=1,font = ("Context Rounded SSi",14,"italic")
        ,bg = Color_,activebackground=Color_,fg="#7B0000")
        self.option_mp3.grid(row=0,column=0,padx=20)
        self.option_mp4.grid(row=0,column=1,padx=20)
        format_label.grid(row=0)
        frame_2.place(x=400,y=155)
        ####
        button_image = ImageTk.PhotoImage(Image.open("icon_.png").resize((25,25),Image.LANCZOS))
        frame_3 = Frame(self.root,width=100,height=100,bg=Color_)
        self.download_button =  customtkinter.CTkButton(frame_3,text = "Download",command=self.downloading,text_font = ("Context Rounded SSi",18),image = button_image,
        compound = "right",corner_radius=10,fg_color="#929292",text_color="black",hover_color="#D1D1D1")
        self.download_button.grid(row=0)
        frame_3.place(x=470,y=240)
        ####
        frame_4 = Frame(self.root)
        yt_logo = ImageTk.PhotoImage(Image.open("fgfdfdfdf.png").resize((350,150),Image.LANCZOS))
        image_label  = Label(frame_4,image=yt_logo,bg=Color_)
        image_label.image = yt_logo 
        image_label.grid()
        frame_4.place(x=10,y=50)
        ####
        frame_5 = Frame(self.root,bg=Color_)
        self.path_select = customtkinter.CTkButton(frame_5,text="Browse",height=28,width=20,compound="right",text_font = ("Context Rounded SSi",10,"bold")
        ,fg_color="#929292",text_color="black",hover_color="#D1D1D1",command=self.select_file_path)
        self.path_select.grid()
        frame_5.place(x=705,y=120)
        ####
        frame_6 = Frame(self.root,bg=Color_)
        self.status = StringVar()
        self.status.set("Waiting for action....")
        self.status_label = Label(frame_6,textvariable=self.status,bg=Color_,font=("Beagle",18,"bold"))
        self.status_label.grid(row=0)
        frame_6.place(x=10,y=250)
        ###
        self.m = Menu(self.root, tearoff = 0)
        self.m.add_command(label ="Cut    ตัด   (Ctrl+X)",command=self.cut_text,)
        self.m.add_command(label ="Copy    คัดลอก  (Ctrl+C)",command=self.copy_text)
        self.m.add_command(label ="Paste    วาง  (Ctrl+V)",command=self.paste_text)
        self.m.add_separator()
        self.m.add_command(label ="Select All    เลือกทั้งหมด  (Ctrl+A)",command= self.select_all)
        ###
        self.root.bind_all("<Key>",self._onKeyRelease,"+")
        self.root.mainloop()
        

    def button_command(self):
        self.get_url = self.entry_input.get()
        self.to_download()
    
    def downloading(self):
        self.status.set("Downloading")
        self.status_label.update()
        self.button_command()


    def to_download(self):
        video_url = self.get_url
        format_selector = self.option_id.get()
        if len(self._path.get()) == 0:
            self._path.set(self.file_path.get())
        output_path = self._path.get()
        ydl_opts = [{
            'ignoreerrors': True,
            'format': 'bestaudio/best',
            'postprocessors':
            [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': f'{output_path}/yt_dowloader/mp3/%(title)s.%(ext)s'
        },
        {
            'ignoreerrors': True,
            "format": "bestvideo[height<=3840][ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
            'outtmpl': f'{output_path}/yt_dowloader/mp4/%(title)s.%(ext)s'
        }]

        with yt_dlp.YoutubeDL(ydl_opts[format_selector]) as ydl:
            ydl.download(video_url)
        self.status.set("Completed")
        self.status_label.update()
        messagebox.showinfo("Success",message=f"Download Completed!\nDestination: {output_path}")
        self.status.set("Waiting for action....")
        self.status_label.update()
        
    
    def select_file_path(self):
        folder_selected = askdirectory()
        self._path.set(folder_selected)
        self.file_path.configure(textvariable=self._path,text_font=("Beagle",12,"bold"))
        self.file_path.update()

    def _onKeyRelease(self,event):
        ctrl  = (event.state & 0x4) != 0
        if event.keycode==88 and  ctrl and event.keysym.lower() != "x": 
            event.widget.event_generate("<<Cut>>")

        if event.keycode==86 and  ctrl and event.keysym.lower() != "v": 
            event.widget.event_generate("<<Paste>>")

        if event.keycode==67 and  ctrl and event.keysym.lower() != "c":
            event.widget.event_generate("<<Copy>>")

        if event.keycode==65 and  ctrl and event.keysym.lower() != "a":
            event.widget.event_generate("<<SelectAll>>")

    def copy_text(self):
        self.entry_input.event_generate("<<Copy>>")

    def paste_text(self):
        self.entry_input.event_generate("<<Paste>>")

    def cut_text(self):
        self.entry_input.event_generate("<<Cut>>")
    
    def select_all(self):
        self.entry_input.event_generate("<<SelectAll>>")

    def do_popup(self,event):
        try:
            self.m.tk_popup(event.x_root, event.y_root)
            
        finally:
            self.m.grab_release()
  

Main_app()