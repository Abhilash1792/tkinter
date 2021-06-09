#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *
window=Tk()
window.title("Welcome")
window.mainloop()


# In[7]:


import tkinter 
m = tkinter.Tk() 
''' 
widgets are added here 
'''
m.mainloop() 


# In[233]:


from tkinter import *
me=Tk()
me.title("Tkinter")
mylabel=Label(me,text="Hi this is mu GUI" )
mylabel.config(font=44)
mylabel.grid(row=2 , column =2)
mylabel1=Label(me , text="HIIi this is me",font=12).grid(row = 1 ,column=1)
me.mainloop()


# In[59]:


from tkinter import *
root=Tk()
def clickme():
    label1=Label(root , text="See you clicked me!",bg="lightgreen",fg="red").pack()
mybut=Button(root ,text="Click me" """,state=DISABLED """,padx=12,pady=10,command=clickme,fg="#111111",bg="pink").pack()
root.mainloop()


# In[96]:


from tkinter import *
root=Tk()
e=Entry(root,bg="lightgreen",width=25,borderwidth=10)
e.pack()
e.insert(0,"put your name in this")
def clickme():
    label1=Label(root ,text="Hello " +e.get()).pack()

mybut=Button(root ,text="Name" ,command=clickme).pack()

root.mainloop()


# In[5]:


from tkinter import *
root=Tk()
root.title("Nikhil's Calculater")
e=Entry(root,bg="lightgreen",font=10,width=34,borderwidth=10)
e.grid(row=0 ,column= 0,columnspan=4,padx=10,pady=10 )

def buttonclick(number):
    
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current) + str(number))
    
def buttonclear():
    e.delete(0,END)

def buttonadd():
    global f_num
    global math
    math="addition"
    x=e.get()
    f_num=int(x)
    e.delete(0,END)

def buttonequal():
    y=e.get()
    e.delete(0,END)
    if math=="adition":
        e.insert(0,f_num+int(y))
    if math=="subtraction":
        e.insert(0,f_num-int(y))
    if math=="multiply":
        e.insert(0,f_num*int(y))
    if math=="division":
        e.insert(0,f_num/int(y))
    
    
    
def buttonsub():
    global f_num
    global math
    math="subtraction"
    x=e.get()
    f_num=int(x)
    e.delete(0,END)
def buttondiv():
    global f_num
    global math
    math="division"
    x=e.get()
    f_num=int(x)
    e.delete(0,END)
    
def buttonmul():
    global f_num
    global math
    math="multiply"
    x=e.get()
    f_num=int(x)
    e.delete(0,END)
    
button_0=Button(root,text="0",font=10,padx=40,pady=20,command=lambda :buttonclick(0),bg="black",fg="white")
button_1=Button(root,text="1",font=10,padx=40,pady=20,command=lambda :buttonclick(1),bg="black",fg="white")
button_2=Button(root,text="2",font=10,padx=40,pady=20,command=lambda :buttonclick(2),bg="black",fg="white")
button_3=Button(root,text="3",font=10,padx=40,pady=20,command=lambda :buttonclick(3),bg="black",fg="white")
button_4=Button(root,text="4",padx=40,font=10,pady=20,command=lambda :buttonclick(4),bg="black",fg="white")
button_5=Button(root,text="5",padx=40,pady=20,font=10,command=lambda :buttonclick(5),bg="black",fg="white")
button_6=Button(root,text="6",padx=40,pady=20,font=10,command=lambda :buttonclick(6),bg="black",fg="white")
button_7=Button(root,text="7",padx=40,pady=20,font=10,command=lambda :buttonclick(7),bg="black",fg="white")
button_8=Button(root,text="8",padx=40,font=10,pady=20,command=lambda :buttonclick(8),bg="black",fg="white")
button_9=Button(root,text="9",padx=40,pady=20,font=10,command=lambda :buttonclick(9),bg="black",fg="white")

button_add=Button(root,text="+",font=10,padx=36.5,pady=20,command=buttonadd ,bg="purple",fg="white")

button_equal=Button(root,text="=",font=10,padx=39.5,pady=20,command=buttonequal ,bg="green",fg="white")

button_clear=Button(root,text="Clear",font=10,padx=22,pady=20,command=lambda :buttonclear(),fg="white",bg="darkred")

button_sub=Button(root,text="-",padx=39.5,font=10,pady=20,command=buttonsub, bg="purple",fg="white")

button_div=Button(root,text="/",padx=40,font=10,pady=20,command=buttondiv, bg="purple",fg="white")

button_mul=Button(root,text="*",padx=39,font=10,pady=20,command=buttonmul,bg="purple",fg="white")

button_9.grid(row=1,column=2)
button_8.grid(row=1,column=1)
button_7.grid(row=1,column=0)

button_6.grid(row=2,column=2)
button_5.grid(row=2,column=1)
button_4.grid(row=2,column=0)

button_3.grid(row=3,column=2)
button_2.grid(row=3,column=1)
button_1.grid(row=3,column=0)

button_0.grid(row=4,column=0)
button_clear.grid(row =4 ,column=1)
button_add.grid(row=4,column=3)
button_equal.grid(row=4,column=2)
button_sub.grid(row=3,column=3)
button_div.grid(row=1,column=3)
button_mul.grid(row=2,column=3)
root.mainloop()


# In[273]:


# Function to evaluate the final expression 
def equalpress(): 
    # Try and except statement is used 
    # for handling the errors like zero 
    # division error etc. 
  
    # Put that code inside the try block 
    # which may generate the error 
    try: 
  
        global expression 
  
        # eval function evaluate the expression 
        # and str function convert the result 
        # into string 
        total = str(eval(expression)) 
  
        equation.set(total) 
  
        # initialze the expression variable 
        # by empty string 
        expression = "" 
  
    # if error is generate then handle 
    # by the except block 
    except: 
  
        equation.set(" error ") 
        expression = "" 
  
  
# Function to clear the contents 
# of text entry box 
def clear(): 
    global expression 
    expression = "" 
    equation.set("") 
  
  
