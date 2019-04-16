"""Simple unit tests for some
internal functionality of the
spelling completion server.
"""

import unittest
import flask_server

class TestSearch(unittest.TestCase):

    def setUp(self):
        flask_server.load_wordlist()

    def test_one_search(self):
        completions = flask_server.get_completions("wat", 5)
        self.assertEqual(completions, ['watch', 'watchband', 'watchdog', 'watcher', 'watchful', 'watchfully'])

    def test_at_beginning(self):
        completions = flask_server.get_completions("a", 5)
        self.assertEqual(completions, ['a', 'aardvark', 'abaci', 'aback', 'abacus', 'abaft'])

    def test_only_matches(self):
        """Only 4 matches for zy in our dictionary"""
        completions = flask_server.get_completions("zy", 5)
        self.assertEqual(completions, ['zydeco', 'zygote', 'zygotic', 'zymurgy'])


if __name__ == "__main__":
    unittest.main()