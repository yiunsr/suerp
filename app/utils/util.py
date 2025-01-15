import copy

def merge_selective_dict(dict0, dict1, key_prefix, keys):
    dict_clone = copy.deepcopy(dict0)
    for key in keys:
        dict_clone[key] = dict1.get(key_prefix + key)
    return dict_clone