# Driver code 
if __name__ == "__main__": 
    # create a GUI window 
    gui = Tk() 
  
    # set the background colour of GUI window 
    gui.configure(background="light green") 
  
    # set the title of GUI window 
    gui.title("Simple Calculator") 
  
    # set the configuration of GUI window 
    gui.geometry("265x125") 
  
    # StringVar() is the variable class 
    # we create an instance of this class 
    equation = StringVar() 
  
    # create the text entry box for 
    # showing the expression . 
    expression_field = Entry(gui, textvariable=equation) 
  
    # grid method is used for placing 
    # the widgets at respective positions 
    # in table like structure . 
    expression_field.grid(columnspan=4, ipadx=70) 
  
    equation.set('enter your expression') 
  
    # create a Buttons and place at a particular 
    # location inside the root window . 
    # when user press the button, the command or 
    # function affiliated to that button is executed . 
    button1 = Button(gui, text=' 1 ', fg='black', bg='red', 
                     command=lambda: press(1), height=1, width=7) 
    button1.grid(row=2, column=0) 
  
    button2 = Button(gui, text=' 2 ', fg='black', bg='red', 
                     command=lambda: press(2), height=1, width=7) 
    button2.grid(row=2, column=1) 
  
    button3 = Button(gui, text=' 3 ', fg='black', bg='red', 
                     command=lambda: press(3), height=1, width=7) 
    button3.grid(row=2, column=2) 
  
    button4 = Button(gui, text=' 4 ', fg='black', bg='red', 
                     command=lambda: press(4), height=1, width=7) 
    button4.grid(row=3, column=0) 
  
    button5 = Button(gui, text=' 5 ', fg='black', bg='red', 
                     command=lambda: press(5), height=1, width=7) 
    button5.grid(row=3, column=1) 
  
    button6 = Button(gui, text=' 6 ', fg='black', bg='red', 
                     command=lambda: press(6), height=1, width=7) 
    button6.grid(row=3, column=2) 
  
    button7 = Button(gui, text=' 7 ', fg='black', bg='red', 
                     command=lambda: press(7), height=1, width=7) 
    button7.grid(row=4, column=0) 
  
    button8 = Button(gui, text=' 8 ', fg='black', bg='red', 
                     command=lambda: press(8), height=1, width=7) 
    button8.grid(row=4, column=1) 
  
    button9 = Button(gui, text=' 9 ', fg='black', bg='red', 
                     command=lambda: press(9), height=1, width=7) 
    button9.grid(row=4, column=2) 
  
    button0 = Button(gui, text=' 0 ', fg='black', bg='red', 
                     command=lambda: press(0), height=1, width=7) 
    button0.grid(row=5, column=0) 
  
    plus = Button(gui, text=' + ', fg='black', bg='red', 
                  command=lambda: press("+"), height=1, width=7) 
    plus.grid(row=2, column=3) 
  
    minus = Button(gui, text=' - ', fg='black', bg='red', 
                   command=lambda: press("-"), height=1, width=7) 
    minus.grid(row=3, column=3) 
  
    multiply = Button(gui, text=' * ', fg='black', bg='red', 
                      command=lambda: press("*"), height=1, width=7) 
    multiply.grid(row=4, column=3) 
  
    divide = Button(gui, text=' / ', fg='black', bg='red', 
                    command=lambda: press("/"), height=1, width=7) 
    divide.grid(row=5, column=3) 
  
    equal = Button(gui, text=' = ', fg='black', bg='red', 
                   command=equalpress, height=1, width=7) 
    equal.grid(row=5, column=2) 
  
    clear = Button(gui, text='Clear', fg='black', bg='red', 
                   command=clear, height=1, width=7) 
    clear.grid(row=5, column='1') 
  
    # start the GUI 
    gui.mainloop() 


# In[2]:


import tkinter as tk
from tkinter import ttk

exp = " "
def press(num):
    global exp
    exp+=str(num)
    equation.set(exp)

def equalpress():
    try:
        global exp
        total = str(eval(exp))
        equation.set(total)
        exp = " "
    except:
        equation.set('error')
        exp = " "


def clear ():
    global exp
    exp = " "
    equation.set(" ")



if __name__ == "__main__":


    dk = tk.Tk()
    dk.title('Calculator')
    #dk.iconbitmap('C:\\Users\\Admin\\PycharmProjects\\DANISH\\venv\calculator.ico')
    dk.geometry('258x170')
    dk.maxsize(width=258,height=170)

    dk.configure(bg='blue')

    # imp


equation = tk.StringVar()
dis_entry = ttk.Entry(dk,width = 40, state = 'readonly', background ='red', textvariable = equation)
dis_entry.grid(row = 0 , columnspan = 10, ipadx = 6 , ipady = 8)
dis_entry.focus()


btn7 = ttk.Button(dk, text = '7' , width = 5 ,  command = lambda : press(7) )
btn7.grid(row = 1 , column = 0 ,ipady = 4 , ipadx = 2)

btn8 = ttk.Button(dk, text = '8' , width = 5 ,  command = lambda : press(8) )
btn8.grid(row = 1 , column = 1 ,ipady = 4, ipadx = 2)

btn9 = ttk.Button(dk, text = '9' , width = 5 ,  command = lambda : press(9) )
btn9.grid(row = 1 , column = 2,ipady = 4, ipadx = 2)

btnmines = ttk.Button(dk, text = '-' , width = 8 ,  command = lambda : press('-') )
btnmines.grid(row = 1 , column = 3 , ipady = 3, ipadx = 2)

btnmul = ttk.Button(dk, text = '*' , width = 8 ,  command = lambda : press("*") )
btnmul.grid(row = 1 , column = 4 , ipady = 3, ipadx = 2)

btn4 = ttk.Button(dk, text = '4' , width = 5 ,  command = lambda : press(4) )
btn4.grid(row = 2 , column = 0 ,ipady = 4 , ipadx = 2)

btn5 = ttk.Button(dk, text = '5' , width = 5 ,  command = lambda : press(5) )
btn5.grid(row = 2 , column = 1 ,ipady = 4, ipadx = 2)

btn6 = ttk.Button(dk, text = '6' , width = 5 ,  command = lambda : press(6) )
btn6.grid(row = 2 , column = 2,ipady = 4, ipadx = 3)



btnplus = ttk.Button(dk, text = '+' , width = 5 ,  command = lambda : press("+") )
btnplus.grid(row = 2 , column = 3,ipady = 4, ipadx = 10)



btndiv = ttk.Button(dk, text = '/' , width = 5 ,  command = lambda : press("/")  )
btndiv.grid(row = 2 , column = 4,ipady = 4, ipadx = 10)



btnequal = ttk.Button(dk, text = 'Enter' , width = 5,  command = equalpress )
btnequal.grid(row = 3 , column = 4,ipady = 4, ipadx = 10)



btn0= ttk.Button(dk, text = '0' , width = 5,  command = lambda : press(0)  )
btn0.grid(row = 3 , column = 3,ipady = 4, ipadx = 10)



btn3 = ttk.Button(dk, text = '3' , width = 5,  command = lambda : press(3)  )
btn3.grid(row = 3 , column = 0 ,ipady = 4 , ipadx = 2)


btn2 = ttk.Button(dk, text = '2' , width = 5,  command = lambda : press(2)  )
btn2.grid(row = 3 , column = 1 ,ipady = 4, ipadx = 2)





btn1 = ttk.Button(dk, text = '1' , width = 5 ,  command = lambda : press(1) )
btn1.grid(row = 3 , column = 2,ipady = 4, ipadx = 2)


btnclr = ttk.Button(dk, text = 'Clear' , width = 5 ,  command = clear )
btnclr.grid(row = 4 , columnspan = 6,ipady = 4, ipadx = 108)



dk.mainloop()


