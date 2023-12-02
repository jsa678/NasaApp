import tkinter as tk
import os, random
import requests
import webbrowser
import tkintermapview
from tkinter import messagebox , Canvas, PhotoImage, mainloop, ttk
from math import sin
from Nasa import *
from articleScrapper import *




frame_styles = {"relief": "groove",
                "bd": 3, "bg": "#5C5C5C",
                "fg": "#000000", "font": ("Arial", 12, "bold")}

def callback(url):
    webbrowser.open_new(url)

def change_bg():
    if is_picture == "image":
        change_desktop(response['title'])
        tk.messagebox.showinfo("Success", "Your background is changed ")
    else:
        video_url = response["url"]
        
        tk.messagebox.showinfo(title="Error",
                                    message="Today's image is actually a video... \n"
                                            "    So heres the link instead \n\n"
                                            " Link: \n"
                                            "{}".format(video_url)
                                    )


def fact_time():
    # say_fact()
    tk.messagebox.showinfo(title="Fact", message=nasa_fact, icon='info')

class MyApp(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        main_frame = tk.Frame(self, bg="#3D59AB", height=800, width=1200)
        main_frame.pack_propagate(0)
        main_frame.pack(fill="both", expand="true")
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)
        # self.resizable(0, 0) prevents the app from being resized
        # self.geometry("1024x600") fixes the applications size
        self.frames = {}
        pages = (Some_Widgets, PageOne)#, PageTwo, PageThree, PageFour)
        
        for F in pages:
            frame = F(main_frame, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame(Some_Widgets)

    def show_frame(self, name):
        frame = self.frames[name]
        frame.tkraise()

    def OpenNewWindow(self):
        OpenNewWindow()

    def Quit_application(self):
        self.destroy()


class GUI(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.main_frame = tk.Frame(self, bg="#104E8B", height=900, width=1200)
        # self.main_frame.pack_propagate(0)
        self.main_frame.pack(fill="both", expand="true")
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)



class Some_Widgets(GUI):  # inherits from the GUI class
    def __init__(self, parent, controller):
        GUI.__init__(self, parent)

        frame1 = tk.LabelFrame(self, frame_styles, text="Nasa Event API")
        frame1.place(rely=0.05, relx=0.02, height=330, width=750)

        frame2 = tk.LabelFrame(self, frame_styles, text="Background Change")
        frame2.place(rely=0.5, relx=0.70, height=150, width=300)

        frame3 = tk.LabelFrame(self,frame_styles,text="Data Sources")
        frame3.place(rely=0.70, relx=0.70, height=150, width=300)

        frame4 = tk.LabelFrame(self,frame_styles,text="Recent Space Articles! - Web Scraping using Beautifulsoup4")
        frame4.place(rely=0.5, relx=0.02, height=400, width=750)

        frame5 = tk.LabelFrame(self,frame_styles,text="About the NASA App")
        frame5.place(rely=0.05, relx=0.7, height=200, width=350)

        frame6 = tk.LabelFrame(self,frame_styles,text="Reach Me Here!!")
        frame6.place(rely=0.3, relx=0.7, height=100, width=350)

        def multiple_yview(*args):
            my_text1.yview(*args)
            my_text1.yview(*args)
    

        text_scroll = tk.Scrollbar(frame4)
        text_scroll.pack( side = "left", fill= "y")
        my_text1 = tk.Text(frame4, height=20, font=("bold", 20), yscrollcommand=text_scroll.set, wrap='word')
        my_text1.pack(side= "left", padx=3)
        text_scroll.config(command = multiple_yview)


        for item, link in zip(titleAll,linkAll):
            button = tk.Button(my_text1,text=item, width= 75 , command= lambda x = link: webbrowser.open_new(x), pady=5)
            my_text1.window_create('end', window=button)
            my_text1.insert('end', '\n')



        text = tk.Text(frame5, wrap= 'word')
        text.pack()
        text.insert(tk.END,"Thanks for checking out my NASA App. My Name is Justin Singer and I am a new Freelancer! I wrote this small app initially for fun and to help keep my desktop background fun. However I have expanded on the initial code to highlight some of my various Python skills while also having fun with something I have always have loved... SPACE! This project aims to fill out my portfolio and give potetional clients a small sample of my abilities. To gather 'Nasa Events' APIs were utilized, for daily Space articles 'Beautiful Soup' was used for Web Scrapping and the entire GUI is built using tkinter!")


        button1 = tk.Button(frame2, text="Change Background", command=lambda: change_bg())
        button1.pack()
        button2 = tk.Button(frame2, text="Fact Popup", command=lambda: fact_time())
        button2.pack()
        button3 = tk.Button(frame3, text="NASA Image API", command=lambda: callback("https://apod.nasa.gov/apod/astropix.html"))
        button3.pack()
        button4 = tk.Button(frame3, text="NASA Event APIs", command=lambda: callback("https://eonet.gsfc.nasa.gov/docs/v3#eventsAPI"))
        button4.pack()
        button5 = tk.Button(frame3, text="Space and Other Science News Source", command=lambda: callback("https://www.sciencenews.org/"))
        button5.pack()

        button6 = tk.Button(frame6, text="LinkedIn", command=lambda: callback("https://www.linkedin.com/in/justin-singer/"))
        button6.pack()
        button7 = tk.Button(frame6, text="UpWork", command=lambda: callback("https://www.upwork.com/freelancers/justinsinger"))
        button7.pack()
        button8 = tk.Button(frame6, text="GitHub", command=lambda: callback("https://github.com/jsa678"))
        button8.pack()



 

        # This is a treeview.
        tv1 = ttk.Treeview(frame1)
        tv1.tag_configure('odd', background='#4F4F4F')
        tv1.tag_configure('even', background='#9E9E9E')
        column_list_account = ["NASA Events", "Event Type", "Coordinates"]
        tv1['columns'] = column_list_account
        tv1["show"] = "headings"  # removes empty column
        for column in column_list_account:
            tv1.heading(column, text=column)
            tv1.column(column, width=0)
        tv1.column("NASA Events", minwidth=0, width=150)
        tv1.place(relheight=1, relwidth=0.995)
        treescroll = tk.Scrollbar(frame1)
        treescroll.configure(command=tv1.yview)
        tv1.configure(yscrollcommand=treescroll.set)
        treescroll.pack(side="right", fill="y")

        def Load_data():
            for row in ChartArray:
                tv1.insert("", "end", values=row)

        def Refresh_data():
            # Deletes the data in the current treeview and reinserts it.
            tv1.delete(*tv1.get_children())  # *=splat operator
            Load_data()

        Load_data()


class PageOne(GUI):
    def __init__(self, parent, controller):
        GUI.__init__(self, parent)

        label1 = tk.Label(self.main_frame, font=("Verdana", 20), text="Page One")
        label1.pack(side="top")


class OpenNewWindow(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        main_frame = tk.Frame(self)
        main_frame.pack_propagate(0)
        main_frame.pack(fill="both", expand="true")
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)
        self.title("Here is the Title of the Window")
        self.geometry("500x500")
        self.resizable(0, 0)

        frame1 = ttk.LabelFrame(main_frame, text="This is a ttk LabelFrame")
        frame1.pack(expand=True, fill="both")

        label1 = tk.Label(frame1, font=("Verdana", 20), text="OpenNewWindow Page")
        label1.pack(side="top")

top = MyApp()
root = MyApp()
root.withdraw()
root.title("Tkinter App Template")

root.mainloop()


