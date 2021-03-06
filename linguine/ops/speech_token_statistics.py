import json
from operator import itemgetter

import splat.complexity


class SpeechTokenStatistics:
    def run(self, data):
        results = []

        for corpus in data:
            tokens = json.loads(corpus.contents)
            for token in tokens:
                if token['word'] == '<sil>':
                    token['word'] = '[SIL]'
                token['length'] = token['end'] - token['start']  # All times in ms
            filler_tokens = list(token for token in tokens if token['filler'])
            word_tokens = list(token for token in tokens if not token['filler'])

            transcript = ' '.join(token['word'] for token in tokens)

            num_fillers = len(filler_tokens)
            num_words = len(word_tokens)
            filler_time = sum(map(itemgetter('length'), filler_tokens)) / 1000
            word_time = sum(map(itemgetter('length'), word_tokens)) / 1000
            total_time = tokens[-1]['end'] / 1000
            words_per_minute = num_words / (total_time / 60)

            word_token_text = [token['word'] for token in word_tokens]
            num_syllables = splat.complexity.num_syllables(word_token_text)
            syllables_per_minute = num_syllables / (total_time / 60)

            longest_tokens = list(map(lambda tok: {'word': tok['word'], 'length': tok['length'] / 1000},
                                      sorted(word_tokens, key=itemgetter('length'), reverse=True)[:10]))

            result = {
                'transcript': transcript,
                'base_stats': {
                    'num_fillers': num_fillers,
                    'num_words': num_words,
                    'filler_time': filler_time,
                    'word_time': word_time,
                    'total_time': total_time,
                    'words_per_minute': words_per_minute,
                    'syllables_per_minute': syllables_per_minute,
                },
                'longest_tokens': longest_tokens
            }

            results.append(result)

        return results