# In[1]:


from tkinter import *
root=Tk()
root.iconbitmap("C:/Users/nikhi/Downloads/Google-Noto-Emoji-People-Bodyparts-11947-middle-finger-light-skin-tone.ico")
root.title("Image or icon")
root.mainloop()


# In[2]:


from tkinter import *
root=Tk()
root.title("Exit program")
button_quit=Button(root,text="Quit",fg="green",bg="red",command=root.quit)
button_quit.pack()

root.mainloop()


# In[7]:


from tkinter import *
from PIL import ImageTk,Image
root=Tk()
my_img=ImageTk.PhotoImage(Image.open ("Google-Noto-Emoji-People-Bodyparts-11947-middle-finger-light-skin-tone.ico"))
my_lbl=Label(image=my_img)
my_lbl.pack()
root.iconbitmap("Google-Noto-Emoji-People-Bodyparts-11947-middle-finger-light-skin-tone.ico")
root.title("Image and icon")
root.mainloop()


# In[ ]:


import tkinter
parent_widget = tkinter.Tk()
def menu_callback():
    print("I'm in the menu callback!")
def submenu_callback():
    print("I'm in the submenu callback!")
menu_widget = tkinter.Menu(parent_widget)
submenu_widget = tkinter.Menu(menu_widget, tearoff=False)
submenu_widget.add_command(label="Submenu Item1",
                           command=submenu_callback)
submenu_widget.add_command(label="Submenu Item2",
                           command=submenu_callback)
menu_widget.add_cascade(label="Item1", menu=submenu_widget)
menu_widget.add_command(label="Item2",
                        command=menu_callback)
menu_widget.add_command(label="Item3",
                        command=menu_callback)
parent_widget.config(menu=menu_widget)
tkinter.mainloop()


# In[15]:


from tkinter import *
root=Tk()
entry=Entry(root,text="Enter me").pack()
#entry.insert(0,"hello")
root.mainloop()


# In[1]:


def pour(jug1, jug2):
    max1, max2, goal = 3, 5, 4
    print(jug1, jug2)
    if jug2 == goal:
        return
    elif jug1 != 0 and jug2 == 0:
        pour(0, jug1)
    elif jug2 == max2:
        pour(0, jug1)
    elif jug1 == goal:
        pour(jug1, 0)   
    elif jug1 < max1:
        pour(max1, jug2)
    elif jug1 < (max2-jug2):
        pour(0, (jug1+jug2))
    else:
        pour(jug1-(max2-jug2), (max2-jug2)+jug2)
 
pour(0, 0)


# In[3]:


from math import *
banana=3000
x=(banana-2000)/5     #3000-5x=2000  first intermediate point
y=floor((2000-1000)/3)   #2000-3y=1000   second intermediate point
z=1000-x-y       # 1000-x-y  last point
result=1000-z     # finl answer
print(result)


# In[3]:


#exp 1
total=int(input('Enter no. of bananas at starting:\t'))
distance=int(input('Enter distance you want to cover:\t'))
load_capacity=int(input('Enter max load capacity of your camel:\t'))
lose=0
start=total
for i in range(distance):   # the camel moves 1 km at a time 
    while start>0:
        
        start=start-load_capacity
        if start==1:   # to check if camel has 1b left then it moves forward only
            lose=lose-1 
        lose=lose+2     # as the camel travels 1 mile forward and backward
    
    #at the last destination the camel only moves forward
    
    lose=lose-1
    start=total-lose
    #print(start,lose)
    if start==0:
        break
print("Total bananas left : ",start)  


# In[16]:


#exp 2
class Graph:

    def __init__(self, edges, N):
 
        self.adj = [[] for _ in range(N)]

        for (src, dest) in edges:
            self.adj[src].append(dest)
            self.adj[dest].append(src)

def colorGraph(graph):

    result = {}
    for u in range(N):

        assigned = set([result.get(i) for i in graph.adj[u] if i in result])

        color = 1
        for c in assigned:
            if color != c:
                break
            color = color + 1

        result[u] = color
    for v in range(N):
        print("Color assigned to vertex", v, "is", colors[result[v]])

if __name__ == '__main__':
    colors = ["", "BLUE", "GREEN", "RED", "YELLOW", "ORANGE", "PINK",
              "BLACK", "BROWN", "WHITE", "PURPLE", "VOILET"]
    edges = [(0,1),(0,4),(0,5),(4,5),(1,4),(1,3),(2,3),(2,4)]
    N = 6
    graph = Graph(edges, N)
    colorGraph(graph)
 


# In[17]:



print(graph.adj)


# In[1]:


#exp 3   <trial>
import time
import itertools



def solve1():
    for s in range(1, 10):
        for e in range(0, 10):
            for n in range(0, 10):
                for d in range(0, 10):
                    for m in range(1, 10):
                        for o in range(0, 10):
                            for r in range(0, 10):
                                for y in range(0, 10):
                                    if distinct(s, e, n, d, m, o, r, y):
                                        send = 1000 * s + 100 * e + 10 * n + d
                                        more = 1000 * m + 100 * o + 10 * r + e
                                        money = 10000 * m + 1000 * o + 100 * n + 10 * e + y
                                        if send + more == money:
                                            return send, more, money


def distinct(*args):
    return len(set(args)) == len(args)

def solve2():
    #letters = input("Enter your string: ")
    #letters1 = list(letters)
    letters = ('s', 'h', 'o', 'w', 'm', 'e', 't')
    digits = range(10)
    for perm in itertools.permutations(digits, len(letters)):
        sol = dict(zip(letters, perm))
        if sol['s'] == 0 or sol['m'] == 0:
            continue
        send = 1000 * sol['s'] + 100 * sol['e'] + 10 * sol['n'] + sol['d']
        more = 1000 * sol['m'] + 100 * sol['o'] + 10 * sol['r'] + sol['e']
        money = 10000 * sol['m'] + 1000 * sol['o'] + 100 * sol['n'] + 10 * sol['e'] + sol['y']
        if send + more == money:
            return send, more, money


print(solve1())
print(solve2())


# In[1]:


#exp 3 <correct>
import itertools
first = input('Enter the first string: ')
one = first
second = input('Enter the second string: ')
two = second
ans = input('Enter the answer string: ')
answer = ans
numbers = range(10)
first = [i for i in first]
second = [i for i in second]
ans = [i for i in ans]
letters = []
for item in first:
    letters.append(item)
for item in second:
    letters.append(item)
for item in ans:
    letters.append(item)
letters = list(set(letters))
for p in itertools.permutations(numbers, len(letters)):
    s = dict(zip(letters,p))
    if s[first[0]]==0 or s[second[0]]==0:
        continue
    send = 1000 * s[first[0]] + 100 * s[first[1]] + 10 * s[first[2]] + s[first[3]]
    more = 1000 * s[second[0]] + 100 * s[second[1]] + 10 * s[second[2]] + s[second[3]]
    money = 10000 * s[ans[0]] + 1000 * s[ans[1]] + 100 * s[ans[2]] + 10 * s[ans[3]] + s[ans[4]]        
    if send + more == money:
        print(one,': ',send)
        print(two,': ',more)
        print(answer,': ',money)


