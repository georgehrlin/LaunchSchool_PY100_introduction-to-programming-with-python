return ("This is a long string. "
        "It's actually very long. "
        "It spans multiple lines. "
        "Are you getting tired of this? "
        "So am I.")

# f-strings? r-strings?

return """
    This is a long string.
    It's actually very long.
    It spans multiple lines.
    Are you getting tired of this?
    So am I.
"""

# Multi-value literals use line-breaks
# List continuation
my_list = [
    "Antonina",
    "Brandi",
    "Trevor",
]

# Tuple continuation
my_tuple = (
    3.141592,
    2.718282,
    1.414213
)

# Set continuation
my_set = {
    "Dog",
    "Cat",
    "Pet",
}

# "When writing collection literals over multiple lines... the convention is to
# end every item in the list with a comma, including the last element."