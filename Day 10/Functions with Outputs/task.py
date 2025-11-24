# def format_name(f_name, l_name):
#     """ It takes first and last name and
#     formats them into two separate strings """
#     f_name = f_name.title()
#     l_name = l_name.title()
#     return f"{f_name} {l_name}"
#
#
# format_name()


def outer_function(a, b):
    def inner_function(c, d):
        return c + d

    return inner_function(a, b)


result = outer_function(5, 10)
print(result)