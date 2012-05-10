# -*- coding: utf-8 -*-
import re, csv, json
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

# only include words that include of a least 2 letters, numbers or underscores
re_word = re.compile(r'\w{2,}')
# very simple regex to match something that may be a URL, path, file name or assignment
re_uri = re.compile(r'\S*[\/\.=]\S*')

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
    tokens = word_tokenize(re.sub(re_uri, '', text.lower()))
    words = [w for w in tokens if len(w) > 1 and re.match(re_word, w) and w not in stopwords]
    for b in browsers:
        if re.search(browsers[b], text):
            # replace occurences of browser itself
            texts[b] += [w for w in words if not re.search(browsers[b], w)]
fcsv.close()

for b in texts:
    fdist = FreqDist(w for w in texts[b]).items()
    freqdists[b] = [(w, c) for w, c in fdist if c >= 10]

#print freqdists['chrome']
#print freqdists['ie']
print json.dumps(freqdists['ie'][:200])
