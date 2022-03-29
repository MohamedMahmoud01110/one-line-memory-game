from termcolor import colored
from random import shuffle
from math import radians
from os import system
import time
import colorama
from colorama import Fore,Back,Style
from colorama.ansi import Fore
from colorama.initialise import reset_all
colorama.init()
import string
import random
p1=0
p2=0
x1=1
x2=1
y1=1
y2=1
v=0
list_of_number=list(range(1,21))
list_of_characters=['A','B','C','D','E','F','G','H','I','J']*2
shuffle(list_of_characters)
index=list(range(1,21))
temp=[]
dic={}
print(Fore.LIGHTGREEN_EX+"Welcome in One line memory game "+Style.RESET_ALL)
start=input(Fore.LIGHTBLUE_EX+"Press ENTER to START..."+Style.RESET_ALL)
if start=="":
    while v==0:
        while True:
            print(*index)
            x1=int(input(Fore.RED+"PLAYER ONE"+Style.RESET_ALL+" ,choose the first number from above: "))
            x2=int(input(Fore.RED+"PLAYER ONE"+Style.RESET_ALL+" ,choose the second number from above: "))
            if x1 and x2 in index:
                if x1!=x2:
                  for i in range(1,21):
                    dic[i] = list_of_characters[i-1]
                  if dic[x1] == dic[x2]:
                    index[x1-1]='*'
                    index[x2-1]='*'
                    list_of_number.remove(x1)                   
                    list_of_number.remove(x2) 
                    
                    p1=p1+1
                    print("PLAYER ONE SCORE:"+Fore.RED,str(1)+Style.RESET_ALL)
                    print("PLAYER ONE ALL SCORE:"+Fore.RED,str(p1)+Style.RESET_ALL)
                    time.sleep(2)
                    system('cls')
                    break
                  else:
                      temp = []
                      for i in range(0,20):
                        if i == x1-1 and x1 in index :
                           temp.append(colored(list_of_characters[i],color="red"))
                        elif i == x2-1 and x2 in index:
                           temp.append(colored(list_of_characters[i],color="red"))
                        else: 
                           temp.append(index[i])       
                      print(*temp)
                      print("PLAYER ONE SCORE:"+Fore.RED,str(0)+Style.RESET_ALL)
                      print("PLAYER ONE ALL SCORE:"+Fore.RED,str(p1)+Style.RESET_ALL)
                      time.sleep(2)
                      system('cls')
                      break 
                else:
                    print(Fore.LIGHTMAGENTA_EX+"you can't use the same number twice.."+Style.RESET_ALL+"plz choose diffrent numbers")

            else:
                print(Fore.LIGHTRED_EX+"Error, Number not exist!!"+Style.RESET_ALL)     
        if p1>p2 and index==['*']*20  : 
            print(Fore.LIGHTGREEN_EX+"PLAYER ONE WINS\U0001F382"+Style.RESET_ALL)
            v=1
            break
        elif p1==p2 and index==['*']*20:
          print(Fore.LIGHTRED_EX+"DRAW!!"+Style.RESET_ALL)
          break  
            
        if v==0:
                while True:
                    print (*index)
                    y1=int(input(Fore.YELLOW+"PLAYER TWO"+Style.RESET_ALL+" ,choose the first number from above: "))
                    y2=int(input(Fore.YELLOW+"PLAYER TWO"+Style.RESET_ALL+" ,choose the second number from above: "))
                    if y1 and y2 in index:
                        if y1!=y2:
                          for i in range(1,21):
                            dic[i] = list_of_characters[i-1]
                          if dic[y1] == dic[y2]:
                            index[y1-1]='*'
                            index[y2-1]='*'
                            list_of_number.remove(y1)
                            list_of_number.remove(y2)
                            p2=p2+1
                            print("PLAYER TWO SCORE:"+Fore.YELLOW,str(1)+Style.RESET_ALL)
                            print("PLAYER TWO ALL SCORE:"+Fore.YELLOW,str(p2)+Style.RESET_ALL)
                            time.sleep(2)
                            system('cls')
                            break
                          else:
                            temp=[]
                            for i in range(0,20):
                              if i ==y1- 1 and y1 in index :
                                 temp.append(colored(list_of_characters[i],color="red")) 
                              elif i ==y2- 1 and y2 in index:
                                 temp.append(colored(list_of_characters[i],color="red"))
                              else: 
                                 temp.append(index[i])   
                            print(*temp)
                            print("PLAYER TWO SCORE:"+Fore.YELLOW,str(0)+Style.RESET_ALL)
                            print("PLAYER TWO ALL SCORE:"+Fore.YELLOW,str(p2)+Style.RESET_ALL)
                            time.sleep(2)
                            system('cls')  
                            break
                        else:
                            print(Fore.LIGHTMAGENTA_EX+"you can't use the same twice.."+Style.RESET_ALL+"plz choose diffrent numbers")
                    else:
                        print(Fore.LIGHTRED_EX+"Error, Number not exist!!"+Style.RESET_ALL)
                if p1<p2 and index==['*']*20 : 
                    print(Fore.LIGHTGREEN_EX+"PLAYER TWO WINS\U0001F382"+Style.RESET_ALL)
                    v=1
                    break
                elif p1==p2 and index==['*']*20:
                 print(Fore.LIGHTRED_EX+"DRAW!!"+Style.RESET_ALL)
                 break 
              
                

    
