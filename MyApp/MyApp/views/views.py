from MyApp import app

import MyApp.core.data_reader
import MyApp.core.query_processor
import MyApp.testing.generate_random_queries

#import json

from flask import request
from flask import Response
from flask import jsonify

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/topMatchingDocs', methods=['GET'])
def topMatchingDocs():
    count=int(request.args.get('count'))
    query_str=request.args.get('query')
    
    result= MyApp.core.query_processor.FindTopMatchingDocs(count, query_str)
    #raise
    return 'Matching Docs: <br/> <br/>' + result.replace('\n', '<br/>')
    #return 'Matching Docs: <br/> <br/>' + result
    #return 'empty'


@app.route('/topMatchingDocsImproved', methods=['GET'])
def topMatchingDocsImproved():
    count=int(request.args.get('count'))
    query_str=request.args.get('query')
    
    result= MyApp.core.query_processor.FindTopMatchingDocsImproved(count, query_str)
    #raise
    return 'Matching Docs: <br/> <br/>' + result.replace('\n', '<br/>')

@app.route('/InitDataSources', methods=['POST'])
def InitDataSources():
    result = MyApp.core.data_reader.ReadAndIndexFileData();
    return result.replace('\n', '<br/>')

## make this a post method
@app.route('/GenerateRandomQueries/count=<int:count>', methods=['GET'])
def GenerateRandomQueries(count):
    result = MyApp.testing.generate_random_queries.GenerateRandomQueries(count)
    return 'Queries Generated'


    
    


