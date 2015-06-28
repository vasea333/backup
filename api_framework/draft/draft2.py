


def form_standard_path(name, dir_nam = None):
    if dir_nam is None:
        return '%s/%s' % ("users/class", name)
    else:
        return '%s/%s/%s' % ("users/class", dir_nam, name)
print (form_standard_path("Alex"))
print(form_standard_path("Alex", "sub_class"))