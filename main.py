from tkinter import*
from tkinter import messagebox,filedialog
import subprocess
class Vs_code:
    def __init__(self,root):
        self.root=root
        self.root.title("VS Code Editor")
        self.root.geometry("1350x700+0+0")

        self.path_name=''
        self.color_theme=StringVar()
        self.color_theme.set('Light Default')
        self.font_size=18
        #=====================Menu Icons ================

        self.new_file_icon=PhotoImage(file='icons/new.png')
        self.open_file_icon=PhotoImage(file='icons/open.png')
        self.save_file_icon=PhotoImage(file='icons/save.png')
        self.save_as_file_icon=PhotoImage(file='icons/save as.png')
        self.exit_file_icon=PhotoImage(file='icons/exit.png')

        self.light_default_icon=PhotoImage(file='icons/light default.png')
        self.light_plus_icon=PhotoImage(file='icons/light plus.png')
        self.dark_icon=PhotoImage(file='icons/dark.png')
        self.red_icon=PhotoImage(file='icons/red.png')
        self.monokai_icon=PhotoImage(file='icons/monkai.png')
        self.night_blue_icon=PhotoImage(file='icons/night blue.png')

        #=====================Menus======================

        Mymenu=Menu(self.root)

        Filemenu=Menu(Mymenu,tearoff=False)
        Filemenu.add_command(label='New File',image=self.new_file_icon,compound=LEFT,accelerator='Clt+N',command=self.new_file)
        Filemenu.add_command(label='Open File',image=self.open_file_icon,compound=LEFT,accelerator='Ctl+O',command=self.open_file)
        Filemenu.add_command(label='Save',image=self.save_file_icon,compound=LEFT,accelerator='Ctl+S',command=self.save_file)
        Filemenu.add_command(label='Save as',image=self.save_as_file_icon,compound=LEFT,accelerator='Ctl+Alt+s',command=self.save_as_file)
        Filemenu.add_command(label='Exit',image=self.exit_file_icon,compound=LEFT,accelerator='Ctl+Q',command=self.exit_function)

        color_theme=Menu(Mymenu,tearoff=False)
        color_theme.add_radiobutton(label='Light Default',value='Light Default',variable=self.color_theme,image=self.light_default_icon,compound=LEFT,command=self.color_change)
        color_theme.add_radiobutton(label='Light Plus',value='Light Plus',variable=self.color_theme,image=self.light_plus_icon,compound=LEFT,command=self.color_change)
        color_theme.add_radiobutton(label='Dark',value='Dark',variable=self.color_theme,image=self.dark_icon,compound=LEFT,command=self.color_change)
        color_theme.add_radiobutton(label='Red',value='Red',variable=self.color_theme,image=self.red_icon,compound=LEFT,command=self.color_change)
        color_theme.add_radiobutton(label='Monokai',value='Monokai',variable=self.color_theme,image=self.monokai_icon,compound=LEFT,command=self.color_change)
        color_theme.add_radiobutton(label='Night Blue',value='Night Blue',variable=self.color_theme,image=self.night_blue_icon,compound=LEFT,command=self.color_change)

        Mymenu.add_cascade(label='File',menu=Filemenu)
        Mymenu.add_cascade(label='Color Theme',menu=color_theme)
        Mymenu.add_command(label='Clear',command=self.clear_all)
        Mymenu.add_separator()
        Mymenu.add_command(label='Run',command=self.run)
        self.root.config(menu=Mymenu)

        #==================Menu Ends Here==============================

        #==================EditorFrame=================================        
        
        

        EditorFrame=Frame(self.root,bg="white")
        EditorFrame.place(x=0,y=0,relwidth=1,height=500)

        Scrolly=Scrollbar(EditorFrame,orient=VERTICAL)
        Scrolly.pack(side=RIGHT,fill=Y)
        self.txt_editor=Text(EditorFrame,bg='white',font=('times new roman',self.font_size),yscrollcommand=Scrolly.set)
        self.txt_editor.pack(fill=BOTH,expand=1)
        Scrolly.config(command=self.txt_editor.yview)


        #==================OutputFrame=================================        
        

        outputFrame=LabelFrame(root,text='output',font=('arial',12,'bold'))
        outputFrame.place(x=0,y=500,relwidth=1,height=170)


        Scrolly=Scrollbar(outputFrame,orient=VERTICAL)
        Scrolly.pack(side=RIGHT,fill=Y)
        self.txt_output=Text(outputFrame,bg='white',font=('times new roman',18),yscrollcommand=Scrolly.set)
        self.txt_output.pack(fill=BOTH,expand=1)
        Scrolly.config(command=self.txt_output.yview)

        #===================Shortcuts==============================

        self.root.bind('<Control-plus>',self.font_size_inc)
        self.root.bind('<Control-minus>',self.font_size_dec)
        self.root.bind('<Control-o>',self.open_file)
        self.root.bind('<Control-n>',self.new_file)
        self.root.bind('<Control-s>',self.save_file)
        self.root.bind('<Control-Alt-s>',self.save_as_file)
        self.root.bind('<Control-q>',self.exit_function)


        #===================All Functions===========================

    def font_size_inc(self,event=None):
        self.font_size+=1
        self.txt_editor.config(font=('times new roman',self.font_size))

    def font_size_dec(self,event=None):
        self.font_size-=1
        self.txt_editor.config(font=('times new roman',self.font_size))    

    def run(self):
        if self.path_name=='':
            messagebox.showerror('Error',"please save the file to execute the code",parent=self.root)
        else:
            command=f'python {self.path_name}'
            run_file=subprocess.Popen(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
            output,error=run_file.communicate()
            self.txt_output.delete('1.0',END)
            self.txt_output.insert('1.0',output)
            self.txt_output.insert('1.0',error)



    def clear_all(self):
        self.txt_editor.delete('1.0',END)
        self.txt_output.delete('1.0',END)

    def color_change(self):
        if self.color_theme.get()=='Light Default':
            self.txt_editor.config(bg='#ffffff',fg='#000000')
            self.txt_output.config(bg='#ffffff',fg='#000000')
        if self.color_theme.get()=='Light Plus':
            self.txt_editor.config(bg='#e0e0e0',fg='#474747')
            self.txt_output.config(bg='#e0e0e0',fg='#474747')
        if self.color_theme.get()=='Dark':
            self.txt_editor.config(bg='#2d2d2d',fg='#c4c4c4')
            self.txt_output.config(bg='#2d2d2d',fg='#c4c4c4')
        if self.color_theme.get()=='Red':
            self.txt_editor.config(bg='#ffe8e8',fg='#2d2d2d')
            self.txt_output.config(bg='#ffe8e8',fg='#2d2d2d')
        if self.color_theme.get()=='Monokai':
            self.txt_editor.config(bg='#d3b774',fg='#474747')
            self.txt_output.config(bg='#d3b774',fg='#474747')
        if self.color_theme.get()=='Night Blue':
            self.txt_editor.config(bg='#6b9dc2',fg='#ededed')
            self.txt_output.config(bg='#6b9dc2',fg='#ededed')
    


    def exit_function(self,event=None):
        self.root.destroy()

    def new_file(self,event=None):
        self.path_name=''
        self.txt_editor.delete('1.0',END)
        self.txt_output.delete('1.0',END)
        
    def save_file(self,event=None):
        if self.path_name=="":
           self.save_as_file()
        else:
            fp=open(self.path_name,'w')
            fp.write(self.txt_editor.get('1.0',END))
            fp.close()

    def open_file(self,event=None):
        path=filedialog.askopenfilename(filetypes=[('Python Files','*.py')],defaultextension=('.py'))
        if path!='':
            self.path_name=path
            fp=open(self.path_name,'r')
            data=fp.read()
            self.txt_editor.delete('1.0',END)
            self.txt_editor.insert('1.0',data)
            fp.close()
    def save_as_file(self,event=None):
        path=filedialog.asksaveasfilename(filetypes=[('Python Files','*.py')],defaultextension=('.py'))
        if path!='':
            self.path_name=path
            fp=open(self.path_name,'w')
            fp.write(self.txt_editor.get('1.0',END))
            fp.close()



root=Tk()
obj=Vs_code(root)
root.mainloop()