# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 17:45:49 2022

@author: mjcho
"""

#%% 1st code
import keyboard
import threading
import time

velocity_num = 0
flag = 0

class Velocity():
    def __init__(self):
        # super().__init__()
        pass
    
    def control_velocity1(self):
        global velocity_num
        global flag
        
        print("start")
        # char = "up"
        while True:
            char = keyboard.read_key()
            if(char == "p"):
                flag = 1
                # print("you pressed p")
                break
            elif(char == "up"):
                velocity_num += 1
                # print(velocity_num)
            elif(char == "down"):
                velocity_num -= 1   
                # print(velocity_num)
            time.sleep(0.1)

class PrintResult(): #class선언, threading함수의 속성을 사용하지 않기에, 상속은 필요 없음
    def __init__(self): #생성자 함수(인스턴스 초기화)
        # super().__init__()
        pass
        
    def print_velocity1(self):
        # global velocity_num
        # global flag
            
        while True:
            print("the velocity is", velocity_num)
            time.sleep(0.01)
            
            if(flag == 1):
                print("end!!")
                break


if __name__ == "__main__":

    velocity_class = Velocity() #클래스의 instance 생성
    print_class = PrintResult()
    
    p1 = threading.Thread(target = velocity_class.control_velocity1) #threading.Thread함수의 instance 생성
    p2 = threading.Thread(target = print_class.print_velocity1)
    
        
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()

#%% 2nd method
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
    

    
    
    















