import json

def load_json(path):
    """
    Load a JSON file given a path.
    
    Parameters
    ----------
    path
        The path to the JSON file.
        
    Returns
    -------
    data
        The content of the JSON file.
    """
    
    with open(path) as json_file:
        data = json.load(json_file)
    return data