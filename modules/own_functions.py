import json
import collections
import xml.etree.ElementTree as ET

# почитать про collections

def read_json(file, max_len_word=6, top_words=10):
    with open(file, 'r', encoding='utf-8') as f:
        data = json.load(f)
        description_words = []
    for item in data['rss']['channel']['items']:
        description = [word for word in item['description'].split() if len(word) > max_len_word]
        description_words.extend(description)
        counter_words = collections.Counter(description_words)
    print(counter_words.most_common(top_words))

