from flask import Flask, request, render_template

app = Flask(__name__, template_folder='')

default_key = '1'
key = default_key
@app.route('/', methods=['GET', 'POST'])

def mainpage():
  if 'key' in request.form:
    key = request.form['key']
  if request.method == 'POST' and request.form['submit'] == 'save':
    key = request.form['key']
    print(key)
  #return "ok"
  return render_template('index.html', key="ovidiu")

if __name__ == '__main__':
  app.run(host='0.0.0.0')
