from tkinter import END, Tk
from tkinter import ttk
import tkinter

class App1():

        #Fields- Attributes
        #Constructors- Special methods called when we first create an instance
    def __init__(self):
        print("Building App")
        #Build my GUI

        self.root=Tk()
        self.root.title("Task Scheduler")
        self.root.resizable(False,False)
        self.checkmark1=tkinter.BooleanVar()
        self.var1=tkinter.BooleanVar()
        self.var2=tkinter.BooleanVar()
        self.var3=tkinter.BooleanVar()
        #frame
        self.style=ttk.Style()
        self.style.configure("BW.TLabel", background="yellow")
        self.frame=ttk.LabelFrame(self.root, text="Goals",style="BW.TLabel")
        self.frame1=ttk.LabelFrame(self.root, text="Tasks")
        self.frame2=ttk.LabelFrame(self.root, text="Sub-Tasks")

        self.place_holderG=ttk.Label(self.frame, text="No goals right now")
        self.place_holderG1=ttk.Label(self.frame1, text="No tasks right now")
        self.place_holderG2=ttk.Label(self.frame2, text="No sub-tasks right now")

        #input bar
        self.bar_entry1=ttk.Entry(self.root, width=30)
        self.bar_entry2=ttk.Entry(self.root, width=30)
        self.bar_entry3=ttk.Entry(self.root, width=30)

        #Checkmarks
        self.check_test=ttk.Checkbutton(self.frame, text="",variable=self.var1,onvalue=True,offvalue=False)
        self.check_test1=ttk.Checkbutton(self.frame1, text="",variable=self.var2,onvalue=True,offvalue=False)
        self.check_test2=ttk.Checkbutton(self.frame2, text="",variable=self.var3,onvalue=True,offvalue=False)


        #buttons
        self.add_goal=ttk.Button(self.root, text="Add",command=A.add_Goal)
        self.Del=ttk.Button(self.root,text="Del")
        self.add_task=ttk.Button(self.root, text="Add",command=A.add_Task)
        self.Del1=ttk.Button(self.root, text="Del")
        self.add_subtask=ttk.Button(self.root, text="Add",command=A.add_SubTask)
        self.Del2=ttk.Button(self.root, text="Del")
        self.save_button=ttk.Button(self.root, text="Save")
        self.quit_button=ttk.Button(self.root, text="Exit",command=self.root.destroy)


        #show on screen
        self.frame.grid(column=1,row=1)
        self.frame1.grid(column=1, row=2)
        self.frame2.grid(column=1, row=3)

        #buttons_show
        self.add_goal.grid(row=1,column=6)
        self.Del.grid(row=1,column=7)
        self.add_task.grid(row=2,column=6)
        self.Del1.grid(row=2,column=7)
        self.add_subtask.grid(row=3,column=6)
        self.Del2.grid(row=3,column=7)
        self.save_button.grid(row=10,column=9)
        self.quit_button.grid(row=10, column=10)

        self.place_holderG.grid()
        self.place_holderG1.grid()
        self.place_holderG2.grid()

        self.bar_entry1.grid(row=1,column=5,ipadx=1,ipady=1)
        self.bar_entry2.grid(row=2,column=5,ipadx=1,ipady=1)
        self.bar_entry3.grid(row=3,column=5,ipadx=1,ipady=1)

        self.root.mainloop()


    #Method - Behaviours

a=App1() #Create an app object and store the reference

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
        self.main.update({a.bar_entry1.get():False})
        #for index, key in enumerate(self.main.keys()):
        #    print(index,key)

    def clear_goal(self):
        """clearing goal dict"""
        self.main.clear()
        pass

    def add_task(self):
        """Add task to task dict"""
        self.tasks.update({a.bar_entry2.get():False})
        #for index,key in enumerate(self.tasks.keys()):
        #    print(index,key)

    def remove_task(self):
        self.tasks.popitem()
        pass

    def add_subtask(self):
        """Add sub-tasks to sub-task dict"""
        self.sub_task.update({a.bar_entry3.get():False})
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
        self.connection.update({a.bar_entry1.get():[]})
        #for key in T.main.keys():
        #    for value in T.tasks.keys():
        #        self.connection.update({key})
        #print(self.connection)
        #print(T.main)
        #print(self.Vlist)
        if len(T.main.keys())==1:
            a.place_holderG["text"]=a.bar_entry1.get()
            a.bar_entry1.delete(0,END)
        else:

            #self.connection.update({bar_entry1.get():[self.Vlist]})
            tkinter.Label(a.frame,text=a.bar_entry1.get()).grid()
            tkinter.Checkbutton(a.frame,text="Test",variable=tkinter.BooleanVar(),onvalue=True,offvalue=False,command=self.Test_box).grid(column=2)
            a.bar_entry1.delete(0,END)
            print(T.main)
    
    def Test_box(self):
        if a.checkmark1.get()==False:
            print("Box unchecked")
        else:
            print("Box checked")
            
    def remove_Goal(self):
        pass

    def add_Task(self):
        T.add_task()
        self.connection2.update({a.bar_entry2.get():[]})
        if len(T.tasks.keys())==1:
            for key in T.main.keys():
                self.connection[key]+=[a.bar_entry2.get()]
            #print(self.connection2)
            a.place_holderG1["text"]=a.bar_entry2.get()
            a.bar_entry2.delete(0,END)
            #print(T.tasks)
        else:
            T.add_task()
            for key in T.main.keys():
                for key,val in self.connection.items():
                    if val in self.connection.items():
                        continue
                    continue
                self.connection[key]+=[a.bar_entry2.get()]
                break
            #print(T.tasks)
            print(self.connection)
            tkinter.Label(a.frame1,text=a.bar_entry2.get()).grid()
            tkinter.Checkbutton(a.frame1,text="Test",variable=tkinter.BooleanVar(),onvalue=True,offvalue=False).grid(column=2)
            a.bar_entry2.delete(0,END)


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
                self.connection2[key]+=[a.bar_entry3.get()]
                break
            a.place_holderG2["text"]=a.bar_entry3.get()
            print(self.connection2)
            a.bar_entry3.delete(0,END)
            #print(T.sub_task)
        else:
            T.add_subtask()
            for key in T.tasks.keys():
                for key,val in self.connection2.items():
                    if val in self.connection2.items():
                        continue
                    continue
                self.connection2[key]+=[a.bar_entry3.get()]
                break
            #print(T.sub_task)
            print(self.connection2)
            tkinter.Label(a.frame2,text=a.bar_entry3.get()).grid()
            tkinter.Checkbutton(a.frame2,text="Test",variable=tkinter.BooleanVar(),onvalue=True,offvalue=False).grid(column=2)
            a.bar_entry3.delete(0,END)
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

