from src.utilities import setup
from src.utilities import save_model
from src.moviesdata import process
from src.movie_actor_graph import MovieActorGraph

def run_pipeline(actor_name="Kevin Bacon"):
    print("processing movies data...")
    movies_data = process(config["data_folder"], config["movies_metadata_fn"], config["credits_fn"])
    # print(movies_data.head(3))
    print("constructing movies-actors bipartite graph...")
    g = MovieActorGraph()
    g.construct_graph(movies_data)
    # get actor id and run BFS from his node
    source_id = g.inv_actors_map[actor_name]
    # get siz degrees of separation model starting from Kevin
    print("running BFS...")
    six_separation_degrees = g.run_bfs(source_id)
    save_model(six_separation_degrees, "six_degrees.pkl", config["model_folder"])
    save_model(g.inv_actors_map, "inv_actors_map.pkl", config["model_folder"])

if __name__ == "__main__":
    global config
    config = setup()
    run_pipeline()
