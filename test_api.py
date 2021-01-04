# -*- coding: utf-8 -*-


import flask
from flask import Flask, request, jsonify
from flask import render_template
import pymysql
from database.database import db_connection
import json
app = Flask(__name__) 
app.config['DEBUG'] = True

connection = db_connection()

""" Server Call Back Functions"""

@app.route('/')
def home():
    return render_template('Resume.html')

@app.route('/gor')
def got():
    return render_template('gor.html')

@app.route('/framework_design')
def framework_design():
    return render_template('pseudo2source.html')

@app.route('/api_documentation')
def api_documentation():
    return render_template('skillz_doc.html')


@app.route('/get_data',methods=['GET'])
def get_data():
    cursor = connection.cursor()
    cursor.execute("show columns from richie31.company_email1")
    column_heads = cursor.fetchall()
    columns = [column_heads[i][0] for i in range(len(column_heads))]
    sql_query = "select * from richie31.company_email1;"
    cursor.execute(sql_query)
    email_list = cursor.fetchall()
    response = {'columns': columns,
                'data':email_list}
    return jsonify(response)
    

if __name__ == '__main__':
    app.run(host = "0.0.0.0",port = 5001, debug = True)
    