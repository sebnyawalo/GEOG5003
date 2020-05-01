# GEOG5003
This is an Agent Based Model (ABM) which is designed to create agents and make them move based on parameters fed into the resulting model.
The agent properties and behaviour are influenced by the following parameters:

1)	num_of_agents # defines the number of agents in the model
2)	num_of_iterations # defines the number of iterations by agents
3)	neighbourhood # defines the maximum distance within which an agent can interact with another

The model takes in data from a web-page containing x, y and z values to create the agents for this model. Additionally, the model also reads data from an external file containing a 2D list simulating an enviroment. This enviroment represents 2D space where the agents can interact with other agents and other elements in that space. In this model, agents can move freely, "eat", modify and share their resources with other agents provided that they are within the neighborhood.

The model, when successfully executed, results into a Graphical User Interface showing the agents interaction based on a certain number of agents and iterations.

Project Structure:

Agent Framework.py  - this is agent class which defines the agents behaviours through move, eat and share data methods.

Model.py - defines the model  and  its functions for executing different components of the model

.gitattributes - gives attributes to pathnames in the model

Capture.PNG - A sample screenshot of the resulting agents interaction output

To run the model, execute model.py from console. Once the file has loaded, enter the values of the number of agents, the number of iterations and the number of Neighbour’s.

Once the model had been execute, it will display a GUI, from the file menu click run model
This will display an animated canvas as shown below.




![Capture](https://user-images.githubusercontent.com/63342826/80732195-a6aa3200-8b14-11ea-9370-f1c8dfbc9bf6.PNG)
