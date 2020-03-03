# six-degrees
Six degrees of seperation

## Requirements

# Clone the code:

`git clone https://github.com/kjahan/six-degrees.git`

# Kaggle dataset:

You need to download the Kaggle dataset and store it under the repo folder, unzip it and rename the folder to `movies-dataset`.

# Create Conda environment: 

`conda env create -f environment.yml`

# To activate Conda environment: 

`$ conda activate bacon`

# To deactivate Conda environment: 

`$ conda deactivate`

# MacOS Python issue: 

If you encouter `AttributeError: module 'enum' has no attribute 'IntFlag'` on MacOS, simply run `unset PYTHONPATH` command in your terminal.

# Running movies data pipeline, unit tests, and start HTTP server:

To run the movies data pipeline you need to switch to where you cloned the repo code. To load and parse movies data, constructing the movie-actor bipartite graph, running BFS to compute bacon numbers, and saving the outcome results to disk: `python -m src.run`.

You need to run the above step before triggering api calls to the server!

To run unit tets run `pytest` from the repo root folder.

# Start HTTP server on your local machine: 

Start the HTTP server for handling the api calls and returning the bacon number: `python -m src.server`

# Test HTTP server for "Ronald Reagan" and "Kevin Bacon":

Open the browser of your choice on your local machine and try the following URL. You shold get bacon number of two.

http://127.0.0.1:5001/api/v1/baconnumber?actorname=Ronald%20Reagan


For "Kevin Bacon" you shold get the bacon number of zero.

http://127.0.0.1:5001/api/v1/baconnumber?actorname=Kevin%20Bacon