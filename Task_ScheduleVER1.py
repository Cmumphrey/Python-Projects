


from ast import Load
from tkinter import *
from tkinter import messagebox
from os_text import *





class Task_Scheduler():

    def __init__(self):
        self.main={}
        self.tasks={}
        self.sub_task={}


    def storage(self):
        """Store info in a text file"""
        pass

    def check_completion_subtask(self):
        if all(self.sub_task.values())==True:
            print("Sub-Tasks Completed, Good Job :)")
        pass

    def check_completion_task(self):
        if all(self.sub_task.values())==True:
            self.checkmark_tasks()
            print("Tasks Completed, Good Job :)")
        else:
            print("sub-tasks not complete")

    def check_completion_goal(self):
        for val in self.tasks.values():
            if all(val) == True:
                self.checkmark_main()
                print("Goal Achieved, Nice Going!!! :)")
            else:
                print("Tasks not complete")
    
    def checkmark_main(self):
        """Checkmark for main dict"""
        for key,val in self.main.items():
            self.main.update({key:not val})

    def un_check_main(self):
        for key,val in self.main.items():
            self.main.update({key:not val})
    
    def checkmark_tasks(self):
        """Checkmark for Tasks"""
        for key,val in self.tasks.items():
            self.tasks.update({key:not val})
    
    def checkmark_sub_tasks(self):
        """Checkmark for Sub-Tasks"""
        for key,val in self.sub_task.items():
            self.sub_task.update({key:not val})

    def add_goal(self):
        """ adds a goal to Main objective/dict"""
        self.main.update({bar_entry1.get():False})
        #for index, key in enumerate(self.main.keys()):
        #    print(index,key)

    def clear_goal(self):
        """clearing goal dict"""
        self.main.clear()
        pass

    def remove_goal(self):
        self.main.popitem()
        pass

    def add_task(self):
        """Add task to task dict"""
        self.tasks.update({bar_entry2.get():False})
        #for index,key in enumerate(self.tasks.keys()):
        #    print(index,key)

    def remove_task(self):
        self.tasks.popitem()
        pass

    def add_subtask(self):
        """Add sub-tasks to sub-task dict"""
        self.sub_task.update({bar_entry3.get():False})
        for index,key in enumerate(self.sub_task.keys()):
            print(index,key)
        pass

    def remove_subtask(self):
        """Removing Subtask"""
        self.sub_task.popitem()
        pass

    def upload_image(self):
        """Uses PIL Module, need to think about use case"""
        pass


    def add_note(self):
        pass

    def remove_note(self):
        pass

T=Task_Scheduler()




class App():
    def __init__(self):
        """Makes connections with Goals,Tasks and Sub-tasks"""
        self.connection={}
        self.goalL=[]
        self.connection2={}
        self.taskL=[]
        self.sub_taskL=[]

    def add_Goal(self):
        T.add_goal()
        self.connection.update({bar_entry1.get():[]})
        self.goalL.append(bar_entry1.get())
        #for key in T.main.keys():
        #    for value in T.tasks.keys():
        #        self.connection.update({key})
        #print(self.connection)
        #print(T.main)
        #print(self.Vlist)
        if len(T.main.keys())==1:
            place_holderG["text"]=bar_entry1.get()
            text.insert(END,"-"*len(bar_entry1.get()))
            text.insert(END,"\n"+bar_entry1.get())
            text.insert(END,"\n"+"-"*len(bar_entry1.get()))
            bar_entry1.delete(0,END)
        else:
            
            #self.connection.update({bar_entry1.get():[self.Vlist]})
            Label(frame,text=bar_entry1.get()).grid()
            
            #Checkbutton(frame,text="Test",variable=check[i-1],onvalue=True,offvalue=False,command=self.Test_box).grid(column=2)
            text.insert(END,"\n"+"-"*len(bar_entry1.get()))
            text.insert(END,"\n"+bar_entry1.get())
            text.insert(END,"\n"+"-"*len(bar_entry1.get()))
            bar_entry1.delete(0,END)
            #text.delete("1.0","end")
            print(T.main)
    
    #def items_selected(event):
#
    #    selected_indices = listbox1.curselection()
    #    selected_langs = ",".join([listbox1.get(i) for i in selected_indices])
    #    msg = f'You selected: {selected_langs}'
#
    #    messagebox.showinfo(
    #    title='Information',
    #    message=msg)

   # def Test_box(self):
   #     for but in check:
   #         if but.get()==False:
   #             print("Box unchecked")
   #             print(check)
   #             break
   #         else:
   #             print("Box checked")
