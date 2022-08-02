
import os

def output(text):
    Task=os.open("Task_List.txt",os.O_RDWR|os.O_CREAT)
    line=str.encode(text)
    os.write(Task,line)
    os.close(Task)
    print("Closed file successfully")

