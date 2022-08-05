

import os

def output(text):
    Task=os.open("Task_List.txt",os.O_RDWR|os.O_CREAT)
    line=str.encode(text)
    os.write(Task,line)
    os.close(Task)
    print("Closed file successfully")

def load():
    pass

def remove(text,select):
    #os.remove("Task_list.txt")
    with open("Task_list.txt","r+") as file:
        file.truncate(0)
        file.write(text)
        file.close
    with open("Task_list.txt","r+") as file:
        a=file.read()
        b=a.replace(select,"")
        file.truncate(0)
        #for letter in b:
        #    if letter =="-":
        #        letter.replace("-"*len(select),"")
        file.write(b)
    #Task=open("Task_list.txt",os.O_RDWR)
    #line=str.encode(text)
    #lineS=str.encode(select)
    #line1=line.decode("utf-8")
    #v=str.encode(b"")
    #lines=lineS.decode("utf-8")
    #FinalLine=line1.index(lines)
    #n=50
    #data=os.read(Task,n)
    #dat=data.replace(lineS,b"")
    #print(lineS)
    #os.write(Task,dat)
    #print(dat)
    #os.close(Task)
    file.close()
    print("Process Done")
