
import random, os, re

class WordRecordIndex:
    word_record_map={};
    
    def UpdateIndex(self, word, record_num):
        #word = re.sub('[^A-Za-z0-9]+', '', word).lower()
        self.word_record_map.setdefault(word, set()).add(record_num);

    def QueryWord(self, word):
        word = re.sub('[^A-Za-z0-9]+', '', word).lower()       
        return self.word_record_map.get(word);        
        
        
class FoodRecord:
    review_score=-1
    record_string=''
    tscore=-1;

    def __init__(self, rec_string, record_num):
        global word_record_index
        self.record_string=rec_string
        words=''
        for line in rec_string.split('\n'):
            splitline = [sl.strip() for sl in line.split(':', 1)]

            if len(splitline)==1:
                words+=splitline[0]

            elif splitline[0]=='review/score':
                self.review_score = float(splitline[1])

            elif splitline[0]=='review/summary':
                words+=splitline[1]

            elif splitline[0]=='review/text':
                words+=splitline[1]

            

        words = re.sub('[^A-Za-z0-9 ]+', '', words).lower()

        for word in set(words.split()):
            word_record_index.UpdateIndex(word, record_num);

        self.tscore = self.review_score*10000 + len(words);
            

word_record_index=WordRecordIndex()
all_records=[]

def ReadAndIndexFileData():
    global word_record_index
    global all_records
    
    word_record_index=WordRecordIndex()

    all_records=[]

    random_indices_fname = os.path.join(os.path.dirname(__file__),
                                        '../data/random_indices.txt')
    
    with open(random_indices_fname, 'r') as f:
        sampled_indices=set([int(s) for s in f.read().split()])
    
    fname = os.path.join(os.path.dirname(__file__), '../data/foods.txt')

    rec_num=0;
    rec_added=0;
    with open(fname, 'r') as f:
        record_str='';
        for line in f:
            if line.isspace():
                if rec_num in sampled_indices:
                    all_records.append(FoodRecord(record_str.strip(), rec_added));
                    rec_added+=1;
                    
                rec_num+=1
                record_str='';
                
            else:
                record_str+=line;         
    

    if rec_num in sampled_indices:
        all_records.append(FoodRecord(record_str, rec_added));

    #raise

    result ='records read: ' + str(rec_num) + '\n' + \
            'records added: ' + str(rec_added) + '\n' + \
            'unique words added: ' + str(len(word_record_index.word_record_map))

    return result



    
        
               
    