# In[2]:


print(s)
print(letters)


# In[1]:


#Exp 4
#dfs
from collections import defaultdict
class Graph:
    def __init__(self):
         self.graph = defaultdict(list)
    def addEdge(self, u, v):
        self.graph[u].append(v)
    def DFSUtil(self, v, visited):
        visited.add(v)
        print(v, end=' ')
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)
 

    def DFS(self, v):
 

        visited = set()

        self.DFSUtil(v, visited)


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
 
print("Following is DFS from (starting from vertex 2)")
g.DFS(2)


# In[2]:


#bfs

from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)
    def BFS(self, s):
        visited = [False] * (max(self.graph) + 1)
        queue = []
        queue.append(s)
        visited[s] = True
        while queue:
            s = queue.pop(0)
            print (s, end = " ")
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

                    
#input the edges for the graph                    
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
 
print ("Following is Breadth First Traversal"
                  " (starting from vertex 2)")
g.BFS(2)


# In[17]:


# ex 5: best first search
from queue import PriorityQueue
v = 14
graph = [[] for i in range(v)]

def best_first_search(source, target, n):
    visited = [0] * n
    visited = True
    pq = PriorityQueue()
    pq.put((0, source))
    while pq.empty() == False:
        u = pq.get()[1]
        # Displaying the path having lowest cost
        print(u, end=" ")
        if u == target:
            break
        for v, c in graph[u]:
            if visited[v] == False:
                visited[v] = True
                pq.put((c, v))
    print()
def addedge(x, y, cost):
    graph[x].append((y, cost))
    graph[y].append((x, cost))

addedge(0, 1, 3)
addedge(0, 2, 6)
addedge(0, 3, 5)
addedge(1, 4, 9)
addedge(1, 5, 8)
addedge(2, 6, 12)
addedge(2, 7, 14)
addedge(3, 8, 7)
addedge(8, 9, 5)
addedge(8, 10, 6)
addedge(9, 11, 1)
addedge(9, 12, 10)
addedge(9, 13, 2)
 
source = 0
target = 9
best_first_search(source, target, v)


# In[1]:


#ex 5 - A*
class Node():
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def astar(maze, start, end):

    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    open_list = []
    closed_list = []
    open_list.append(start_node)

    while len(open_list) > 0:
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        open_list.pop(current_index)
        closed_list.append(current_node)
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]

        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue
            if maze[node_position[0]][node_position[1]] != 0:
                continue
            new_node = Node(current_node, node_position)
            children.append(new_node)

        for child in children:
            for closed_child in closed_list:
                if child == closed_child:
                    continue
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue
            open_list.append(child)

maze = [[0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]]

start = (0, 0)
end = (0, 3)

path = astar(maze, start, end)
print(path)


# In[1]:


#exp 6 - tick tack
from math import inf as infinity
from random import choice
import platform
import time
from os import system

HUMAN = -1
COMP = +1
board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]


def evaluate(state):
    
    if wins(state, COMP):
        score = +1
    elif wins(state, HUMAN):
        score = -1
    else:
        score = 0

    return score


def wins(state, player):
    
    win_state = [
        [state[0][0], state[0][1], state[0][2]],
        [state[1][0], state[1][1], state[1][2]],
        [state[2][0], state[2][1], state[2][2]],
        [state[0][0], state[1][0], state[2][0]],
        [state[0][1], state[1][1], state[2][1]],
        [state[0][2], state[1][2], state[2][2]],
        [state[0][0], state[1][1], state[2][2]],
        [state[2][0], state[1][1], state[0][2]],
    ]
    if [player, player, player] in win_state:
        return True
    else:
        return False


def game_over(state):
    
    return wins(state, HUMAN) or wins(state, COMP)


def empty_cells(state):
    
    cells = []

    for x, row in enumerate(state):
        for y, cell in enumerate(row):
            if cell == 0:
                cells.append([x, y])

    return cells


def valid_move(x, y):
    
    if [x, y] in empty_cells(board):
        return True
    else:
        return False


def set_move(x, y, player):
    
    if valid_move(x, y):
        board[x][y] = player
        return True
    else:
        return False


def minimax(state, depth, player):
    
    if player == COMP:
        best = [-1, -1, -infinity]
    else:
        best = [-1, -1, +infinity]

    if depth == 0 or game_over(state):
        score = evaluate(state)
        return [-1, -1, score]

    for cell in empty_cells(state):
        x, y = cell[0], cell[1]
        state[x][y] = player
        score = minimax(state, depth - 1, -player)
        state[x][y] = 0
        score[0], score[1] = x, y

        if player == COMP:
            if score[2] > best[2]:
                best = score  # max value
        else:
            if score[2] < best[2]:
                best = score  # min value

    return best


def clean():
    """
    Clears the console
    """
    os_name = platform.system().lower()
    if 'windows' in os_name:
        system('cls')
    else:
        system('clear')


def render(state, c_choice, h_choice):
    

    chars = {
        -1: h_choice,
        +1: c_choice,
        0: ' '
    }
    str_line = '---------------'

    print('\n' + str_line)
    for row in state:
        for cell in row:
            symbol = chars[cell]
            print(f'| {symbol} |', end='')
        print('\n' + str_line)


def ai_turn(c_choice, h_choice):
    
    depth = len(empty_cells(board))
    if depth == 0 or game_over(board):
        return

    clean()
    print(f'Computer turn [{c_choice}]')
    render(board, c_choice, h_choice)

    if depth == 9:
        x = choice([0, 1, 2])
        y = choice([0, 1, 2])
    else:
        move = minimax(board, depth, COMP)
        x, y = move[0], move[1]

    set_move(x, y, COMP)
    time.sleep(1)


