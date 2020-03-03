# six-degrees
Six degrees of seperation

# Create the environment: 

`conda env create -f environment.yml`

# To activate this environment: 

`$ conda activate bacon`

# To deactivate an active environment: 

`$ conda deactivate`

# MacOS Python issue: 

If you encouter `AttributeError: module 'enum' has no attribute 'IntFlag'` on MacOS, simply run `unset PYTHONPATH` command in your terminal.

# Run the movies data pipeline:

To extract movies data, constructing the graph, running BFS, computing bacon number, and saving the outcome run: `python -m src.run`

# Start web server: 

Start the web server for running the api to get bacon number: `python -m src.server`

# Test api server for "Ronald Reagan":

Open your browser and test bacon number for "Ronald Reagan". You shold get bacon number of two.

http://127.0.0.1:5001/api/v1/baconnumber?actorname=Ronald%20Reagan

# Test api server for "Kevin Bacon":

For "Kevin Bacon" you shold get the bacon number of zero.

http://127.0.0.1:5001/api/v1/baconnumber?actorname=Kevin%20Bacon