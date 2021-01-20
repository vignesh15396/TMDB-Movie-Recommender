import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn
from wsgiref import simple_server
from flask import Flask, request, render_template,jsonify
from flask_cors import CORS,cross_origin
from flask import Response
import os
from flask_cors import CORS, cross_origin
import json

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
#dashboard.bind(app)
CORS(app)


@app.route("/", methods=['GET'])
@cross_origin()
def home():
    list_df = pd.read_csv('plot.csv')
    movie_list="%".join(list(list_df.columns))
    return render_template('index.html',movie_list=movie_list)
    # return render_template('index.html')

@app.route("/plot", methods=['POST'])
@cross_origin()
def plot():
    print('in plot')
    if request.method=='POST':
        print('if')
        try:
            print('try')
            movie=request.form['movie']
            print('after movie')
            plot_df = pd.read_csv('plot.csv')
            cast_df = pd.read_csv('cast.csv')
            p1 = 0
            p2 = 0
            plot_str=''
            cast_str=''
            for i in list(plot_df[movie][0:10]):
                p1 += 1
                plot_str=plot_str+str(p1)+') '+i+'.'
            for i in list(cast_df[movie][0:10]):
                p2 += 1
                cast_str=cast_str+str(p2)+') '+i+'.'
            return render_template('plot.html', movies=plot_str,movies2=cast_str)
        except Exception as e:
            print('The Exception message is: ', e)
            return 'something is wrong'

@app.route("/top", methods=['POST'])
@cross_origin()
def top():
    print('in top')
    if request.method=='POST':
        print('if')
        try:
            print('try')
            print('after movie')
            top_df = pd.read_csv('top_pop.csv')
            print('top df')
            p1 = 0
            p2=0
            top_str=''
            pop_str=''
            for i in list(top_df['top'][0:10]):
                p1 += 1
                top_str=top_str+str(p1)+') '+i+'.'
            for i in list(top_df['popular'][0:10]):
                p2 += 1
                pop_str=pop_str+str(p2)+') '+i+'.'
            print('after for')
            return render_template('top.html', top=top_str,pop=pop_str)
        except Exception as e:
            print('The Exception message is: ', e)
            return 'something is wrong'


#port = int(os.getenv("PORT",5000))
if __name__ == "__main__":
    host = '0.0.0.0'
    port = 8000
    httpd = simple_server.make_server(host, port, app)
    # print("Serving on %s %d" % (host, port))
    httpd.serve_forever()