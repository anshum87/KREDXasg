#python
from flask import Flask

import MyApp.core.data_reader

app = Flask(__name__)
#MyApp.core.data_reader.ReadAndIndexFileData();

import MyApp.views.views
