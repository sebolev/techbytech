import json
import csv
import re

from nltk.tokenize import RegexpTokenizer
from jsoncomment import JsonComment
from collections import namedtuple

Graph1 = namedtuple('Graph1',
        ['drug',
        'pubmed_title',
        'journal']
)
Graph2 = namedtuple('Graph2',
        ['drug',
        'scientific_title',
        'journal']
)


def sanitize_json_string(str):
    json = JsonComment()
    json_obj = json.loads(str)
    return json_obj


def remove_words(str):
    pattern = r'(\\x.{2})+'
    mod_string = re.sub(pattern, '', str)
    return mod_string


def to_list_of_words(str):
    tk = RegexpTokenizer('\\w+', gaps=True)
    geek = tk.tokenize(str)
    return geek


def construct_graphs(pubmeds, drugs, clinical_trials):
    graph1 = []
    for drug in drugs:
        for pubmed in pubmeds:
            if(pubmed[1].lower().find(drug[1])!= -1):
                graph1.append(Graph1(drug[1], pubmed[1], pubmed[3]))

    graph2 = []
    for drug in drugs:
        for clinical_trial in clinical_trials:
            if(clinical_trial[1].lower().find(drug[1])!= -1):
                graph2.append(Graph2(drug[1], clinical_trial[1], clinical_trial[3]))
    return (graph1,graph2)


def save_results(graph1,graph2):
    with open('../output/graph1.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(Graph1._fields)
        writer.writerows(graph1)

    with open('../output/graph2.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(Graph2._fields)
        writer.writerows(graph2)


if __name__ == '__main__':

    with open('../input/pubmed.csv') as csv_object:
        pubmeds = csv.reader(csv_object, delimiter=',')

    with open('../input/pubmed.json') as j_object:
        pubmed = json.load(j_object)

    with open('../input/drugs.csv') as csv_object:
        drugs = csv.reader(csv_object, delimiter=',')

    with open("../input/clinical_trials.csv") as csv_object:
        clinical_trials = csv.reader(csv_object, delimiter=',')

    (graph1,graph2) = construct_graphs(pubmeds, drugs, clinical_trials)
    save_results(graph1,graph2)