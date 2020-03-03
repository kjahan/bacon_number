import yaml
import pickle
import re

def setup():
    """
    Setup configuration
    """
    config_file_path = "config/config.yml"
    return yaml.load(open(config_file_path), Loader=yaml.FullLoader)

def save_model(six_separation_degrees, filename, model_folder):
    print("saving {} outcome...".format(filename))
    model_fn = model_folder + filename
    with open(model_fn, 'wb') as fp:
        pickle.dump(six_separation_degrees, fp)

def load_model(filename, model_folder):
    print("loading {} outcome...".format(filename))
    model_fn = model_folder + filename
    with open(model_fn, 'rb') as fp:
        six_separation_degrees = pickle.load(fp)
    return six_separation_degrees

def cleanup_json(dirty_json):
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