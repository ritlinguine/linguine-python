import unittest

from pymongo import MongoClient

from linguine.transaction import Transaction


@unittest.skip("Transaction tests currently do nothing")
class TransactionTest(unittest.TestCase):

    def setUp(self):
        self.trans = Transaction()
        self.test_data = {}

    def test_parse_json(self):
        # set up test data
        db = 'linguine-test'
        corpora = MongoClient()[db].corpus
        test_contents_id = corpora.insert({"title": "A Tale of Two Cities",
                                           "contents": "it was the best of times it was the worst of times it was the age of whatever it was the age of whatever",
                                           "tags": []})
        self.test_data = '{"transaction_id":"1", "operation":"NoOp", "library":"no_library", "corpora_ids":["' + str(
            test_contents_id) + '"]}'

        # clean up
        corpora.remove(test_contents_id)

    def test_run(self):
        # set up test data
        db = 'linguine-test'
        corpora = MongoClient()[db].corpus
        test_contents_id = corpora.insert({"title": "A Tale of Two Cities",
                                           "contents": "it was the best of times it was the worst of times it was the age of whatever it was the age of whatever",
                                           "tags": []})
        self.test_data = '{"transaction_id":"1", "operation":"NoOp", "library":"no_library", "corpora_ids":["' + str(
            test_contents_id) + '"]}'

        # execute code

        # clean up
        corpora.remove(test_contents_id)


if __name__ == '__main__':
    unittest.main()
