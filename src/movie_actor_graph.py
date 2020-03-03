import re
import json
from collections import deque

class MovieActorGraph:
    def __init__(self):
        # a map from movie id to a list of actor id's
        self.movie_actor_adj_list = {}
        # a map from actor id to a list of movie id's
        self.actor_movie_adj_list = {}
        # a map from movies id to their title
        self.movies_map = {}
        # a map from movies titles to their ids
        self.inv_movies_map = {}
        # a map from actors id to their name
        self.actors_map = {}
        # a map from actors names to their ids
        self.inv_actors_map = {}

    def cleanup_json(self, dirty_json):
        b = re.sub("{'", '{"', dirty_json)
        c = re.sub("':", '":', b)
        d = re.sub(", '", ', "', c)
        e = re.sub(": '", ': "', d)
        f = re.sub("', ", '", ', e)
        h = re.sub("'", '', f)
        i = re.sub('}', '"}', h)
        j = re.sub(r': ([a-zA-Z\s]+), ', r': "\1", ', i)
        k = re.sub(r' None"', r' null', j)
        return k

    def construc_inverse_maps(self):
        self.inv_actors_map = {v: k for k, v in self.actors_map.items()}
        self.inv_movies_map = {v: k for k, v in self.movies_map.items()}

    def construct_graph(self, raw_data):
        cnt, errors = 0, 0
        failed_movies = {}
        for index, row in raw_data.iterrows():
            cnt += 1
            movie_id, movie_title = row['id'], row['title']
            if movie_id not in self.movies_map:
                self.movies_map[movie_id] = movie_title
            dirty_json = row['cast']
            try:
                dirty_json = self.cleanup_json(dirty_json)
                cast_data = json.loads(dirty_json)
                for cast in cast_data:
                    actor_name = cast['name']
                    actor_id = cast['id']
                    if actor_id not in self.actors_map:
                        self.actors_map[actor_id] = actor_name
                    # build movie-actor adj list
                    if movie_id not in self.movie_actor_adj_list:
                        self.movie_actor_adj_list[movie_id] = [actor_id]
                    else:
                        self.movie_actor_adj_list[movie_id].append(actor_id)
                    # build actor-movie adj list
                    if actor_id not in self.actor_movie_adj_list:
                        self.actor_movie_adj_list[actor_id] = [movie_id]
                    else:
                        self.actor_movie_adj_list[actor_id].append(movie_id)
            except json.JSONDecodeError as err:
                print("JSONDecodeError: {}, Movie id: {}, title: {}".format(err, movie_id, movie_title))
                failed_movies[movie_id] = True
                errors += 1
        print("Parsed credist: {}, errors: {}".format(cnt, errors))
        self.construc_inverse_maps()

    def bfs(self, source_id):
        _debug_ = False
        q = deque()
        q.append(source_id)
        six_separation_degrees = {source_id: 0}
        visited = {}
        degree = 1
        while q:
            u = q.popleft()
            if _debug_:
                print("u: {}".format(u))
            if u not in visited:
                visited[u] = True
                if _debug_:
                    print("degree(u): {}".format(six_separation_degrees[u]))
                if six_separation_degrees[u] % 2 == 0:
                    # u is an actor type node
                    neighbors = self.actor_movie_adj_list[u]
                    if _debug_:
                        print("actor type, neighbors: {}".format(neighbors))
                else:
                    # u is a movie type node
                    neighbors = self.movie_actor_adj_list[u]
                    if _debug_:
                        print("movie type, neighbors: {}".format(neighbors))
                for v in neighbors:
                    if v not in visited:
                        q.append(v)
                        if v not in six_separation_degrees:
                            six_separation_degrees[v] = six_separation_degrees[u] + 1
        return six_separation_degrees
