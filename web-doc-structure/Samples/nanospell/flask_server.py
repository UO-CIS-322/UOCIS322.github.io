"""
Tiny server provides spelling completion suggestions on port 5678.
Constructed using the flask web application framework for Python.
"""
import config

import flask
from flask import request
from flask import jsonify
import zipfile
import logging

from typing import List

###
# Globals
###
app = flask.Flask(__name__)
WORDLIST = []   # Loaded on first request

import uuid

app.secret_key = str(uuid.uuid4())
app.debug = config.DEBUG
app.logger.setLevel(logging.DEBUG)

##############
# The page on which we will get spelling
# suggestions.  To avoid some security complications,
# the page and the Ajax response come from the same
# server.
###############

@app.route("/")
def nanospell():
    return flask.render_template("nanospell.html")


###############
#
# AJAX request handlers
#   These return JSON, rather than rendering pages.
#
###############
@app.route("/_suggest_completions")
def suggest_completions():
    """
    Up to k suggestions for completing a word
    """
    app.logger.debug("Got a JSON request")
    prefix = request.args.get('prefix', "default", type=str)
    app.logger.debug(f"Prefix: '{prefix}")
    app.logger.debug(f"The request object: {request}")
    app.logger.debug(f"The arguments: '{request.args}")
    if prefix:
        app.logger.debug(f"Looking up '{prefix}' in {len(WORDLIST)} words")
        completions = get_completions(prefix, 5)
        app.logger.debug(f"Found completions {completions}")
    else:
        app.logger.debug("Didn't have a prefix to look up")
        completions = []
    return jsonify(suggestions=completions)


#############
# Used by request handlers
#############

def load_wordlist():
    """Load the WORDLIST from an external file"""
    global WORDLIST
    zipped = zipfile.ZipFile(config.WORDFILE)
    reader = zipped.open("dict.txt")
    words = [line.decode('utf8').strip() for line in reader]
    # Note we could have a benign race condition:  If the first
    # two requests come in very close to each other, we will read
    # word list twice (or more), and build unnecessary copies of the
    # list, but as assignment to the list is atomic we will still end
    # up with one valid copy of the list.
    WORDLIST = words


def get_completions(prefix: str, max_completions: 5) -> List[str]:
    global WORDLIST
    if not WORDLIST: 
        load_wordlist()
    # Standard binary search until we succeed or fail; then
    # whether we succeed or fail, the next few words could be
    # completions.
    low = 0
    high = len(WORDLIST) - 1
    while high >= low:
        probe = (high + low) // 2
        probe_word = WORDLIST[probe]
        if probe_word == prefix:
            return scan_completions(prefix, WORDLIST, probe, max_completions)
        if probe_word > prefix:
            high = probe - 1
        else:
            low = probe + 1
    # If we completed the search without finding a match,
    # then 'low' is the index of the first word that could potentially
    # be a match.
    #
    return scan_completions(prefix, WORDLIST, low, max_completions)


def scan_completions(prefix, words, start_scan, max_entries=5) -> List[str]:
    """Starting at words[start_scan], return up to max_entries strings
    that could be completions of prefix.
    """
    completions = []
    count = 0
    probe = start_scan
    while count <= max_entries and probe < len(words) and words[probe].startswith(prefix):
        completions.append(words[probe])
        probe += 1
        count += 1
    return completions


#############


if __name__ == "__main__":
    import uuid

    app.secret_key = str(uuid.uuid4())
    app.debug = config.DEBUG
    app.logger.setLevel(logging.DEBUG)
    app.run(port=config.PORT)


