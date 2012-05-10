# -*- coding: utf-8 -*-
import re, csv
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

# only include words made up of letters, numbers, hyphens and underscores
re_word = re.compile(r'[\w-]')
stopwords = set(stopwords.words('english'))
texts = {'ie': [], 'firefox': [], 'chrome': [], 'opera': [], 'safari': []}
freqdists = {}

browsers = {
    'ie': re.compile(r'\b(?:ie\s*\d*|internet\s*explorer)\b', re.I),
    'firefox': re.compile(r'\bfirefox\b', re.I),
    'chrome': re.compile(r'\bchrome\b', re.I),
    'opera': re.compile(r'\bopera\b', re.I),
    'safari': re.compile(r'\bsafari\b', re.I),
}

#fcsv = open('browser_mentions.ext.csv', 'rb')
fcsv = open('browser_mentions.csv', 'rb')
reader = csv.reader(fcsv)
headers = reader.next()
for record in reader:
    text = record[0]
    tokens = word_tokenize(text.lower())
    words = [w for w in tokens if len(w) > 1 and re.match(re_word, w) and w not in stopwords]
    for b in browsers:
        if re.search(browsers[b], text):
            texts[b] += words
fcsv.close()

for b in texts:
    fdist = FreqDist(w for w in texts[b]).items()
    freqdists[b] = [(w, c) for w, c in fdist if c >= 10]

print freqdists['chrome']
