
# run from commandline and pass arguments like this pythonpath/python.exe model.py 200 20 30
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

r = requests.get('https://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html',\
     verify= False)

content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')

td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})

# global variables
num_of_agents = 30
num_of_iterations  = 100
neighbourhood = 20

environment = []
agents = []

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

# read image data into envitonment list
with open('in.txt', mode='r') as csv_file:
    file_reader = csv.reader(csv_file, delimiter=",")
    line_count = 0
    for row in file_reader: 
        rowList = []       
        for values in row:
            rowList.append(float(values))
        environment.append(rowList)
        line_count += 1

##    # this is just to show how many lines are in the file
##    print 'Processed {} lines from txt file.'.format(line_count)

# Make agents.
for i in range(num_of_agents):
    
    try:
        y = int(td_ys[i].text)
    except:
        y = None
    try:
        x = int(td_xs[i].text)
    except:
        x = None

    agents.append(agentframework.Agent(environment, agents, y, x))
    
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

# stopping condition
def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < 10) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1

def run():
    # animate
    #animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=num_of_iterations)
    animation = matplotlib.animation.FuncAnimation(fig, update, interval=1)
    canvas.draw()


root = tkinter.Tk()
root.wm_title("ABM Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

menu_bar = tkinter.Menu(root)   
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="File", menu=model_menu)
model_menu.add_command(label="Execute", command=run)


tkinter.mainloop() # Wait for interactions.
