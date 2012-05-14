# -*- coding: utf-8 -*-
import csv, json

language_correlation = {
    'name':'LanguageCorrelation',
    'children': []
}
from_to = {}

langs = ['JavaScript', 'Ruby', 'Python', 'Shell', 'Java', 'PHP', 'C', 'Perl', 'C++', 'Objective-C']

fcsv = open('language_correlation.csv', 'rb')
reader = csv.reader(fcsv)
headers = reader.next()
for record in reader:
    correlation, from_lang, to_lang, created_at = record
    if from_lang not in langs: continue
    correlation = float(correlation)
    if correlation < 10: continue
    if from_lang not in from_to:
        from_to[from_lang] = []
    from_to[from_lang].append({'name': to_lang, 'size': round(correlation)})
fcsv.close()

for from_lang in from_to:
    language_correlation['children'].append(
        {'name': from_lang, 'children': from_to[from_lang]})

print json.dumps(language_correlation)
