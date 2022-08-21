![Bacon Number](https://images.squarespace-cdn.com/content/v1/5a8d040564b05f9d780ecc2f/1554157278547-CG0BXDCS4ELRM4PWIQVA/image-asset.png)

# Six degrees of Kevin Bacon 
[Six Degrees of Kevin Bacon](https://en.wikipedia.org/wiki/Six_Degrees_of_Kevin_Bacon)

# Requirements

## Clone project

`git clone https://github.com/kjahan/six-degrees.git`

## Download dataset

You should download [The Movies Dataset](https://www.kaggle.com/rounakbanik/the-movies-dataset) and store it locally under the repo folder. Unzip the dataset file and rename its folder to `movies-dataset`.

## Conda environment setup

To create, activate and deactivate Conda environment:

`conda env create -f environment.yml`


`$ conda activate bacon`


`$ conda deactivate`

## MacOS Python issue

If you encouter `AttributeError: module 'enum' has no attribute 'IntFlag'` on MacOS, simply run `unset PYTHONPATH` command in your terminal.

## Running project

To run the movies data pipeline you need to switch to where you cloned the repo code. To load and parse movies data, constructing the movie-actor bipartite graph, running BFS to compute bacon numbers, and saving the outcome results to disk: `python -m src.run`.

You need to run the above step before triggering api calls to the server!

To run unit tets run `pytest` from the repo root folder.

## Starting HTTP server

Start the HTTP server for handling the api calls and returning the bacon number: `python -m src.server`

## Testing 

To test the HTTP server for "Ronald Reagan" and "Kevin Bacon", open the browser of your choice on your machine and try the following URLs. You shold get bacon number of two for "Ronald Reagan" and zero for "Kevin Bacon".

[Ronald's Bacon Number](http://127.0.0.1:5001/api/v1/baconnumber?actorname=Ronald%20Reagan)


[Kevin's Bacon Number](http://127.0.0.1:5001/api/v1/baconnumber?actorname=Kevin%20Bacon)
