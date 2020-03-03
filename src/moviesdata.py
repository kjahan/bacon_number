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
    # Let's join the two dataset based on movie id
    merged = pd.merge(metadata, credits, on='id')
    return merged 