#
   #             break
            
    def remove_Goal(self):
        pass

    def add_Task(self):
        T.add_task()
        self.connection2.update({bar_entry2.get():[]})
        self.taskL.append(bar_entry2.get())
        if len(T.tasks.keys())==1:
            for key in T.main.keys():
                self.connection[key]+=[bar_entry2.get()]
            #print(self.connection2)
            place_holderG1["text"]=bar_entry2.get()
            text.insert(END,"\n+ "+bar_entry2.get())
            bar_entry2.delete(0,END)
            #print(T.tasks)
        else:
            T.add_task()
            for key in T.main.keys():
                for key,val in self.connection.items():
                    if val in self.connection.items():
                        continue
                    continue
                self.connection[key]+=[bar_entry2.get()]
                break
            #print(T.tasks)
            print(self.connection)
            Label(frame1,text=bar_entry2.get()).grid()
            #Checkbutton(frame1,text="Test",variable=BooleanVar(),onvalue=True,offvalue=False).grid(column=2)
            text.insert(END,"\n+ "+bar_entry2.get())
            bar_entry2.delete(0,END)


    def remove_Task(self):
        pass

    def add_SubTask(self):
        T.add_subtask()
        self.sub_taskL.append(bar_entry3.get())
        #place_holderG2["text"]=bar_entry3.get()
        #print(self.connection2)
        if len(T.sub_task.keys())==1:
            for key in T.tasks.keys():
                for key,val in self.connection2.items():
                    if val in self.connection2.items():
                        continue
                    continue
                self.connection2[key]+=[bar_entry3.get()]
                break
            place_holderG2["text"]=bar_entry3.get()
            text.insert(END,"\n==>"+bar_entry3.get())
            print(self.connection2)
            bar_entry3.delete(0,END)
            #print(T.sub_task)
        else:
            T.add_subtask()
            for key in T.tasks.keys():
                for key,val in self.connection2.items():
                    if val in self.connection2.items():
                        continue
                    continue
                self.connection2[key]+=[bar_entry3.get()]
                break
            #print(T.sub_task)
            print(self.connection2)
            Label(frame2,text=bar_entry3.get()).grid()
            #Checkbutton(frame2,text="Test",variable=BooleanVar(),onvalue=True,offvalue=False).grid(column=2)
            text.insert(END,"\n==>"+bar_entry3.get())
            bar_entry3.delete(0,END)
            #print(T.sub_task)

    def remove_SubTask(self):
        pass

    def GetGoal_input(self):
        pass

    def GetTask_input(self):
        pass

    def GetSubTask_input(self):
        pass

    def Pick_Color(self):
        pass
    


A=App()



root=Tk()
checkmark1=BooleanVar()  
root.title("Task Scheduler")
root.resizable(True,True)
var1=BooleanVar()
var2=BooleanVar()
var3=BooleanVar()

#Frame
frame=LabelFrame(root, text="Goals")
frame1=LabelFrame(root, text="Tasks")
frame2=LabelFrame(root, text="Sub-Tasks")
#canvas/listbox 1
def New_window():

    def items_selected(event):

        selected_i = listbox1.curselection()
        selected_goal = ",".join([listbox1.get(i) for i in selected_i])
        msg = f'You completed: {selected_goal}'

        messagebox.showinfo(
        title='Information',
        message=msg)
        if selected_goal in A.goalL:
            #print(selected_langs)
            T.main.update({selected_goal:True})
            #print(T.main)
            idx=listbox1.get(0,END).index(selected_goal)
            listbox1.delete(idx)
            wip=text.get(1.0,END)
            remove(wip,selected_goal)
            
    Window=Toplevel()
    ca=Canvas(Window,height=8,width=8)
    ca.grid()
    goalLv=StringVar(value=A.goalL)
    listbox1=Listbox(Window, listvariable=goalLv,height=6,selectmode="EXTENDED")
    listbox1.grid(column=5,row=0,sticky="nwes")
    listbox1.bind('<<ListboxSelect>>', items_selected)
    #output(text.get(1.0,END))
#canvas/listbox2
def New_window1():

    def items_selected1(event):

        selected_i = listbox2.curselection()
        selected_task = ",".join([listbox2.get(i) for i in selected_i])
        msg = f'You completed: {selected_task}'

        messagebox.showinfo(
        title='Information',
        message=msg)
        if selected_task in A.taskL:
            print(selected_task)
            T.tasks.update({selected_task:True})
            print(T.tasks)
            idx=listbox2.get(0,END).index(selected_task)
            listbox2.delete(idx)
            wip=text.get(1.0,END)
            remove(wip,selected_task)
    Window1=Toplevel()
    ca=Canvas(Window1,height=8,width=8)
    ca.grid()
    taskL=StringVar(value=A.taskL)
    listbox2=Listbox(Window1, listvariable=taskL,height=6,selectmode="EXTENDED")
    listbox2.grid(column=5,row=0,sticky="nwes")
    listbox2.bind('<<ListboxSelect>>', items_selected1)
    #print(A.taskL)
    
