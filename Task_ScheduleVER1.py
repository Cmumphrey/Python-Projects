

from tkinter import *
from tkinter import colorchooser
from tkinter import messagebox
from tkinter import ttk
import PIL

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
        #self.Vlist=[]
        self.connection2={}
        #self.Vlist2=[]

    def add_Goal(self):
        T.add_goal()
        self.connection.update({bar_entry1.get():[]})
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
            Checkbutton(frame,text="Test",variable=BooleanVar(),onvalue=True,offvalue=False,command=self.Test_box).grid(column=2)
            text.insert(END,"\n"+"-"*len(bar_entry1.get()))
            text.insert(END,"\n"+bar_entry1.get())
            text.insert(END,"\n"+"-"*len(bar_entry1.get()))
            bar_entry1.delete(0,END)
            print(T.main)
    
    def Test_box(self):
        if checkmark1.get()==False:
            print("Box unchecked")
        else:
            print("Box checked")
            
    def remove_Goal(self):
        pass

    def add_Task(self):
        T.add_task()
        self.connection2.update({bar_entry2.get():[]})
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
            Checkbutton(frame1,text="Test",variable=BooleanVar(),onvalue=True,offvalue=False).grid(column=2)
            text.insert(END,"\n+ "+bar_entry2.get())
            bar_entry2.delete(0,END)


    def remove_Task(self):
        pass

    def add_SubTask(self):
        T.add_subtask()
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
            text.insert(END,"\n-  "+bar_entry3.get())
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
            Checkbutton(frame2,text="Test",variable=BooleanVar(),onvalue=True,offvalue=False).grid(column=2)
            text.insert(END,"\n-  "+bar_entry3.get())
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

#input bar
bar_entry1=Entry(root, width=30)
bar_entry2=Entry(root, width=30)
bar_entry3=Entry(root, width=30)

#Checkmarks
check_test=Checkbutton(frame, text="",variable=var1,onvalue=True,offvalue=False)
check_test1=Checkbutton(frame1, text="",variable=var2,onvalue=True,offvalue=False)
check_test2=Checkbutton(frame2, text="",variable=var3,onvalue=True,offvalue=False)

#buttons
add_goal=Button(root, text="Add",command=A.add_Goal)
Del=Button(root,text="Del")
add_task=Button(root, text="Add",command=A.add_Task)
Del1=Button(root, text="Del")
add_subtask=Button(root, text="Add",command=A.add_SubTask)
Del2=Button(root, text="Del")
save_button=Button(root, text="Save")
quit_button=Button(root, text="Exit",command=root.destroy)

#labels
place_holderG=Label(frame, text="No goals right now")
place_holderG1=Label(frame1, text="No tasks right now")
place_holderG2=Label(frame2, text="No sub-tasks right now")

#Scrollbar
text=Text(root, height=8,width=35 )
text.grid(sticky="ew",row=0,column=8)
scroll=Scrollbar(root, orient="vertical", command=text.yview)
scroll.grid(row=0, column=0, sticky="ns")
text["yscrollcommand"]=scroll.set

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
save_button.grid(row=10,column=9)
quit_button.grid(row=10, column=10)

#checkmark_show
check_test.grid(row=2,column=2)
check_test1.grid(row=2,column=2)
check_test2.grid(row=2,column=2)

#Intiate App
root.mainloop()

