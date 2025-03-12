# This file makes the directory a package
# In Python, a directory with an __init__.py file is considered a package.
# Packages allow for a hierarchical structuring of the module namespace using dot notation.
# For example, if you have a directory structure like this:
# 
# expense_tracker/
# ├── __init__.py
# ├── module1.py
# └── subpackage/
#     ├── __init__.py
#     └── module2.py
#
# You can import module1 with `import expense_tracker.module1`
# and module2 with `import expense_tracker.subpackage.module2`.
# 
# The __init__.py file can be empty, or it can contain initialization code for the package.
# It can also define the __all__ variable, which controls what is imported when a client imports the package using `from package import *`.
