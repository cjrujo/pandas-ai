"""
Constants used in the pandasai package.

It includes Start & End Code tags, Whitelisted Python Packages and
While List Builtin Methods.

"""
# Default directory to store chart if user doesn't provide any
DEFAULT_CHART_DIRECTORY = "exports/charts"

DEFAULT_FILE_PERMISSIONS = 0o755

# List of Python builtin libraries that are added to the environment by default.
WHITELISTED_BUILTINS = [
    "abs",
    "all",
    "any",
    "ascii",
    "bin",
    "bool",
    "bytearray",
    "bytes",
    "callable",
    "chr",
    "classmethod",
    "complex",
    "delattr",
    "dict",
    "dir",
    "divmod",
    "enumerate",
    "filter",
    "float",
    "format",
    "frozenset",
    "getattr",
    "hasattr",
    "hash",
    "help",
    "hex",
    "id",
    "int",
    "isinstance",
    "issubclass",
    "iter",
    "len",
    "list",
    "locals",
    "map",
    "max",
    "memoryview",
    "min",
    "next",
    "object",
    "oct",
    "ord",
    "pow",
    "print",
    "property",
    "range",
    "repr",
    "reversed",
    "round",
    "set",
    "setattr",
    "slice",
    "sorted",
    "staticmethod",
    "str",
    "sum",
    "super",
    "tuple",
    "type",
    "vars",
    "zip",
]

# List of Python packages that are whitelisted for import in generated code
WHITELISTED_LIBRARIES = [
    "sklearn",
    "statsmodels",
    "seaborn",
    "plotly",
    "ggplot",
    "matplotlib",
    "numpy",
    "datetime",
    "json",
    "io",
    "base64",
    "scipy",
    "streamlit",
]
