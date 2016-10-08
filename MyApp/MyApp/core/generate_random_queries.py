
import random
import os
import codecs
import re

import MyApp.core.data_reader

# use processedindees for generating this?

query_prefix='http://localhost:5000/topMatchingDocs/count=20&query='


def GenerateRandomQueries(count):
    global query_prefix

    MyApp.core.data_reader.ReadAndIndexFileData()

    random_queries_fname = os.path.join(os.path.dirname(__file__),
                                        '../data/random_queries.txt')
    

    with open(random_queries_fname, 'w') as f:
        for _ in range(count):
            query_length = random.randint(1,10)
            query = ','.join(random.sample(list(MyApp.core.data_reader.word_record_index.word_record_map),
                                           query_length));
            f.write(query_prefix+query+'\n');
            
        
        
def GenerateRandomQueriesFromFile(count):
    global query_prefix
    data_fname = os.path.join(os.path.dirname(__file__),
                                        '../data/foods.txt')
    all_words=set()
    with codecs.open(data_fname, 'r', "iso-8859-1") as f:
        for line in f:
            splitline=line.split(':')
            if (len(splitline)>1) & (splitline[0]!='review/summary') & (splitline[0]!='review/text'):
                continue;
            for word in splitline[-1].split():
                all_words.add(word)
        

    random_queries_fname = os.path.join(os.path.dirname(__file__),
                                        '../data/random_queries.txt')

    processed_words=set()
    for word in all_words:
        word = re.sub('[^A-Za-z0-9]+', '', word)
        processed_words.add(word)

    with open(random_queries_fname, 'w') as f:
        for _ in range(count):
            query_length = random.randint(1,10)
            query = ','.join(random.sample(processed_words, query_length));
            f.write(query_prefix+query+'\n');        
