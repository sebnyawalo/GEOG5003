import sys
import tkinter
import requests
import random
import operator
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot
import matplotlib.animation
import csv
import bs4
import agentframework
import time

# measure the time it takes to execute the code project execution time
begin = time.time()

# sets out the main GUI window
root = tkinter.Tk()
# sets the name of the window 
root.wm_title("ABM-Model")
# define the frame to hold the labels and entry boxes
frame = tkinter.Frame(root, relief=tkinter.RAISED, borderwidth=1)
# use pack layout Geometry to place the frame on the main window
frame.pack(fill=tkinter.BOTH, expand=True)
#  define the entry boxes, sets default values
txt1 = tkinter.Entry(frame)
txt1.insert(0, "10")
# use the get() method to get the value of the entry boxes
num_of_agents = int(txt1.get())

txt1.pack(side=tkinter.RIGHT,padx=5, pady=5)

Lab3 = tkinter.Label(frame, text="neighbourhood")
Lab3.pack(side=tkinter.LEFT,padx=5, pady=5)

txt2 =tkinter.Entry(frame) 
txt2.pack(side=tkinter.LEFT,padx=5, pady=5)
txt2.insert(0, "12")
neighbourhood = int(txt2.get())

Lab2 =tkinter.Label(frame,text="Iterations") 
Lab2.pack(side=tkinter.LEFT,padx=5, pady=5)

txt3 =tkinter.Entry(frame)
txt3.pack(side=tkinter.LEFT,padx=5, pady=5)
txt3.insert(0, "15")
num_of_iterations = int(txt2.get())

Lab1 =tkinter.Label(frame,text="num_of_agents")
Lab1.pack(side=tkinter.LEFT,padx=5, pady=5)
# second frame to hold the canvas
frame1 = tkinter.Frame(root)
frame1.pack(side=tkinter.LEFT,fill=tkinter.BOTH)

environment = []
agents = []

# define the grid to handle the animation
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])


# get the web page 
r = requests.get('https://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html',\
     verify= False)

# grab the webpage content 
content = r.text
# pass the content DOM as python object for proccessing
soup = bs4.BeautifulSoup(content, 'html.parser')
# get all the elements with attribute class y and X
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})

# read image data into envitonment list
with open('in.txt', mode='r') as csv_file:
    file_reader = csv.reader(csv_file, delimiter=",")
 
    for row in file_reader: 
        rowList = []       
        for values in row:
            rowList.append(float(values))
        environment.append(rowList)
        
# write the enviroment to file 
with open("environment_output.txt", "w") as f:
    for line in environment:
        for value in line:
            f.write(str(value) + " ")
        f.write("\n")

# compute the distance between the agents
# Eucledian distance is the distance between two points in Euclidean space
# """ If the points A(x1,y1) and B(x2,y2) are in 2-dimensional space,
#  then the Euclidean distance between them is |AB| = √ ((x2-x1)^2 + (y2-y1)^2)"""

def distance_between(agents_row_a, agents_row_b):
    return((((agents_row_a.x - agents_row_b.y)**2) + ((agents_row_b.x - agents_row_b.y)**2))**0.5)

dist_between_agents = []
for agents_row_a in agents:
    # print(agents_row_a) 
    for agents_row_b in agents:
        # print(agents_row_b)
        # a)Can you find the maximum and minimum distances between your agents?
        # create a new distance list : dist_between_agents
        dist = distance_between(agents_row_a,agents_row_b)
        # append all the distances into this list
        # then we use the max function to find the max value of the list
        dist_between_agents.append(dist)

# Make agents.
for i in range(num_of_agents):
    #  set the values of both y and x to default if theres an error loading the data
    try:
        y = int(td_ys[i].text)
    except:
        y = None
    try:
        x = int(td_xs[i].text)
    except:
        x = None

    agents.append(agentframework.Agent(environment, agents, y, x))
    # shuffle the agents list 
    random.shuffle(agents)
carry_on = True

# update
def update(frame_number):
    
    fig.clear()   

    global carry_on

    # move agents.
    for j in range(num_of_iterations):
        for i in range(num_of_agents):
            random.shuffle(agents)        
            agents[i].move()
            agents[i].eat()
            agents[i].share_with_neighbours(neighbourhood)
            #print agents[i].agents[i]._x # print other agents x

    matplotlib.pyplot.xlim(0, 99)
    matplotlib.pyplot.ylim(0, 99)
    matplotlib.pyplot.imshow(environment)

   

    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i]._x,agents[i]._y)

print("--- %s seconds ---" % (time.time() - begin))
def run():
    # animate
    #animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=num_of_iterations)
    animation = matplotlib.animation.FuncAnimation(fig, update, interval=1)
    canvas.draw()



# button = tkinter.Button(root,text="neighbours")
# button.pack(side=tkinter.LEFT)
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=frame1)
canvas._tkcanvas.pack(side=tkinter.BOTTOM, fill=tkinter.NONE, expand=1)

menu_bar = tkinter.Menu(root)   
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="File", menu=model_menu)
model_menu.add_command(label="Run model", command=run)




tkinter.mainloop() # keep the gui window open until interuption