def New_window2():

    def items_selected2(event):

        selected_i = listbox3.curselection()
        selected_subtask = ",".join([listbox3.get(i) for i in selected_i])
        msg = f'You completed: {selected_subtask}'

        messagebox.showinfo(
        title='Information',
        message=msg)
        if selected_subtask in A.sub_taskL:
            print(selected_subtask)
            T.sub_task.update({selected_subtask:True})
            print(T.sub_task)
            idx=listbox3.get(0,END).index(selected_subtask)
            listbox3.delete(idx)
            wip=text.get(1.0,END)
            remove(wip,selected_subtask)
    Window2=Toplevel()
    ca=Canvas(Window2,height=8,width=8)
    ca.grid()
    subtask=StringVar(value=A.sub_taskL)
    listbox3=Listbox(Window2, listvariable=subtask,height=6,selectmode="EXTENDED")
    listbox3.grid(column=5,row=0,sticky="nwes")
    listbox3.bind('<<ListboxSelect>>', items_selected2)

def saveB():
    output(text.get(1.0,END))

def LoadB():
    a=load()
    text.insert("1.0",a)
    #text.insert(a)
#input bar
bar_entry1=Entry(root, width=30)
bar_entry2=Entry(root, width=30)
bar_entry3=Entry(root, width=30)

#Checkmarks
check_test=Checkbutton(frame, text="",variable=var1,onvalue=True,offvalue=False)
check_test1=Checkbutton(frame1, text="",variable=var2,onvalue=True,offvalue=False)
check_test2=Checkbutton(frame2, text="",variable=var3,onvalue=True,offvalue=False)
#listboxes


#goalLv=StringVar(value=A.goalL)
#listbox1=Listbox(root, listvariable=goalLv,height=6,selectmode="extended")
#listbox1.grid(column=5,row=0,sticky="nwes")
#listbox1.bind('<<ListboxSelect>>', A.items_selected())

#Scrollbar
text=Text(root, height=8,width=35 )
#text.config(state="disabled")
text.grid(sticky="ew",row=0,column=9)
scroll=Scrollbar(root, orient="vertical", command=text.yview)
scroll.grid(row=0, column=0, sticky="ns")
text["yscrollcommand"]=scroll.set

#buttons

add_goal=Button(root, text="Add",command=A.add_Goal)
Del=Button(root,text="Del")
add_task=Button(root, text="Add",command=A.add_Task)
Del1=Button(root, text="Del")
add_subtask=Button(root, text="Add",command=A.add_SubTask)
Del2=Button(root, text="Del")
save_button=Button(root, text="Save",command=saveB)
load_button=Button(root,text="LOAD",command=LoadB).grid(row=10,column=10)
quit_button=Button(root, text="Exit",command=root.destroy)
#Buttons for listboxes
Goal_complete=Button(root,text="Goals",command=lambda: New_window()).grid(row=0,column=6)
task_complete=Button(root,text="Tasks",command=lambda: New_window1()).grid(row=0,column=7)
sub_task_complete=Button(root,text="S_Tasks",command=lambda: New_window2()).grid(row=0,column=8)

#labels
place_holderG=Label(frame, text="No goals right now")
place_holderG1=Label(frame1, text="No tasks right now")
place_holderG2=Label(frame2, text="No sub-tasks right now")



#Shove on screen
bar_entry1.grid(row=1,column=5,ipadx=1,ipady=1)
bar_entry2.grid(row=2,column=5,ipadx=1,ipady=1)
bar_entry3.grid(row=3,column=5,ipadx=1,ipady=1)

#frames_show
frame.grid(column=1,row=1)
frame1.grid(column=1,row=2)
frame2.grid(column=1,row=3)
place_holderG.grid()
place_holderG1.grid()
place_holderG2.grid()

#buttons_show
add_goal.grid(row=1,column=6)
Del.grid(row=1,column=7)
add_task.grid(row=2,column=6)
Del1.grid(row=2,column=7)
add_subtask.grid(row=3,column=6)
Del2.grid(row=3,column=7)
save_button.grid(row=10,column=11)
quit_button.grid(row=10, column=12)

#checkmark_show
#check_test.grid(row=2,column=2)
#check_test1.grid(row=2,column=2)
#check_test2.grid(row=2,column=2)

#Intiate App
root.mainloop()

