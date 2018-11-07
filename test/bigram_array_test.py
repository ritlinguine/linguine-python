import json
import unittest

from linguine.corpus import Corpus
from linguine.ops.bigram_array import BigramArray


class BigramArrayTest(unittest.TestCase):

    def setUp(self):
        self.op = BigramArray()

    def test_run(self):
        self.test_data = [Corpus("0", "Test", "The quick brown fox jumped over the lazy dog.\n")]
        results = self.op.run(self.test_data)
        desired_results = [
            {"chars": ["_", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
                       "p", "q", "r", "t", "u", "v", "w", "x", "y", "z"],
             "array": {
                 "p": {"p": 0, "b": 0, "d": 0, "j": 0, "r": 0, "x": 0, "f": 0, "t": 0, "q": 0, "e": 1, "g": 0, "a": 0,
                       "o": 0, "u": 0, "w": 0, "h": 0, "k": 0, "y": 0, "v": 0, "z": 0, "i": 0, "c": 0, "m": 0, "_": 0,
                       "l": 0, "n": 0},
                 "b": {"p": 0, "b": 0, "d": 0, "j": 0, "r": 1, "x": 0, "f": 0, "t": 0, "q": 0, "e": 0, "g": 0, "a": 0,
                       "o": 0, "u": 0, "w": 0, "h": 0, "k": 0, "y": 0, "v": 0, "z": 0, "i": 0, "c": 0, "m": 0, "_": 0,
                       "l": 0, "n": 0},
                 "d": {"p": 0, "b": 0, "d": 0, "j": 0, "r": 0, "x": 0, "f": 0, "t": 0, "q": 0, "e": 0, "g": 0, "a": 0,
                       "o": 1, "u": 0, "w": 0, "h": 0, "k": 0, "y": 0, "v": 0, "z": 0, "i": 0, "c": 0, "m": 0, "_": 1,
                       "l": 0, "n": 0},
                 "j": {"p": 0, "b": 0, "d": 0, "j": 0, "r": 0, "x": 0, "f": 0, "t": 0, "q": 0, "e": 0, "g": 0, "a": 0,
                       "o": 0, "u": 1, "w": 0, "h": 0, "k": 0, "y": 0, "v": 0, "z": 0, "i": 0, "c": 0, "m": 0, "_": 0,
                       "l": 0, "n": 0},
                 "r": {"p": 0, "b": 0, "d": 0, "j": 0, "r": 0, "x": 0, "f": 0, "t": 0, "q": 0, "e": 0, "g": 0, "a": 0,
                       "o": 1, "u": 0, "w": 0, "h": 0, "k": 0, "y": 0, "v": 0, "z": 0, "i": 0, "c": 0, "m": 0, "_": 1,
                       "l": 0, "n": 0},
                 "x": {"p": 0, "b": 0, "d": 0, "j": 0, "r": 0, "x": 0, "f": 0, "t": 0, "q": 0, "e": 0, "g": 0, "a": 0,
                       "o": 0, "u": 0, "w": 0, "h": 0, "k": 0, "y": 0, "v": 0, "z": 0, "i": 0, "c": 0, "m": 0, "_": 1,
                       "l": 0, "n": 0},
                 "f": {"p": 0, "b": 0, "d": 0, "j": 0, "r": 0, "x": 0, "f": 0, "t": 0, "q": 0, "e": 0, "g": 0, "a": 0,
                       "o": 1, "u": 0, "w": 0, "h": 0, "k": 0, "y": 0, "v": 0, "z": 0, "i": 0, "c": 0, "m": 0, "_": 0,
                       "l": 0, "n": 0},
                 "t": {"p": 0, "b": 0, "d": 0, "j": 0, "r": 0, "x": 0, "f": 0, "t": 0, "q": 0, "e": 0, "g": 0, "a": 0,
                       "o": 0, "u": 0, "w": 0, "h": 2, "k": 0, "y": 0, "v": 0, "z": 0, "i": 0, "c": 0, "m": 0, "_": 0,
                       "l": 0, "n": 0},
                 "q": {"p": 0, "b": 0, "d": 0, "j": 0, "r": 0, "x": 0, "f": 0, "t": 0, "q": 0, "e": 0, "g": 0, "a": 0,
                       "o": 0, "u": 1, "w": 0, "h": 0, "k": 0, "y": 0, "v": 0, "z": 0, "i": 0, "c": 0, "m": 0, "_": 0,
                       "l": 0, "n": 0},
                 "e": {"p": 0, "b": 0, "d": 1, "j": 0, "r": 1, "x": 0, "f": 0, "t": 0, "q": 0, "e": 0, "g": 0, "a": 0,
                       "o": 0, "u": 0, "w": 0, "h": 0, "k": 0, "y": 0, "v": 0, "z": 0, "i": 0, "c": 0, "m": 0, "_": 2,
                       "l": 0, "n": 0},
                 "g": {"p": 0, "b": 0, "d": 0, "j": 0, "r": 0, "x": 0, "f": 0, "t": 0, "q": 0, "e": 0, "g": 0, "a": 0,
                       "o": 0, "u": 0, "w": 0, "h": 0, "k": 0, "y": 0, "v": 0, "z": 0, "i": 0, "c": 0, "m": 0, "_": 0,
                       "l": 0, "n": 0},
                 "a": {"p": 0, "b": 0, "d": 0, "j": 0, "r": 0, "x": 0, "f": 0, "t": 0, "q": 0, "e": 0, "g": 0, "a": 0,
                       "o": 0, "u": 0, "w": 0, "h": 0, "k": 0, "y": 0, "v": 0, "z": 1, "i": 0, "c": 0, "m": 0, "_": 0,
                       "l": 0, "n": 0},
                 "o": {"p": 0, "b": 0, "d": 0, "j": 0, "r": 0, "x": 1, "f": 0, "t": 0, "q": 0, "e": 0, "g": 1, "a": 0,
                       "o": 0, "u": 0, "w": 1, "h": 0, "k": 0, "y": 0, "v": 1, "z": 0, "i": 0, "c": 0, "m": 0, "_": 0,
                       "l": 0, "n": 0},
                 "u": {"p": 0, "b": 0, "d": 0, "j": 0, "r": 0, "x": 0, "f": 0, "t": 0, "q": 0, "e": 0, "g": 0, "a": 0,
                       "o": 0, "u": 0, "w": 0, "h": 0, "k": 0, "y": 0, "v": 0, "z": 0, "i": 1, "c": 0, "m": 1, "_": 0,
                       "l": 0, "n": 0},
                 "w": {"p": 0, "b": 0, "d": 0, "j": 0, "r": 0, "x": 0, "f": 0, "t": 0, "q": 0, "e": 0, "g": 0, "a": 0,
                       "o": 0, "u": 0, "w": 0, "h": 0, "k": 0, "y": 0, "v": 0, "z": 0, "i": 0, "c": 0, "m": 0, "_": 0,
                       "l": 0, "n": 1},
                 "h": {"p": 0, "b": 0, "d": 0, "j": 0, "r": 0, "x": 0, "f": 0, "t": 0, "q": 0, "e": 2, "g": 0, "a": 0,
                       "o": 0, "u": 0, "w": 0, "h": 0, "k": 0, "y": 0, "v": 0, "z": 0, "i": 0, "c": 0, "m": 0, "_": 0,
                       "l": 0, "n": 0},
                 "k": {"p": 0, "b": 0, "d": 0, "j": 0, "r": 0, "x": 0, "f": 0, "t": 0, "q": 0, "e": 0, "g": 0, "a": 0,
                       "o": 0, "u": 0, "w": 0, "h": 0, "k": 0, "y": 0, "v": 0, "z": 0, "i": 0, "c": 0, "m": 0, "_": 1,
                       "l": 0, "n": 0},
                 "y": {"p": 0, "b": 0, "d": 0, "j": 0, "r": 0, "x": 0, "f": 0, "t": 0, "q": 0, "e": 0, "g": 0, "a": 0,
                       "o": 0, "u": 0, "w": 0, "h": 0, "k": 0, "y": 0, "v": 0, "z": 0, "i": 0, "c": 0, "m": 0, "_": 1,
                       "l": 0, "n": 0},
                 "v": {"p": 0, "b": 0, "d": 0, "j": 0, "r": 0, "x": 0, "f": 0, "t": 0, "q": 0, "e": 1, "g": 0, "a": 0,
                       "o": 0, "u": 0, "w": 0, "h": 0, "k": 0, "y": 0, "v": 0, "z": 0, "i": 0, "c": 0, "m": 0, "_": 0,
                       "l": 0, "n": 0},
                 "z": {"p": 0, "b": 0, "d": 0, "j": 0, "r": 0, "x": 0, "f": 0, "t": 0, "q": 0, "e": 0, "g": 0, "a": 0,
                       "o": 0, "u": 0, "w": 0, "h": 0, "k": 0, "y": 1, "v": 0, "z": 0, "i": 0, "c": 0, "m": 0, "_": 0,
                       "l": 0, "n": 0},
                 "i": {"p": 0, "b": 0, "d": 0, "j": 0, "r": 0, "x": 0, "f": 0, "t": 0, "q": 0, "e": 0, "g": 0, "a": 0,
                       "o": 0, "u": 0, "w": 0, "h": 0, "k": 0, "y": 0, "v": 0, "z": 0, "i": 0, "c": 1, "m": 0, "_": 0,
                       "l": 0, "n": 0},
                 "c": {"p": 0, "b": 0, "d": 0, "j": 0, "r": 0, "x": 0, "f": 0, "t": 0, "q": 0, "e": 0, "g": 0, "a": 0,
                       "o": 0, "u": 0, "w": 0, "h": 0, "k": 1, "y": 0, "v": 0, "z": 0, "i": 0, "c": 0, "m": 0, "_": 0,
                       "l": 0, "n": 0},
                 "m": {"p": 1, "b": 0, "d": 0, "j": 0, "r": 0, "x": 0, "f": 0, "t": 0, "q": 0, "e": 0, "g": 0, "a": 0,
                       "o": 0, "u": 0, "w": 0, "h": 0, "k": 0, "y": 0, "v": 0, "z": 0, "i": 0, "c": 0, "m": 0, "_": 0,
                       "l": 0, "n": 0},
                 "_": {"p": 0, "b": 1, "d": 1, "j": 1, "r": 0, "x": 0, "f": 1, "t": 1, "q": 1, "e": 0, "g": 0, "a": 0,
                       "o": 1, "u": 0, "w": 0, "h": 0, "k": 0, "y": 0, "v": 0, "z": 0, "i": 0, "c": 0, "m": 0, "_": 0,
                       "l": 1, "n": 0},
                 "l": {"p": 0, "b": 0, "d": 0, "j": 0, "r": 0, "x": 0, "f": 0, "t": 0, "q": 0, "e": 0, "g": 0, "a": 1,
                       "o": 0, "u": 0, "w": 0, "h": 0, "k": 0, "y": 0, "v": 0, "z": 0, "i": 0, "c": 0, "m": 0, "_": 0,
                       "l": 0, "n": 0},
                 "n": {"p": 0, "b": 0, "d": 0, "j": 0, "r": 0, "x": 0, "f": 0, "t": 0, "q": 0, "e": 0, "g": 0, "a": 0,
                       "o": 0, "u": 0, "w": 0, "h": 0, "k": 0, "y": 0, "v": 0, "z": 0, "i": 0, "c": 0, "m": 0, "_": 1,
                       "l": 0, "n": 0}}}]
        self.assertEqual(json.loads(results), desired_results)


if __name__ == '__main__':
    unittest.main()
