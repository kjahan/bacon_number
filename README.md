# six-degrees
Six degrees of seperation

# Create the environment: 

`conda env create -f environment.yml`

# To activate this environment: 

`$ conda activate bacon`

# To deactivate an active environment: 

`$ conda deactivate`

## If you encouter `AttributeError: module 'enum' has no attribute 'IntFlag'` on MacOS, simply run `unset PYTHONPATH` command in your terminal.

# Run the movies data pipeline for running BFS, computing bacon number and saving the outcome:

`python -m src.run`

# Run the web server which servers the api for returning bacon number: `python -m src.server`

# Open your browser to test the api end point as follows for "Ronal Ragan", we shold get bacon number of 2 :)

http://127.0.0.1:5001/api/v1/baconnumber?actorname=Ronald%20Reagan

## Try "Kevin Bacon" with the API endpoint and you shold get bacon number of 0 :)

http://127.0.0.1:5001/api/v1/baconnumber?actorname=Kevin%20Bacon