import yaml
import pickle

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