def human_turn(c_choice, h_choice):
    
    depth = len(empty_cells(board))
    if depth == 0 or game_over(board):
        return

    # Dictionary of valid moves
    move = -1
    moves = {
        1: [0, 0], 2: [0, 1], 3: [0, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        7: [2, 0], 8: [2, 1], 9: [2, 2],
    }

    clean()
    print(f'Human turn [{h_choice}]')
    render(board, c_choice, h_choice)

    while move < 1 or move > 9:
        try:
            move = int(input('Use numpad (1..9): '))
            coord = moves[move]
            can_move = set_move(coord[0], coord[1], HUMAN)

            if not can_move:
                print('Bad move')
                move = -1
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')


def main():
    """
    Main function that calls all functions
    """
    clean()
    h_choice = ''  # X or O
    c_choice = ''  # X or O
    first = ''  # if human is the first

    # Human chooses X or O to play
    while h_choice != 'O' and h_choice != 'X':
        try:
            print('')
            h_choice = input('Choose X or O\nChosen: ').upper()
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')

    # Setting computer's choice
    if h_choice == 'X':
        c_choice = 'O'
    else:
        c_choice = 'X'

    # Human may starts first
    clean()
    while first != 'Y' and first != 'N':
        try:
            first = input('First to start?[y/n]: ').upper()
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')

    # Main loop of this game
    while len(empty_cells(board)) > 0 and not game_over(board):
        if first == 'N':
            ai_turn(c_choice, h_choice)
            first = ''

        human_turn(c_choice, h_choice)
        ai_turn(c_choice, h_choice)

    # Game over message
    if wins(board, HUMAN):
        clean()
        print(f'Human turn [{h_choice}]')
        render(board, c_choice, h_choice)
        print('YOU WIN!')
    elif wins(board, COMP):
        clean()
        print(f'Computer turn [{c_choice}]')
        render(board, c_choice, h_choice)
        print('YOU LOSE!')
    else:
        clean()
        render(board, c_choice, h_choice)
        print('DRAW!')

    exit()


if __name__ == '__main__':
    main()


# In[11]:


import os
print(os.getcwd())


# In[4]:


# exp 7

class Substitution:
	def _init_(self, variable, replacement):
		self.variable = variable
		self.replacement = replacement

	def _str_(self):
		return str(self.variable) + " = " + str(self.replacement)

		
class Variable:
    def _init_(self, variable_name):
        """
        Initialize a variable with the given name.
        The name should start with an upper-case letter.
        """
        if variable_name[0].islower(): raise (Exception("Variable name starting with lower-case!"))
        self.variable_name = variable_name

    def _eq_(self, other):
        """
        Checks whether self and other represent the same variable.
        Two variables are the same if they have the same name.
        """
        return isinstance(other, Variable) and self.variable_name == other.variable_name

    def _ne_(self, other):
        """
        Checks whether self and other represent different variables.
        """
        return not self._eq_(other)

    def _str_(self):
        """
        Returns a string representation of the variable.
        """
        return self.variable_name

    def _repr_(self):
        """
        Returns a string representation of the variable.
        """
        return str(self)

    def _hash_(self):
        """
        Produces a hash of the variable so it can be stored in a dictionary.
        """
        return str(self)._hash_()

    def occurs_in(self, other):
        """
        Recursively performs the "occurs check" during unification.
        If self represents the same variable as other, returns True.
        Else if other is an instance of Expression,
        and self occurs in one or more of other's arguments, returns True.
        Otherwise, returns False.
        """
        if isinstance(other, Variable) and self._eq_(other):
            return True
        if isinstance(other, Expression) and self._str() in other.str_():
            return True
        return False


class Constant:
    def _init_(self, constant_name):
        """
        Initialize a constant with the given name.
        The name should start with a lower-case letter.
        """
        if constant_name[0].isupper(): raise (Exception("Constant name starting with upper-case!"))
        self.constant_name = constant_name

    def _eq_(self, other):
        """
        Checks whether self and other represent the same constant.
        Two constants are the same if they have the same name.
        """
        return isinstance(other, Constant) and self.constant_name == other.constant_name

    def _ne_(self, other):
        """
        Checks whether self and other represent different constants.
        """
        return not self._eq_(other)

    def _str_(self):
        """
        Returns a string representation of the constant.
        """
        return self.constant_name

    def _repr_(self):
        """
        Returns a string representation of the constant.
        """
        return str(self)

    def _hash_(self):
        """
        Produces a hash of the constant so it can be stored in a dictionary.
        """
        return str(self)._hash_()


class Expression:
    """
    Represents a compound FOL expression with a top-level function or predicate symbol.
    The "operator" field is the top-level function or predicate symbol.
    The "arguments" field is a list of Constants, Variables, and/or Expression objects.
    """

    def _init_(self, operator, arguments):
        """
        operator: a function or predicate symbol (a string)
        arguments: a list of Constants, Variables, and/or Expression objects.
        """
        self.operator = operator
        self.arguments = arguments

    def _str_(self):
        """
        Returns a string representation of the expression.
        """
        return "%s(%s)" % (
            self.operator,
            ", ".join(map(str, self.arguments)))

    def _repr_(self):
        """
        Returns a string representation of the expression.
        """
        return str(self)

    def _hash_(self):
        """
        Produces a hash of the expression so it can be stored in a dictionary.
        """
        return str(self)._hash_()

    def _eq_(self, other):
        """
        Checks whether self and other represent the same expression.
        Two expressions are the same if they have the same operator
        and each of their respective arguments are the same.
        """
        if not isinstance(other, Expression): return False
        if self.operator != other.operator: return False
        if len(self.arguments) != len(other.arguments): return False
        return all([a1 == a2 for a1, a2 in zip(self.arguments, other.arguments)])

    def _ne_(self, other):
        """
        Checks whether self and other represent different expressions.
        """
        return not self._eq_(other)


def parse_expression(s):
    """
    Parses a string s and returns a corresponding expression object.
    Assumes arguments are separated by commas and zero or more whitespace.
    """
    l, d, i = [], 0, 0
    op, args = None, []
    for j, c in enumerate(s):
        if c == "(":
            if op is None:
                op = s[:j]
                i = j + 1
            d += 1
        if c == ")":
            if d == 1:
                if j > i: args.append(s[i:j])
                i = j + 1
            d -= 1
        if c == "," and d == 1:
            args.append(s[i:j])
            i = j + 1
        if c == " " and i == j: i += 1

    if op is None:
        if s[0].isupper():
            return Variable(s)
        else:
            return Constant(s)

    return Expression(op, list(map(parse_expression, args)))



def unify_with_occurrence_check(formular1, formular2, mgu = [], trace = False):
	#pp(trace, "Unifying expression:", formular1, "with expression:", formular2)
	if mgu is None:
		return None
	elif formular1 == formular2:
		return mgu
	elif isinstance(formular1, Variable):
		return unify_variable(formular1, formular2, mgu, trace)
	elif isinstance(formular2, Variable):
		return unify_variable(formular2, formular1, mgu, trace)
	elif isinstance(formular1, Expression) and isinstance(formular2, Expression):
		if type(formular1) != type(formular2) or formular1.operator != formular2.operator or len(formular1.arguments) != len(formular2.arguments):
			return None
		else:
			for a,b in zip(formular1.arguments, formular2.arguments):
				mgu = unify_with_occurrence_check(a, b, mgu, trace)
			return mgu
	else:
		return None
		
		
		
def substitute(sub, expr):
	"""
    This method applies substituition to sub and expr; which replaces
	on with the other.
    """	
	for s in (x for x in sub if occurs_in(x.variable, expr)):
		if isinstance(expr, Variable):
			expr = s.replacement
		else:
			expr.arguments = [substitute(sub, e) for e in expr.arguments]
	return expr


def occurs_in(var, expr):
	"""
	Return true if variable var occurs anywhere in expr
	"""
	if var == expr:
		return True
	if not isinstance(expr, Expression):
		return False
	return any([occurs_in(var, e) for e in expr.arguments])
  
  
  
def unify_variable(var, exp, mgu, trace):
	#pp(trace, "Unifying variable:", var, "with expression:", exp)
	for s in (x for x in mgu if x.variable == var):
		return unify_with_occurrence_check(s.replacement, exp, mgu, trace)
	t = substitute(mgu, exp)
	if occurs_in(var, t) and isinstance(t, Expression):
		print("\nCannot unify - infinte loop exception!!!")
		return None
	else:
		s = Substitution(var, t)
		mgu = mgu+[s]
		for q in (x for x in mgu if x.replacement == s.variable):
			mgu.remove(q)
			new  = Substitution(q.variable, s.replacement)
			mgu = mgu+[new]
		for r in (x for x in mgu if isinstance(x.replacement, Expression)):
			mgu.remove(r)
			a = substitute(mgu, r.replacement)
			b = Substitution(r.variable, a)
			mgu = mgu+[b]
		for s in (x for x in mgu if (x.variable == x.replacement)):
			#print("Variable already unified, duplicate deleted!!!")
			mgu.remove(s)
		#pp(trace, "MGU now is: ", ", ".join(map(str, mgu)))
		return mgu


def main():

	keep_running = True

	while keep_running:
  
		print("\nPlease enter the first term:")
		t1 = input("-->")
		print("\nPlease enter the second term:")
		t2 = input("-->")
		
	
		#mgu: Most General Unifier
		mgu = unify_with_occurrence_check(parse_expression(t1), parse_expression(t2), trace = False)	
		if mgu is None:
			print("\nno")
		else:
			print("\n")
			print("\n".join(map(str, mgu)))
			print("\nyes")
  
  
		print("\n\n>>> Do you want to run unifier again? (Y/N)")
		re_run = input("--> ")

		if re_run != "y" and re_run != "Y":
			keep_running = False
		
		
# Run main
if __name__ == "__main__":
	main()


# In[5]:


#exp 7 alter
def unify(E1, E2):
    constants = [chr(i) for i in range(ord('a'), ord('w') + 1)]
    variables = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    variables.extend(['x', 'y', 'z'])
    if (E1 in constants and E2 in constants) or (E1 is None and E2 is None):  # base case
        if E1 == E2:
            return None
        else:
            return "FAIL"

    elif E1 in variables:
        if E1 in E2:
            return "FAIL - E1 occurs in E2"
        else: 
            return (E2 + "/" + E1)
          
    elif E2 in variables:
        if E2 in E1:
            return "FAIL - E2 occurs in E1"
        else: 
            return (E1 + "/" + E2)
    else:
        if ('(' in E1 and '(' not in E2):
            return "FAIL - E1 is a function and E2 is a variable/constant"
        elif ('(' not in E1 and '(' in E2):
            return "FAIL - E1 is a variable/constant and E2 is a function"

print("Enter the Expressions (without spaces):")
s1 = input()
s2 = input()
E1 = s1[2:len(s1)-1].split(',')
E2 = s2[2:len(s2)-1].split(',')
if s1[0] != s2[0]:
    print("FAIL - Initial Predicate Symbols in E1 and E2 are not identical")
elif len(E1) != len(E2):
    print("FAIL - E1 and E2 have different number of arguments")
else:
    n = len(E1)
    s = []   # General Unifiers
    print("----------------------------------------------------------------------------")
    for i in range(n):
        print("E1:", E1[i])
        print("E2:", E2[i])
        print("Result:", unify(E1[i],E2[i]))
        print("----------------------------------------------------------------------------")
        if "FAIL" not in unify(E1[i],E2[i]):
            s.append(unify(E1[i],E2[i]))
        
    if len(s) == n:
        print("General Unifiers: { ", end = "")
        for i in range(len(s)):
            if i != len(s)-1:
                print(s[i] + ", ", end = "")
            else:
                print(s[i] + " }", end = "")


# In[2]:


#EXp-8
SIZE = 9
#sudoku problem
#cells with value 0 are vacant cells
matrix = [
    [6,5,0,8,7,3,0,9,0],
    [0,0,3,2,5,0,0,0,8],
    [9,8,0,1,0,4,3,5,7],
    [1,0,5,0,0,0,0,0,0],
    [4,0,0,0,0,0,0,0,2],
    [0,0,0,0,0,0,5,0,3],
    [5,7,8,3,0,1,0,2,6],
    [2,0,0,0,4,8,9,0,0],
    [0,9,0,6,2,5,0,8,1]]

#function to print sudoku
def print_sudoku():
    for i in matrix:
        print (i)

def number_unassigned(row, col):
    num_unassign = 0
    for i in range(0,SIZE):
        for j in range (0,SIZE):
            #cell is unassigned
            if matrix[i][j] == 0:
                row = i
                col = j
                num_unassign = 1
                a = [row, col, num_unassign]
                return a
    a = [-1, -1, num_unassign]
    return a

def is_safe(n, r, c):
    #checking in row
    for i in range(0,SIZE):
        #there is a cell with same value
        if matrix[r][i] == n:
            return False
    #checking in column
    for i in range(0,SIZE):
        #there is a cell with same value
        if matrix[i][c] == n:
            return False
    row_start = (r//3)*3
    col_start = (c//3)*3;
    #checking submatrix
    for i in range(row_start,row_start+3):
        for j in range(col_start,col_start+3):
            if matrix[i][j]==n:
                return False
    return True

def solve_sudoku():
    row = 0
    col = 0
    
    a = number_unassigned(row, col)
    if a[2] == 0:
        return True
    row = a[0]
    col = a[1]
    #number between 1 to 9
    for i in range(1,10):
        #if we can assign i to the cell or not
        #the cell is matrix[row][col]
        if is_safe(i, row, col):
            matrix[row][col] = i
            #backtracking
            if solve_sudoku():
                return True
            #f we can't proceed with this solution
            #reassign the cell
            matrix[row][col]=0
    return False

if solve_sudoku():
    print("The final sudoko solution is -->\n")
    print_sudoku()
else:
    print("No solution")


# In[2]:


# Monty Hall Game in Python    exp -9
import random

def play_monty_hall(choice):
    prizes = ['goat', 'car', 'goat']
    random.shuffle(prizes) 
    
    while True:
        opening_door = random.randrange(len(prizes))
        if prizes[opening_door] != 'car' and choice-1 != opening_door:
            break
    
    opening_door = opening_door + 1
    print('We are opening the door number-%d' % (opening_door))
    
    # Determining switching door
    options = [1,2,3]
    options.remove(choice)
    options.remove(opening_door)
    switching_door = options[0]
    
    # Asking for switching the option
    print('Now, do you want to switch to door number-%d? (yes/no)' %(switching_door))
    answer = input()
    if answer == 'yes':
        result = switching_door - 1
    else:
        result = choice - 1
        
    print('And your prize is ....', prizes[result].upper())

choice = int(input('Which door do you want to choose? (1,2,3): '))

# Playing game
play_monty_hall(choice)


# In[ ]:


import re
from itertools import permutations
from collections import deque
from sys import argv, exit
from time import perf_counter
from copy import deepcopy

def openProblem():

    objects = ['E', 'G', 'C', 'D', 'F', 'A', 'B']
    initTemp = [('CLEAR', 'B', ''), ('CLEAR', 'A', ''), ('ONTABLE', 'F', ''), ('ONTABLE', 'D', ''),
                ('ON', 'B', 'C'), ('ON', 'C', 'G'), ('ON', 'G', 'E'), ('ON', 'E', 'F'), ('ON', 'A', 'D')]
    goalTemp = [('E', 'B'), ('B', 'F'), ('F', 'D'),
                ('D', 'A'), ('A', 'C'), ('C', 'G')]

    init = {i: ['table', True] for i in objects}

    print('Init Temp', initTemp)
    print('Goal Temp', goalTemp)
    print('objects', objects)

    # print()

    for item in initTemp:
        if item[0] == 'ON':
            init[item[1]][0] = item[2]
            init[item[2]][1] = False
        # unessecary, but left for readability
        # elif item[0] == 'ONTABLE':
        #    state[item[1]][0] = 'table'
        # elif item[0] == 'CLEAR':
        #    state[item[1]][1] = True
        #####################################

    # Initialize goal and their state (position, is clear).
    goal = {i: ['table', True] for i in objects}

    # For each item that's is on another, change it's location
    # and set to unclear.
    for item in goalTemp:
        goal[item[0]][0] = item[1]
        goal[item[1]][1] = False

    return init, goal, objects

def writeSolution(solution):
    print('\n')
    i = 0
    for move in solution:
        i += 1
        print('{}. Move({}, {}, {})\n' .format(
            i, move[0], move[1], move[2]))

class State(object):
    """
        description
            A state's description dictionary looks like this...
            {'A': ['B', True], 'C': ['table', True], 'B': ['table', False]}

            And represents...
            'That cube': ['is on top of that', is it clear on top?]

            And if we visualize it, it looks like this...
             ___
            | A |
            |___|  ___
            | B | | C |
            |___| |___|
            ====================== <-- table

        parent
            The parent state object.

        move
            The move that was required to form that state from parent state.
            The list has the following format...
            ['A', 'B', 'C'] or ['A', 'B', 'table']
            ...which means, move cube A, from cube, on top of cube C or table.
    """

    def __init__(self, description=None, parent=None, move=None):
        super(State, self).__init__()
        self._parent = parent
        self._moveToForm = move

        # If no initial state description is given, try to create it,
        # by following the move that this state was given to form itself.
        if not description:
            self._stateDescription = deepcopy(self._parent._stateDescription)

            # If that move doesn't exists, it probably means, that it's a root state.
            if self._moveToForm is not None:
                self.__move(self._moveToForm[0], self._moveToForm[2])
        # Otherwise, just use the state given as argument.
        else:
            self._stateDescription = description

    # Overriding the equals method, so the comparison of the states is its
    # description dictionary.
    def __eq__(self, other):
        if other is None:
            return False
        return self._stateDescription == other._stateDescription

    # Overriding the representation method, for debugging purposes.
    def __repr__(self):
        return str(self._stateDescription) + '\n'

    def _generateStateChildren(self):
        """
            Generates all possible children (states) of itself (state).
            Each child state represents a possible move.
        """
        # Find all clear cubes of the state.
        clearCubes = [
            key for key in self._stateDescription if self._stateDescription[key][1] is True]

        # Calculate all possible move permutations and
        # add the special case of moving a cube onto table, if it's not already.
        possibleMoves = list(permutations(clearCubes, 2)) + [(
            cube, 'table') for cube in clearCubes if self._stateDescription[cube][0] != 'table']

        # Initialize the final generated children states list.
        states = []

        # For every possible move, create a child state, whose parent is this
        # very state and its move to form is given bt the move method.
        for cubeToMove, destinationCube in possibleMoves:
            states.append(State(parent=self, move=self.__move(
                cubeToMove, destinationCube, True)))

        return states

    def __move(self, object, destination, fake=False):
        """
            Moves the selected object to desired destination and
            returns the action in detail. Optionally,
            it only returns the hypothetical move, without actually doing it.
        """

        # Initialize the initial position of the cube.
        oldPosition = self._stateDescription[object][0]

        # Fake means, that the move is only recorded and not performed.
        # This is useful when we only want the move to form a state
        # from another and then passed as an argument to a new state object.
        if fake:
            return [object, oldPosition, destination]

        # The cube below is now clear, because the cube above it is lifted.
        # Unless it's the table, which is always something we can place on.
        if oldPosition != 'table':
            self._stateDescription[oldPosition][1] = True

        # Cube is now onto destination cube.
        self._stateDescription[object][0] = destination

        # The cube below is now unclear, because the cube above it is placed.
        # Unless it's the table, which is always something we can place on.
        if destination != 'table':
            self._stateDescription[destination][1] = False

        # [move a cube, from that cube, on top of another cube or on table]
        move = [object, oldPosition, destination]

        return move

    def __hash__(self):
        # Creating my own hashing method for the state, which is uniquely
        # identified by the cube, its position and a letter T(rue) or F(alse),
        # which denotes whether the cube is clear above or not.
        string = ''
        for key, value in self._stateDescription.items():
            string += "".join(key + value[0] + str(value[1])[0])
        return hash(string)

    def _tracePath(self):
        """
            Finds the moves required to solve the problem.
        """

        # Initialize the final path list.
        path = []
        # Initialize the current parent as this very state.
        currentParent = self

        # While there is a parent, we have not reached the root...
        while currentParent._parent is not None:
            # Add the move that the current parent required to form to the path.
            path.append(currentParent._moveToForm)
            # Set the current parent, the parent of the it, the grandparent.
            # So, we can go one vertex above, until there is no parent.
            # That means we have reached the root, because it has no parent.
            currentParent = currentParent._parent

        # Invert the order before you return, becase we need
        # the path from the root to the state,
        # but we have the path from this very state
        # (which is probably a solution) to the root.
        return path[::-1]

    def _tracePathDEBUG(self):
        # Just pretty printing the moves to solution.
        i = 0
        for move in self._tracePath():
            i += 1
            print('{}. Move({}, {}, {})' .format(i, move[0], move[1], move[2]))

def breadthFirstSearch(initialState, goalState, timeout=60):
    # Initialize iterations counter.
    iterations = 0

    # Initialize visited vertexes as set, because it's faster to check
    # if an item exists, due to O(1) searching complexity on average case.
    # The items here are hashable state objects.
    # A list, has O(n) on average case, when searching for an item existence.
    #
    # Initialize the search queue which is a double-ended queue and has O(1)
    # complexity on average case when popping an item from it's left.
    # A list has O(n) on average case, when popping from the left,
    # so a deque, improves performance for both ends accesses.
    #
    # source : https://wiki.python.org/moin/TimeComplexity
    visited, queue = set(), deque([initialState])

    # Initialize timeout counter.
    t1 = perf_counter()
    # While there are elements to search for...
    while queue:
        # Initialize on each iteration the performace of the previous.
        t2 = perf_counter()
        # If the the previous iteration has exceeded the allowed time,
        # then return, prematurely, nothing.
        if t2 - t1 > timeout:
            return None, iterations

        iterations += 1
        vertex = queue.popleft()

        if vertex == goalState:
            return vertex._tracePath(), iterations

        for neighbour in vertex._generateStateChildren():
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

def depthFirstSearch(initialState, goalState, timeout=60):
    # Initialize iterations counter.
    iterations = 0

    # Initialize visited vertexes as set, because it's faster to check
    # if an item exists, due to O(1) searching complexity on average case.
    # The items here are hashable state objects.
    # A list, has O(n) on average case, when searching for an item existence.
    #
    # Initialize the search queue which is a double-ended queue and has O(1)
    # complexity on average case when popping an item from it's right.
    # A list has O(1) on average case, when popping from the right,
    # which is the same, but we leave it the same as BFS for readability reasons.
    #
    # source : https://wiki.python.org/moin/TimeComplexity
    visited, stack = set(), deque([initialState])

    # Initialize timeout counter.
    t1 = perf_counter()

    # While there are elements to search for...
    while stack:
        # Initialize on each iteration the performace of the previous.
        t2 = perf_counter()
        # If the the previous iteration has exceeded the allowed time,
        # then return, prematurely, nothing.
        if t2 - t1 > timeout:
            return None, iterations

        iterations += 1
        vertex = stack.pop()  # right

        if vertex == goalState:
            return vertex._tracePath(), iterations

        if vertex in visited:
            continue

        for neighbour in vertex._generateStateChildren():
            stack.append(neighbour)

        visited.add(vertex)

def __distanceFromGoal(currentStates, goalState):
    """ The H function. """

    # Initialize a list of each state's scores.
    statesScores = []

    # For each state in currently discovered states...
    for state in currentStates:

        # Initialize out place blocks.
        outOfPlaceBlocks = 0

        # For each block in every state...
        for block in state._stateDescription:

            # If that block is not positioned correctly, increase out of place
            # blocks for that state.
            if state._stateDescription[block] != goalState._stateDescription[block]:
                outOfPlaceBlocks += 1

        # Store the final score for that state.
        statesScores.append(outOfPlaceBlocks)

    # Return the index of the state with smallest distance from goal.
    return statesScores.index(min(statesScores))

def __distanceFromGoalWithLeastMoves(currentStates, goalState):
    """ The G + H function. """

    # Initialize a list of each state's scores.
    statesScores = []

    # For each state in currently discovered states...
    for state in currentStates:

        # Initialize out place blocks.
        outOfPlaceBlocks = 0

        # For each block in every state...
        for block in state._stateDescription:

            # If that block is not positioned correctly, increase out of place
            # blocks for that state.
            if state._stateDescription[block] != goalState._stateDescription[block]:
                outOfPlaceBlocks += 1

        # Store how many blocks are out of place plus the number of moves
        # needed to reach from root to each state.
        statesScores.append(outOfPlaceBlocks + len(state._tracePath()))

    # Return the index of the state with smallest distance
    # and least moves from goal.
    return statesScores.index(min(statesScores))

def heuristicSearch(initialState, goalState, algorithm='best', timeout=60):
    # Each algorithm uses a different heuristic function for the search.
    if algorithm == 'astar':
        function = __distanceFromGoalWithLeastMoves
    elif algorithm == 'best':
        function = __distanceFromGoal

    # Initialize iterations counter.
    iterations = 0

    # Initialize visited vertexes as set, because it's faster to check
    # if an item exists, due to O(1) searching complexity on average case.
    # The items here are hashable state objects.
    # A list, has O(n) on average case, when searching for an item existence.
    #
    # Initialize the search list.
    # A list has O(n) for popping items on average case.
    # We cannot improve it any further, since we may access items in the middle.
    #
    # source : https://wiki.python.org/moin/TimeComplexity
    visited, list = set(), [initialState]

    # Initialize timeout counter.
    t1 = perf_counter()

    # While there are elements to search for...
    while list:
        # Initialize on each iteration the performace of the previous.
        t2 = perf_counter()
        # If the the previous iteration has exceeded the allowed time,
        # then return, prematurely, nothing.
        if t2 - t1 > timeout:
            return None, iterations

        iterations += 1
        # Determine which item you pop, defined by the heuristic function of
        # the corresponding algorithm.
        item = function(list, goalState)
        vertex = list.pop(item)

        if vertex == goalState:
            return vertex._tracePath(), iterations

        for neighbour in vertex._generateStateChildren():
            if neighbour in visited:
                continue

            visited.add(neighbour)
            list.append(neighbour)

############################

def main(argv):
    # if len(argv) > 4:
    #     print('Usage:\npython3 {} <algorithm> <problem_file_name.pddl> [solution_file_name]' .format(
    #         argv[0]))
    #     exit(1)

    # problemFile = argv[2]
    # outputFile = ''
    # if len(argv) == 4:
    #     outputFile = argv[3]

    init, goal, cubes = openProblem()

    # Initialize inital and goal states.
    initialState = State(init)
    goalState = State(goal)

    algorithm = 'astar'

    t1 = perf_counter()

    if algorithm == 'breadth':
        solution, iters = breadthFirstSearch(initialState, goalState)
    elif algorithm == 'depth':
        solution, iters = depthFirstSearch(initialState, goalState)
    elif algorithm == 'best' or algorithm == 'astar':
        solution, iters = heuristicSearch(initialState, goalState, algorithm)
    else:
        raise Exception(
            'Unknown algorithm. Available : breadth, depth, best, astar')

    t2 = perf_counter()

    # print('| Problem name: {}' .format(' ' * 10 + problemFile))
    print('| Algorithm used: {}' .format(' ' * 8 + algorithm))
    print('| Number of cubes: {}' .format(' ' * 7 + str(len(cubes))))
    print('| Cubes: {}' .format(' ' * 17 + str(' '.join(cubes))))
    if solution:
        print('| Solved in: {}' .format(' ' * 13 + str(t2-t1)))
        print('| Algorithm iterations: {}' .format(' ' * 2 + str(iters)))
        print('| Moves: {}' .format(' ' * 17 + str(len(solution))))

        print('| Solution:' + ' ' * 15 + 'Found!')
        writeSolution(solution)
    else:
        print('| Solution:' + ' ' * 15 + 'NOT found, search timed out.')

if __name__ == '__main__':
    main(argv)

