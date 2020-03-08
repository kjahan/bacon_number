import pandas as pd
import numpy as np


def process(base_folder, movies_metadata_fn, credits_fn):
    # Process movies_metadata data structure/schema
    metadata = pd.read_csv(base_folder + movies_metadata_fn)
    # Cast id to int64 and drop any NAN values!
    metadata.id = pd.to_numeric(metadata.id, downcast='signed', errors='coerce')
    metadata = metadata[metadata['id'].notna()]
    # cast id to int64 for later join
    metadata['id'] = metadata['id'].astype(np.int64)
    # Process credits data structure/schema
    credits = pd.read_csv(base_folder + credits_fn)
    # Cast id to int
    credits.id = pd.to_numeric(credits.id, downcast='signed', errors='coerce')
    # cast id to int64 for later join
    credits['id'] = credits['id'].astype(np.int64)
    # let's grab movies ids from both datasets (movies metadata and credits) and union them
    credits_id_set = set(credits['id'].tolist())
    metadata_id_set = set(metadata['id'].tolist())
    union = credits_id_set.union(metadata_id_set)
    # since movie/actors ids might overlap let's map movie ids to
    # a new space using random to reduce the collision chance!
    mapped_ids = {x : x + np.random.randint(1, 1e10) for x in union}
    # apply the mapping
    metadata['id'] = metadata['id'].apply(lambda x: mapped_ids[x])
    credits['id'] = credits['id'].apply(lambda x: mapped_ids[x])
    # test again for collision detetcion
    credits_id_set = set(credits['id'].tolist())
    metadata_id_set = set(metadata['id'].tolist())
    # Let's test Salmna Khan (actor id=42802) and raise excetion if that id is in movies data
    salman_khan_id = 42802
    salman_khan_id_exists = (salman_khan_id in credits_id_set) or (salman_khan_id in metadata_id_set)
    new_movie_id = mapped_ids[salman_khan_id]
    salman_khan_mapped_id_exists = (new_movie_id in credits_id_set) or (new_movie_id in metadata_id_set)
    if salman_khan_id_exists or not salman_khan_mapped_id_exists:
        print("Mapping movie ids failed - collision for Salman Khan actor id with a movie id!")
        raise RuntimeError
    # Let's join the two dataset based on movie id
    merged = pd.merge(metadata, credits, on='id')
    return merged
