
import MyApp.core.data_reader as data_reader
import collections
import heapq

def ProcessDoc(doc_score_map, docid):
    if docid in doc_score_map:
        doc_score_map[docid][0]+=1
    else:
        # break scores by first looking at review/score and then total review length
        doc_score_map[docid]=[1, data_reader.all_records[docid].review_score,
                              len(data_reader.all_records[docid].record_string)]

def FindTopMatchingDocs(count, query):
    doc_score_map={}
    for query_word in query.split(','):
        for docid in data_reader.word_record_index.QueryWord(query_word) or set():
            ProcessDoc(doc_score_map, docid)

    top_docs= collections.Counter(doc_score_map).most_common(count)
    
    return '\n\n'.join([data_reader.all_records[docid].record_string for \
            docid,_ in top_docs])
      

def FindTopMatchingDocsImproved(count, query):
    my_counter = collections.Counter(None)
    
    for query_word in query.split(','):
        my_counter += collections.Counter(data_reader.word_record_index.QueryWord(query_word))
        
    doc_score_list=[[freq*100000 + data_reader.all_records[docid].tscore, docid] for
                    docid,freq in my_counter.items()]

    top_docs= heapq.nlargest(count, doc_score_list)
    
    return '\n\n'.join([data_reader.all_records[docid].record_string for \
            _,docid in top_docs])    
    
