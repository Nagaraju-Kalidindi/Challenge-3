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
        }
    }
}

key_to_find = "a/b/c"
value_returned = get_value_from_path(nested_dict, key_to_find)

if value_returned:
    print(f"Key '{key_to_find}' found in nested dict, value:{value_returned}")
else:
    print(f"Key '{key_to_find}' not found in nested dict!!!")
