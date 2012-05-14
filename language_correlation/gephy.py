# -*- coding: utf-8 -*-
import csv, json

alangs = ['JavaScript', 'Ruby', 'Python', 'Shell', 'Java', 'PHP', 'C', 'Perl', 'C++', 'Objective-C']

langs = []
lang_counts = {}
correlations = []

def lang_idx(lang):
    if lang not in langs:
        langs.append(lang)
    return langs.index(lang)

def update_lang_count(lang, incr):
    if lang not in lang_counts:
        lang_counts[lang] = 0
    lang_counts[lang] += incr

fcsv = open('language_correlation.csv', 'rb')
reader = csv.reader(fcsv)
headers = reader.next()
for record in reader:
    correlation, from_lang, to_lang, created_at = record
    correlation = float(correlation)
    if from_lang not in alangs or to_lang not in alangs: continue
#    if correlation < 1: continue
    from_idx = lang_idx(from_lang)
    to_idx =  lang_idx(to_lang)
    update_lang_count(from_lang, correlation)
    update_lang_count(to_lang, correlation)
    correlations.append((str(from_idx), str(to_idx), str(correlation)))
fcsv.close()

nodes = open('nodes.csv', 'wb')
nodes.write('Id,Label,Weight\n')
nodes.write('\n'.join([','.join((str(langs.index(l)), l, str(lang_counts[l]))) for l in langs]))
nodes.close()

edges = open('edges.csv', 'wb')
edges.write('Source,Target,Weight\n')
edges.write('\n'.join([','.join(c) for c in correlations]))
edges.close()
