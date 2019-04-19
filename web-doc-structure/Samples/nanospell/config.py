"""Configuration options for tiny Ajax server of
   spelling completions.
"""

PORT = 5000     # Serve on localhost:5000
DEBUG = True   

# WORDFILE should be a path to a list of words,
# one word per line, compressed with zip.   
WORDFILE = "static/data/dict.txt.zip"
