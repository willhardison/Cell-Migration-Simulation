# Cell-Migration-Simulation

This repository contains the code and data for the simulation and analysis of cell migration models in varying chemoattractant gradients. The goal of this project is to compare the performance of two cell migration models, namely the Compass model and the Split model, in different gradient conditions. The code is implemented in Python and the simulation results are visualized using Pygame.

## Introduction
This paper presents a computational model to investigate the behavior of cells during chemotaxis, specifically focusing on two models: the Compass model and the Split model. The Compass model suggests that cells form pseudopodia directly toward the direction of a stimulus, while the Split model proposes that cells form pseudopodia from various locations and tend to move in the direction of the gradient while being biased by the previous direction. The study aims to understand the superiority of one model over the other in varying levels of gradient imperfections.

## Simulation
The simulation involves generating grids with different levels of variance in the chemoattractant gradient. The grids represent the environment in which the cells migrate. The simulation considers two types of cells: Compass Cells and Split Cells. The Compass Cells move directly towards the square with the highest chemoattractant concentration, while the Split Cells consider the previous direction and tend to bias their movement accordingly. The simulation takes into account random chance in cell movement to introduce variability and mimic real cell behavior.

## Methods
The simulation is implemented using three Python scripts: grid.py, manager.py, and cell.py. The grid.py script generates a gradient matrix representing the chemoattractant distribution. The manager.py script handles the simulation process and visualization using Pygame. The cell.py script contains the classes for Compass Cells and Split Cells, including functions for movement and interaction with the grid.

## File Descriptions

- `grid.py`: Generates a gradient matrix representing the chemoattractant distribution in the environment.
- `manager.py`: Handles the simulation process and visualization using Pygame.
- `cell.py`: Defines the classes for Compass Cells and Split Cells, including functions for movement and interaction with the grid.
- `analysis.py`: Performs data analysis on the simulation results to measure the efficiency of each cell migration model.

## Running the Simulation
To run the simulation, follow these steps:

1. Install Python (version 3.7 or higher) on your machine.
2. Clone this repository to your local machine or download the code as a ZIP file.
3. Open a terminal or command prompt and navigate to the directory containing the downloaded code.
4. Install the required dependencies by running the following command:

`pip install -r requirements.txt`

5. Run the simulation by executing the following command:

```python manager.py```

The simulation will start, and you will be able to observe the movement of cells in the graphical window.

## Results and Analysis
The simulation generates data on cell movement and completion time in different gradient conditions. The analysis.py script can be used to analyze the simulation results and calculate metrics such as average completion time and efficiency for each cell type. The script also provides functionality to compare different directional weights for the Split Cells.

## Conclusion
This simulation-based study compares the Compass model and the Split model for cell migration in varying chemoattractant gradients. The results support the hypothesis that Split Cells perform better than Compass Cells in gradients with high variance. However, it is important to note that this model simplifies complex processes and further research is needed to fully understand the mechanisms of pseudopod formation and chemotaxis. The code and data provided in this repository can serve as a basis for future studies and exploration of other hypotheses in the field of cell migration.

## References
- `Andrew + Insall 2007`
- `Neilson et al`
- `Manifacier et al 2020`
