# -*- coding: utf-8 -*-
import csv, json

# build langs dict
langs = {}
flangs = open('top_langs.json')
top_langs = json.load(flangs)
idx = 0 # zero-based index
for tl in top_langs:
    if int(tl['pushes']) >= 100000:
        langs[tl['repository_language']] = {'id': idx, 'size': tl['pushes'], 'links': []}
        idx += 1
flangs.close()

# add correlation data to langs dict
fcsv = open('language_correlation.csv', 'rb')
reader = csv.reader(fcsv)
headers = reader.next()
for record in reader:
    correlation, from_lang, to_lang, created_at = record
    correlation = float(correlation)
    if from_lang not in langs or to_lang not in langs: continue
    langs[from_lang]['links'].append({'target': to_lang, 'value': correlation})
fcsv.close()

nodes = []
links = []
for lang in langs:
    if len(langs[lang]['links']) == 0: continue
    nodes.append({'name': lang, 'size': langs[lang]['size']})
    for link in langs[lang]['links']:
        links.append({'source': langs[lang]['id'],
                    'target': langs[link['target']]['id'],
                    'value': link['value']})

print json.dumps({'nodes': nodes, 'links': links})
