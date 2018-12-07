import unittest

from linguine.corpus import Corpus
from linguine.ops.StanfordCoreNLP import StanfordCoreNLP


class StanfordCoreNLPTest(unittest.TestCase):

    def setUp(self):
        self.op = StanfordCoreNLP([])
        self.test_data = [Corpus("0", "Test", "The quick brown fox jumped over the lazy dog.\n")]

    def test_run_pos(self):
        self.op.analysisType = ['pos']
        results = self.op.run(self.test_data)
        desired_results = {
            'sentences': [{
                'tokens': [{'pos': 'DT', 'token': 'The'}, {'pos': 'JJ', 'token': 'quick'},
                           {'pos': 'JJ', 'token': 'brown'}, {'pos': 'NN', 'token': 'fox'},
                           {'pos': 'VBD', 'token': 'jumped'}, {'pos': 'IN', 'token': 'over'},
                           {'pos': 'DT', 'token': 'the'}, {'pos': 'JJ', 'token': 'lazy'},
                           {'pos': 'NN', 'token': 'dog'}, {'pos': '.', 'token': '.'}],
                'deps_json': [{'id': 1, 'tag': 'S', 'head': 0, 'value': 'S'},
                              {'id': 2, 'tag': 'NP', 'head': 1, 'value': 'NP'},
                              {'id': 3, 'tag': 'VP', 'head': 1, 'value': 'VP'},
                              {'id': 4, 'tag': '.', 'head': 1, 'value': '.'},
                              {'id': 5, 'tag': 'DT', 'head': 2, 'value': 'DT'},
                              {'id': 6, 'tag': 'JJ', 'head': 2, 'value': 'JJ'},
                              {'id': 7, 'tag': 'JJ', 'head': 2, 'value': 'JJ'},
                              {'id': 8, 'tag': 'NN', 'head': 2, 'value': 'NN'},
                              {'id': 9, 'tag': '', 'head': 5, 'value': 'The'},
                              {'id': 10, 'tag': '', 'head': 6, 'value': 'quick'},
                              {'id': 11, 'tag': '', 'head': 7, 'value': 'brown'},
                              {'id': 12, 'tag': '', 'head': 8, 'value': 'fox'},
                              {'id': 13, 'tag': 'VBD', 'head': 3, 'value': 'VBD'},
                              {'id': 14, 'tag': 'PP', 'head': 3, 'value': 'PP'},
                              {'id': 15, 'tag': '', 'head': 13, 'value': 'jumped'},
                              {'id': 16, 'tag': 'IN', 'head': 14, 'value': 'IN'},
                              {'id': 17, 'tag': 'NP', 'head': 14, 'value': 'NP'},
                              {'id': 18, 'tag': '', 'head': 16, 'value': 'over'},
                              {'id': 19, 'tag': 'DT', 'head': 17, 'value': 'DT'},
                              {'id': 20, 'tag': 'JJ', 'head': 17, 'value': 'JJ'},
                              {'id': 21, 'tag': 'NN', 'head': 17, 'value': 'NN'},
                              {'id': 22, 'tag': '', 'head': 19, 'value': 'the'},
                              {'id': 23, 'tag': '', 'head': 20, 'value': 'lazy'},
                              {'id': 24, 'tag': '', 'head': 21, 'value': 'dog'},
                              {'id': 25, 'tag': '', 'head': 4, 'value': '.'}]}],
            'entities': [
                {'entityid': 1, 'mentions': [
                    {'mentiontype': 'NOMINAL', 'tokspan_in_sentence': [0, 4], 'sentence': 0, 'animacy': 'ANIMATE',
                     'number': 'SINGULAR', 'gender': 'MALE', 'representative': True, 'head': 3, 'mentionid': 1}]},
                {'entityid': 2, 'mentions': [
                    {'mentiontype': 'NOMINAL', 'tokspan_in_sentence': [6, 9], 'sentence': 0, 'animacy': 'ANIMATE',
                     'number': 'SINGULAR', 'gender': 'UNKNOWN', 'representative': True, 'head': 8, 'mentionid': 2}]}]}
        self.assertEqual(results, desired_results)

    def test_run_ner(self):
        self.op.analysisType = ['pos', 'ner']
        results = self.op.run(self.test_data)
        desired_results = {
            'sentences': [{
                'tokens': [{'token': 'The', 'ner': 'O', 'pos': 'DT'},
                           {'token': 'quick', 'ner': 'O', 'pos': 'JJ'},
                           {'token': 'brown', 'ner': 'O', 'pos': 'JJ'},
                           {'token': 'fox', 'ner': 'O', 'pos': 'NN'},
                           {'token': 'jumped', 'ner': 'O', 'pos': 'VBD'},
                           {'token': 'over', 'ner': 'O', 'pos': 'IN'},
                           {'token': 'the', 'ner': 'O', 'pos': 'DT'},
                           {'token': 'lazy', 'ner': 'O', 'pos': 'JJ'},
                           {'token': 'dog', 'ner': 'O', 'pos': 'NN'},
                           {'token': '.', 'ner': 'O', 'pos': '.'}],
                'deps_json': [{'tag': 'S', 'value': 'S', 'head': 0, 'id': 1},
                              {'tag': 'NP', 'value': 'NP', 'head': 1, 'id': 2},
                              {'tag': 'VP', 'value': 'VP', 'head': 1, 'id': 3},
                              {'tag': '.', 'value': '.', 'head': 1, 'id': 4},
                              {'tag': 'DT', 'value': 'DT', 'head': 2, 'id': 5},
                              {'tag': 'JJ', 'value': 'JJ', 'head': 2, 'id': 6},
                              {'tag': 'JJ', 'value': 'JJ', 'head': 2, 'id': 7},
                              {'tag': 'NN', 'value': 'NN', 'head': 2, 'id': 8},
                              {'tag': '', 'value': 'The', 'head': 5, 'id': 9},
                              {'tag': '', 'value': 'quick', 'head': 6, 'id': 10},
                              {'tag': '', 'value': 'brown', 'head': 7, 'id': 11},
                              {'tag': '', 'value': 'fox', 'head': 8, 'id': 12},
                              {'tag': 'VBD', 'value': 'VBD', 'head': 3, 'id': 13},
                              {'tag': 'PP', 'value': 'PP', 'head': 3, 'id': 14},
                              {'tag': '', 'value': 'jumped', 'head': 13, 'id': 15},
                              {'tag': 'IN', 'value': 'IN', 'head': 14, 'id': 16},
                              {'tag': 'NP', 'value': 'NP', 'head': 14, 'id': 17},
                              {'tag': '', 'value': 'over', 'head': 16, 'id': 18},
                              {'tag': 'DT', 'value': 'DT', 'head': 17, 'id': 19},
                              {'tag': 'JJ', 'value': 'JJ', 'head': 17, 'id': 20},
                              {'tag': 'NN', 'value': 'NN', 'head': 17, 'id': 21},
                              {'tag': '', 'value': 'the', 'head': 19, 'id': 22},
                              {'tag': '', 'value': 'lazy', 'head': 20, 'id': 23},
                              {'tag': '', 'value': 'dog', 'head': 21, 'id': 24},
                              {'tag': '', 'value': '.', 'head': 4, 'id': 25}]}],
            'entities': [
                {'entityid': 1, 'mentions': [
                    {'gender': 'MALE', 'representative': True, 'tokspan_in_sentence': [0, 4], 'head': 3, 'mentionid': 1,
                     'sentence': 0, 'mentiontype': 'NOMINAL', 'number': 'SINGULAR', 'animacy': 'ANIMATE'}]},
                {'entityid': 2, 'mentions': [
                    {'gender': 'UNKNOWN', 'representative': True, 'tokspan_in_sentence': [6, 9], 'head': 8,
                     'mentionid': 2,
                     'sentence': 0, 'mentiontype': 'NOMINAL', 'number': 'SINGULAR', 'animacy': 'ANIMATE'}]}]}
        self.assertEqual(results, desired_results)

    def test_run_sentiment(self):
        self.op.analysisType = ['parse', 'sentiment']
        results = self.op.run(self.test_data)
        desired_results = {
            'sentences': [{
                'sentiment': 'Negative',
                'deps_json': [{'value': 'S', 'head': 0, 'tag': 'S', 'id': 1},
                              {'value': 'NP', 'head': 1, 'tag': 'NP', 'id': 2},
                              {'value': 'VP', 'head': 1, 'tag': 'VP', 'id': 3},
                              {'value': '.', 'head': 1, 'tag': '.', 'id': 4},
                              {'value': 'DT', 'head': 2, 'tag': 'DT', 'id': 5},
                              {'value': 'JJ', 'head': 2, 'tag': 'JJ', 'id': 6},
                              {'value': 'JJ', 'head': 2, 'tag': 'JJ', 'id': 7},
                              {'value': 'NN', 'head': 2, 'tag': 'NN', 'id': 8},
                              {'value': 'The', 'head': 5, 'tag': '', 'id': 9},
                              {'value': 'quick', 'head': 6, 'tag': '', 'id': 10},
                              {'value': 'brown', 'head': 7, 'tag': '', 'id': 11},
                              {'value': 'fox', 'head': 8, 'tag': '', 'id': 12},
                              {'value': 'VBD', 'head': 3, 'tag': 'VBD', 'id': 13},
                              {'value': 'PP', 'head': 3, 'tag': 'PP', 'id': 14},
                              {'value': 'jumped', 'head': 13, 'tag': '', 'id': 15},
                              {'value': 'IN', 'head': 14, 'tag': 'IN', 'id': 16},
                              {'value': 'NP', 'head': 14, 'tag': 'NP', 'id': 17},
                              {'value': 'over', 'head': 16, 'tag': '', 'id': 18},
                              {'value': 'DT', 'head': 17, 'tag': 'DT', 'id': 19},
                              {'value': 'JJ', 'head': 17, 'tag': 'JJ', 'id': 20},
                              {'value': 'NN', 'head': 17, 'tag': 'NN', 'id': 21},
                              {'value': 'the', 'head': 19, 'tag': '', 'id': 22},
                              {'value': 'lazy', 'head': 20, 'tag': '', 'id': 23},
                              {'value': 'dog', 'head': 21, 'tag': '', 'id': 24},
                              {'value': '.', 'head': 4, 'tag': '', 'id': 25}],
                'sentimentValue': 1,
                'parse': '(ROOT (S (NP (DT The) (JJ quick) (JJ brown) (NN fox)) (VP (VBD jumped) (PP (IN over) (NP (DT the) (JJ lazy) (NN dog)))) (. .)))',
                'sentiment_json': [{'value': 'ROOT', 'head': 0, 'tag': 1, 'id': 1},
                                   {'value': 'NP', 'head': 1, 'tag': 2, 'id': 2},
                                   {'value': '@S', 'head': 1, 'tag': 1, 'id': 3},
                                   {'value': 'DT', 'head': 2, 'tag': 2, 'id': 4},
                                   {'value': '@NP', 'head': 2, 'tag': 2, 'id': 5},
                                   {'value': 'The', 'head': 4, 'tag': '', 'id': 6},
                                   {'value': 'JJ', 'head': 5, 'tag': 2, 'id': 7},
                                   {'value': '@NP', 'head': 5, 'tag': 2, 'id': 8},
                                   {'value': 'quick', 'head': 7, 'tag': '', 'id': 9},
                                   {'value': 'JJ', 'head': 8, 'tag': 2, 'id': 10},
                                   {'value': 'NN', 'head': 8, 'tag': 2, 'id': 11},
                                   {'value': 'brown', 'head': 10, 'tag': '', 'id': 12},
                                   {'value': 'fox', 'head': 11, 'tag': '', 'id': 13},
                                   {'value': 'VP', 'head': 3, 'tag': 2, 'id': 14},
                                   {'value': '.', 'head': 3, 'tag': 2, 'id': 15},
                                   {'value': 'VBD', 'head': 14, 'tag': 2, 'id': 16},
                                   {'value': 'PP', 'head': 14, 'tag': 2, 'id': 17},
                                   {'value': 'jumped', 'head': 16, 'tag': '', 'id': 18},
                                   {'value': 'IN', 'head': 17, 'tag': 2, 'id': 19},
                                   {'value': 'NP', 'head': 17, 'tag': 2, 'id': 20},
                                   {'value': 'over', 'head': 19, 'tag': '', 'id': 21},
                                   {'value': 'DT', 'head': 20, 'tag': 2, 'id': 22},
                                   {'value': '@NP', 'head': 20, 'tag': 1, 'id': 23},
                                   {'value': 'the', 'head': 22, 'tag': '', 'id': 24},
                                   {'value': 'JJ', 'head': 23, 'tag': 1, 'id': 25},
                                   {'value': 'NN', 'head': 23, 'tag': 3, 'id': 26},
                                   {'value': 'lazy', 'head': 25, 'tag': '', 'id': 27},
                                   {'value': 'dog', 'head': 26, 'tag': '', 'id': 28},
                                   {'value': '.', 'head': 15, 'tag': '', 'id': 29}],
                'tokens': [{'sentiment': 'Negative', 'token': 'The', 'sentimentValue': 1},
                           {'sentiment': 'Negative', 'token': 'quick', 'sentimentValue': 1},
                           {'sentiment': 'Negative', 'token': 'brown', 'sentimentValue': 1},
                           {'sentiment': 'Negative', 'token': 'fox', 'sentimentValue': 1},
                           {'sentiment': 'Negative', 'token': 'jumped', 'sentimentValue': 1},
                           {'sentiment': 'Negative', 'token': 'over', 'sentimentValue': 1},
                           {'sentiment': 'Negative', 'token': 'the', 'sentimentValue': 1},
                           {'sentiment': 'Negative', 'token': 'lazy', 'sentimentValue': 1},
                           {'sentiment': 'Negative', 'token': 'dog', 'sentimentValue': 1},
                           {'sentiment': 'Negative', 'token': '.', 'sentimentValue': 1}]}],
            'entities': [
                {'entityid': 1, 'mentions': [
                    {'head': 3, 'number': 'SINGULAR', 'mentiontype': 'NOMINAL', 'tokspan_in_sentence': [0, 4],
                     'mentionid': 1, 'sentence': 0, 'animacy': 'ANIMATE', 'gender': 'MALE', 'representative': True}]},
                {'entityid': 2, 'mentions': [
                    {'head': 8, 'number': 'SINGULAR', 'mentiontype': 'NOMINAL', 'tokspan_in_sentence': [6, 9],
                     'mentionid': 2, 'sentence': 0, 'animacy': 'ANIMATE', 'gender': 'UNKNOWN',
                     'representative': True}]}]}
        self.assertEqual(results, desired_results)

    def test_run_parse(self):
        self.op.analysisType = ['parse']
        results = self.op.run(self.test_data)
        desired_results = {
            'sentences': [{
                'parse': '(ROOT (S (NP (DT The) (JJ quick) (JJ brown) (NN fox)) (VP (VBD jumped) (PP (IN over) (NP (DT the) (JJ lazy) (NN dog)))) (. .)))',
                'deps_json': [{'tag': 'S', 'value': 'S', 'head': 0, 'id': 1},
                              {'tag': 'NP', 'value': 'NP', 'head': 1, 'id': 2},
                              {'tag': 'VP', 'value': 'VP', 'head': 1, 'id': 3},
                              {'tag': '.', 'value': '.', 'head': 1, 'id': 4},
                              {'tag': 'DT', 'value': 'DT', 'head': 2, 'id': 5},
                              {'tag': 'JJ', 'value': 'JJ', 'head': 2, 'id': 6},
                              {'tag': 'JJ', 'value': 'JJ', 'head': 2, 'id': 7},
                              {'tag': 'NN', 'value': 'NN', 'head': 2, 'id': 8},
                              {'tag': '', 'value': 'The', 'head': 5, 'id': 9},
                              {'tag': '', 'value': 'quick', 'head': 6, 'id': 10},
                              {'tag': '', 'value': 'brown', 'head': 7, 'id': 11},
                              {'tag': '', 'value': 'fox', 'head': 8, 'id': 12},
                              {'tag': 'VBD', 'value': 'VBD', 'head': 3, 'id': 13},
                              {'tag': 'PP', 'value': 'PP', 'head': 3, 'id': 14},
                              {'tag': '', 'value': 'jumped', 'head': 13, 'id': 15},
                              {'tag': 'IN', 'value': 'IN', 'head': 14, 'id': 16},
                              {'tag': 'NP', 'value': 'NP', 'head': 14, 'id': 17},
                              {'tag': '', 'value': 'over', 'head': 16, 'id': 18},
                              {'tag': 'DT', 'value': 'DT', 'head': 17, 'id': 19},
                              {'tag': 'JJ', 'value': 'JJ', 'head': 17, 'id': 20},
                              {'tag': 'NN', 'value': 'NN', 'head': 17, 'id': 21},
                              {'tag': '', 'value': 'the', 'head': 19, 'id': 22},
                              {'tag': '', 'value': 'lazy', 'head': 20, 'id': 23},
                              {'tag': '', 'value': 'dog', 'head': 21, 'id': 24},
                              {'tag': '', 'value': '.', 'head': 4, 'id': 25}],
                'tokens': [{'token': 'The'}, {'token': 'quick'}, {'token': 'brown'},
                           {'token': 'fox'}, {'token': 'jumped'}, {'token': 'over'},
                           {'token': 'the'}, {'token': 'lazy'}, {'token': 'dog'},
                           {'token': '.'}]}],
            'entities': [
                {'entityid': 1, 'mentions': [
                    {'number': 'SINGULAR', 'gender': 'MALE', 'mentionid': 1, 'tokspan_in_sentence': [0, 4], 'head': 3,
                     'representative': True, 'mentiontype': 'NOMINAL', 'animacy': 'ANIMATE', 'sentence': 0}]},
                {'entityid': 2, 'mentions': [
                    {'number': 'SINGULAR', 'gender': 'UNKNOWN', 'mentionid': 2, 'tokspan_in_sentence': [6, 9],
                     'head': 8, 'representative': True, 'mentiontype': 'NOMINAL', 'animacy': 'ANIMATE',
                     'sentence': 0}]}]}
        self.assertEqual(results, desired_results)

    def test_run_coref(self):
        self.op.analysisType = ['tokenize', 'ssplit', 'coref']
        results = self.op.run(self.test_data)
        desired_results = {
            'sentences': [{
                'deps_json': [{'id': 1, 'value': 'S', 'tag': 'S', 'head': 0},
                              {'id': 2, 'value': 'NP', 'tag': 'NP', 'head': 1},
                              {'id': 3, 'value': 'VP', 'tag': 'VP', 'head': 1},
                              {'id': 4, 'value': '.', 'tag': '.', 'head': 1},
                              {'id': 5, 'value': 'DT', 'tag': 'DT', 'head': 2},
                              {'id': 6, 'value': 'JJ', 'tag': 'JJ', 'head': 2},
                              {'id': 7, 'value': 'JJ', 'tag': 'JJ', 'head': 2},
                              {'id': 8, 'value': 'NN', 'tag': 'NN', 'head': 2},
                              {'id': 9, 'value': 'The', 'tag': '', 'head': 5},
                              {'id': 10, 'value': 'quick', 'tag': '', 'head': 6},
                              {'id': 11, 'value': 'brown', 'tag': '', 'head': 7},
                              {'id': 12, 'value': 'fox', 'tag': '', 'head': 8},
                              {'id': 13, 'value': 'VBD', 'tag': 'VBD', 'head': 3},
                              {'id': 14, 'value': 'PP', 'tag': 'PP', 'head': 3},
                              {'id': 15, 'value': 'jumped', 'tag': '', 'head': 13},
                              {'id': 16, 'value': 'IN', 'tag': 'IN', 'head': 14},
                              {'id': 17, 'value': 'NP', 'tag': 'NP', 'head': 14},
                              {'id': 18, 'value': 'over', 'tag': '', 'head': 16},
                              {'id': 19, 'value': 'DT', 'tag': 'DT', 'head': 17},
                              {'id': 20, 'value': 'JJ', 'tag': 'JJ', 'head': 17},
                              {'id': 21, 'value': 'NN', 'tag': 'NN', 'head': 17},
                              {'id': 22, 'value': 'the', 'tag': '', 'head': 19},
                              {'id': 23, 'value': 'lazy', 'tag': '', 'head': 20},
                              {'id': 24, 'value': 'dog', 'tag': '', 'head': 21},
                              {'id': 25, 'value': '.', 'tag': '', 'head': 4}],
                'tokens': [{'token': 'The'}, {'token': 'quick'}, {'token': 'brown'},
                           {'token': 'fox'}, {'token': 'jumped'}, {'token': 'over'},
                           {'token': 'the'}, {'token': 'lazy'}, {'token': 'dog'},
                           {'token': '.'}]}],
            'entities': [
                {'entityid': 1, 'mentions': [
                    {'gender': 'MALE', 'representative': True, 'sentence': 0, 'mentiontype': 'NOMINAL',
                     'animacy': 'ANIMATE', 'mentionid': 1, 'tokspan_in_sentence': [0, 4],
                     'number': 'SINGULAR', 'head': 3}]},
                {'entityid': 2, 'mentions': [
                    {'gender': 'UNKNOWN', 'representative': True, 'sentence': 0, 'mentiontype': 'NOMINAL',
                     'animacy': 'ANIMATE', 'mentionid': 2, 'tokspan_in_sentence': [6, 9],
                     'number': 'SINGULAR', 'head': 8}]}],
        }
        self.assertEqual(results, desired_results)

    def test_run_relation(self):
        self.op.analysisType = ['parse', 'relation']
        results = self.op.run(self.test_data)
        desired_results = {
            'sentences': [{
                'tokens': [{'token': 'The'}, {'token': 'quick'}, {'token': 'brown'},
                           {'token': 'fox'}, {'token': 'jumped'}, {'token': 'over'},
                           {'token': 'the'}, {'token': 'lazy'}, {'token': 'dog'},
                           {'token': '.'}],
                'relations': [
                    {'object': {'end': 9, 'start': 7, 'lemma': 'lazy dog'},
                     'relation': {'end': 6, 'start': 4, 'lemma': 'jump over'},
                     'subject': {'end': 4, 'start': 1, 'lemma': 'quick brown fox'}},
                    {'object': {'end': 9, 'start': 8, 'lemma': 'dog'},
                     'relation': {'end': 6, 'start': 4, 'lemma': 'jump over'},
                     'subject': {'end': 4, 'start': 3, 'lemma': 'fox'}},
                    {'object': {'end': 9, 'start': 8, 'lemma': 'dog'},
                     'relation': {'end': 6, 'start': 4, 'lemma': 'jump over'},
                     'subject': {'end': 4, 'start': 1, 'lemma': 'quick fox'}},
                    {'object': {'end': 9, 'start': 8, 'lemma': 'dog'},
                     'relation': {'end': 6, 'start': 4, 'lemma': 'jump over'},
                     'subject': {'end': 4, 'start': 1, 'lemma': 'quick brown fox'}},
                    {'object': {'end': 9, 'start': 7, 'lemma': 'lazy dog'},
                     'relation': {'end': 6, 'start': 4, 'lemma': 'jump over'},
                     'subject': {'end': 4, 'start': 2, 'lemma': 'brown fox'}},
                    {'object': {'end': 9, 'start': 8, 'lemma': 'dog'},
                     'relation': {'end': 6, 'start': 4, 'lemma': 'jump over'},
                     'subject': {'end': 4, 'start': 2, 'lemma': 'brown fox'}},
                    {'object': {'end': 9, 'start': 7, 'lemma': 'lazy dog'},
                     'relation': {'end': 6, 'start': 4, 'lemma': 'jump over'},
                     'subject': {'end': 4, 'start': 1, 'lemma': 'quick fox'}},
                    {'object': {'end': 9, 'start': 7, 'lemma': 'lazy dog'},
                     'relation': {'end': 6, 'start': 4, 'lemma': 'jump over'},
                     'subject': {'end': 4, 'start': 3, 'lemma': 'fox'}}],
                'deps_json': [{'head': 0, 'id': 1, 'value': 'S', 'tag': 'S'},
                              {'head': 1, 'id': 2, 'value': 'NP', 'tag': 'NP'},
                              {'head': 1, 'id': 3, 'value': 'VP', 'tag': 'VP'},
                              {'head': 1, 'id': 4, 'value': '.', 'tag': '.'},
                              {'head': 2, 'id': 5, 'value': 'DT', 'tag': 'DT'},
                              {'head': 2, 'id': 6, 'value': 'JJ', 'tag': 'JJ'},
                              {'head': 2, 'id': 7, 'value': 'JJ', 'tag': 'JJ'},
                              {'head': 2, 'id': 8, 'value': 'NN', 'tag': 'NN'},
                              {'head': 5, 'id': 9, 'value': 'The', 'tag': ''},
                              {'head': 6, 'id': 10, 'value': 'quick', 'tag': ''},
                              {'head': 7, 'id': 11, 'value': 'brown', 'tag': ''},
                              {'head': 8, 'id': 12, 'value': 'fox', 'tag': ''},
                              {'head': 3, 'id': 13, 'value': 'VBD', 'tag': 'VBD'},
                              {'head': 3, 'id': 14, 'value': 'PP', 'tag': 'PP'},
                              {'head': 13, 'id': 15, 'value': 'jumped', 'tag': ''},
                              {'head': 14, 'id': 16, 'value': 'IN', 'tag': 'IN'},
                              {'head': 14, 'id': 17, 'value': 'NP', 'tag': 'NP'},
                              {'head': 16, 'id': 18, 'value': 'over', 'tag': ''},
                              {'head': 17, 'id': 19, 'value': 'DT', 'tag': 'DT'},
                              {'head': 17, 'id': 20, 'value': 'JJ', 'tag': 'JJ'},
                              {'head': 17, 'id': 21, 'value': 'NN', 'tag': 'NN'},
                              {'head': 19, 'id': 22, 'value': 'the', 'tag': ''},
                              {'head': 20, 'id': 23, 'value': 'lazy', 'tag': ''},
                              {'head': 21, 'id': 24, 'value': 'dog', 'tag': ''},
                              {'head': 4, 'id': 25, 'value': '.', 'tag': ''}],
                'parse': '(ROOT (S (NP (DT The) (JJ quick) (JJ brown) (NN fox)) (VP (VBD jumped) (PP (IN over) (NP (DT the) (JJ lazy) (NN dog)))) (. .)))'}],
            'entities': [
                {'entityid': 1, 'mentions': [
                    {'mentionid': 1, 'sentence': 0, 'mentiontype': 'NOMINAL', 'representative': True,
                     'tokspan_in_sentence': [0, 4], 'head': 3, 'animacy': 'ANIMATE', 'number': 'SINGULAR',
                     'gender': 'MALE'}]},
                {'entityid': 2, 'mentions': [
                    {'mentionid': 2, 'sentence': 0, 'mentiontype': 'NOMINAL', 'representative': True,
                     'tokspan_in_sentence': [6, 9], 'head': 8, 'animacy': 'ANIMATE', 'number': 'SINGULAR',
                     'gender': 'UNKNOWN'}]}]}
        self.assertEqual(results, desired_results)


if __name__ == '__main__':
    unittest.main()