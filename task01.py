def add_setting(dict_settings, tuple_val):
    k, v = tuple_val
    k = k.lower()
    v = v.lower()
    if k in dict_settings.keys():
        return f"Setting '{k}' already exists! Cannot add a new setting with this name."
    else:
        dict_settings[k] = v
        return f"Setting '{k}' added with value '{v}' successfully!"


def update_setting(dict_settings, tuple_val):
    k, v = tuple_val
    k = k.lower()
    v = v.lower()
    if k in dict_settings.keys():
        dict_settings[k] = v
        return f"Setting '{k}' updated to '{v}' successfully!"
    else:
        return f"Setting '{k}' does not exist! Cannot update a non-existing setting."


def delete_setting(dict_settings, dict_key):
    k = dict_key.lower()
    if k in dict_settings.keys():
        del dict_settings[k]
        return f"Setting '{k}' deleted successfully!"
    else:
        return "Setting not found!"


def view_settings(dict_settings):
    if dict_settings:
        txt = "Current User Settings:\n"
        for k, v in dict_settings.items():
            txt += f"{k.title()}: {v}\n"
        return txt
    else:
        return "No settings available."


test_settings = {"theme": "dark", "notifications": "enabled", "volume": "high"}
print(add_setting({"theme": "light"}, ("THEME", "dark")))
print(update_setting({"theme": "light"}, ("theme", "dark")))
print(delete_setting({"theme": "light"}, "theme"))
print(view_settings(test_settings))
