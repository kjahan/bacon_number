import sys
import os
import json

path = os.getcwd()

# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, path)

from src.movie_actor_graph import MovieActorGraph

def test_bfs():
    g = MovieActorGraph()
    # a map from actors id to their name
    g.actors_map = {0: 'Kevin Bacon', 1: 'Tom Hanks', 2: 'Ronald Reagan'}
    # a map from movies id to their title
    g.movies_map = {100: 'm1', 200: 'm2'}
    # Bipartite graph edges: kevin --> m1, tom hanks --> m1, tom hanks --> m2, ronald regan --> m2
    # a map from movie id to a list of actor id's
    g.movie_actor_adj_list = {100: [0, 1], 200: [1, 2]}
    # a map from actor id to a list of movie id's
    g.actor_movie_adj_list = {0: [100], 1: [100, 200], 2: [200]}
    # let's run BFS from Kevin Bacon node and calculate the degrees of seperation
    kevin_id = 0
    six_separation_degrees = g.bfs(kevin_id)
    # Kevin should have a bacon number of zero!
    kevin_query = 0
    kevin_bacon_num = six_separation_degrees[kevin_query]/2
    assert kevin_bacon_num == 0
    # Based on our mocked bipartite graph Tom Hanks should have a bacon number of one!
    tom_query = 1
    tom_bacon_num = six_separation_degrees[tom_query]/2
    assert tom_bacon_num == 1
    # Based on our mocked bipartite graph Ronal Reagan should have a bacon number of one!
    ronald_query = 2
    ronald_bacon_num = six_separation_degrees[ronald_query]/2
    assert ronald_bacon_num == 2
