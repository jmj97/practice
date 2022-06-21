# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 17:45:49 2022

@author: mjcho
"""
# 2nd method
import keyboard
import threading
import time


velocity_num = 0
flag = 0

class Velocity(threading.Thread):
    def __init__(self):
        super().__init__()
    
    def run(self):
        global velocity_num
        global flag
        
        print("start")
        while True:
            char = keyboard.read_key()
            if(char == "p"):
                flag = 1
                print("you pressed p")
                break
            elif(char == "up"):
                velocity_num += 1
                # print(velocity_num)
            elif(char == "down"):
                velocity_num -= 1   
                # print(velocity_num)
            time.sleep(0.1)


class PrintResult(threading.Thread):
    def __init__(self):
        super().__init__()
    
    def run(self):
        global velocity_num
        global flag
        
        while True:
            print("the velocity is", velocity_num)
            time.sleep(0.1)
            
            if(flag == 1):
                print("end!!")
                break



if __name__ == "__main__":

    velocity_class_thread = Velocity()
    print_class_thread = PrintResult()
    
    velocity_class_thread.start()
    print_class_thread.start()
    
    velocity_class_thread.join()
    print_class_thread.join()
    

    
    
    















