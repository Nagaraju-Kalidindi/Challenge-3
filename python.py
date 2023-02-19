
def get_value_from_nested_dict(nes_dict, key_to_search):
    if key_to_search in nes_dict:
        return nes_dict[key_to_search]
    for key, value in nes_dict.items():
        if isinstance(value, dict):
            returned_value = get_value_from_nested_dict(value, key_to_search)
            if returned_value is not None:
                return returned_value
    return None


def get_value_from_path(nes_dict, key_to_search):
    key_list = key_to_search.split("/")
    value = nes_dict
    for key in key_list:
        value = value.get(key, {})
    if value:
        return value
    else:
        return None


nested_dict = {
    'abc': "111",
    'a': {
        'b': {
            'c': 'd',
            'e': 'f'
        },
        'adf': {
            'aaaa': "2222"
        },
        "aaaa": "4444"
    }
}

key_to_find = "a/b/z"
value_returned = get_value_from_path(nested_dict, key_to_find)

if value_returned:
    print(f"Key '{key_to_find}' found in nested dict, value:{value_returned}")
else:
    print(f"Key '{key_to_find}' not found in nested dict!!!")
