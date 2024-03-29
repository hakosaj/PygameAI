# Intelligent agents for basic games


Just a fun run, creating some basic (retro) games and intelligent agents to play them. Will be creating all of the AI-side from scratch.

Pygame is used in creating the game environment. Tensorflow, PyTorch and SKLearn not allowed!

CHECK OUT THE WIKI PAGE FOR MORE DETAILED INFORMATION! 

https://github.com/hakosaj/PygameAI/wiki


Going to do these games... (tentative):
  - Flappy bird
  - Minesweeper
  - Breakout
  - Snake
  - Tetris
  - Pac-Man
  - Space Invaders

...using these kinds of agents (tentative):
  - Genetic algorithm
  - ANN with backpropagation
  - Q-learning
  - NEAT
  - CNN with only using the screen as input

![Overview of the simulation](https://github.com/hakosaj/PygameAI/blob/master/flappy/gena.JPG) Flappy bird and genetic algorithms
## Getting Started

Clone this and install requirements from requirements.txt.

Then navigate to folder and voilá!



## Using the software

### Flappy

For Flappy bird, the command is

`python main.py [algorithm] [loadfile]`

The `algorithm` options are
  - empty for normal flappy bird
  - `GA` for genetic algorithm
  - `Q` for Q-learning

To load a Q-learning Q-matrix training snapshot, use the "loadfile"-argument to specify the snapshot.

Simpler way is to use the specified files separately:
- `gaflappy.py` for GA
- `manual.py` for normal
- `qflappy.py` for Q learning


### Tetris

The Tetris operates with a 4-parameter vector that govern the agent's behaviour. The program itself can be ran in several different ways. There are two modes for this, visual or nonvisual mode. The nonvisual mode is used for parallerising the genetic algorithm when finding parameters.

Whenever the heuristic agent is playing the game, constant `multi` from `constants.py` dictates whether or not the actual heuristic parallelises the finding of a following move. The default version is doing it. 


The current weightings are able to do at least some hours of continuous gameplay. Hard to tell if a perfect agent will ever be possible?


For Tetris, the command is either

`python tetris.py [control]`

The `[control]` options are
  - `manual` for a normal Tetris game
  - `auto` for playing the game with the heuristic agent with predetermined parameters


To run the parameter-finding GA, use

`python GA.py`

To utilise a faster, nonvisual parallel implementation of the parameter finding algorithm, change

`visual` from `constants.py` to `False`,

and use the command

`python MCGA.py`


The aforementioned uses increasing block amounts and decreasing population sizes.


!!WARNING!!

This takes a LOT of time, there's still work to be done regarding the performance.

!!WARNING!!


My Tetris algorithm is modelled after [Yiyuan Lee](https://codemyroad.wordpress.com/2013/04/14/tetris-ai-the-near-perfect-player/)


### Snake

For basic snake with manual controls, use the command

`python snake.py`

A basic BFS-based AI-agent implemented already. It can be run on visual or nonvisual mode.

To run the agent, use

`python autosnake.py`

The walls are hard in this game. If you want walls that can be went through, change parameter

`walls` from `constants.py` to `False`.




## Status and steps: currently phase I is ready, phase II coming later!

### General
  - Real documentation. File contents, functions, a few words on the algorithms etc.
  - Statistical tests for results

### Flappy
  
  **After phase 1:**
  - Implement the Deep-Q CNN http://cs231n.stanford.edu/reports/2016/pdfs/111_Report.
  - File selection based on argument
  - Update Q-learning reward scheme so it converges better
  - Some sorta ANN (perceptron with 4 inputs and 2 outputs?)
 
### Breakout

  **After phase 1:**
  - Fix the issues with ball+block collisions
  - Implement Deep-Q CNN á lá DeepMind

### Snake

  **After phase 1:**
  - Shortcuts in Hamiltonian AI
  - Deep Neural Net-AI
  
### Tetris

  **After phase 1:**
  - Statistical tests for the parameters and their evolution
  - This one does not do cliffhangers
  - No direct interfacing, get all data from the screen as a player would?
  - Parameter convergence plots


Minesweeper, Pac-Man, Space Invaders and Breakout in phase 2


## Authors

* **Jussi Hakosalo [hakosaj](https://github.com/hakosaj)** - *All of it* 



## License

This project is licensed under the MIT License 
