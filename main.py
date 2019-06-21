from pprint import pprint as pp
from flask import Flask, flash, redirect, render_template, request, url_for
from weather import query_api

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('weather.html',
                           data = [ {'name':'Toronto'}, {'name':'Montreal'}, {'name':'Calgary'},
                                    {'name':'Ottawa'}, {'name':'Edmonton'}, {'name':'Mississauga'},
                                    {'name':'Winnipeg'}, {'name':'Vancouver'}, {'name':'Brampton'},
                                    {'name':'Quebec'}])


@app.route('/result', methods=['GET', 'POST'])
def result():
    data = []
    error = None
    select = request.form.get('comp_select')
    res = query_api(select)
    pp(res)
    print('Request was sent')

    if res:
        data.append(res)
    if len(data) != 2:
        error = 'Bad response from weather API'

    return render_template('result.html',
                           data = data, error = error)

if __name__ == '__main__':
    app.run(debug=True)