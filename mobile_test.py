from flask import Flask, send_from_directory, request
app = Flask(__name__, static_url_path='', static_folder='')


#------------------------------------------------------------------------------#
@app.route('/')
def index():
    return app.send_static_file('index.html')


#------------------------------------------------------------------------------#
@app.route('/css/<path:path>')
def css(path):
    return send_from_directory('css', path)


#------------------------------------------------------------------------------#
@app.route('/js/<path:path>')
def js(path):
    return send_from_directory('js', path)


#------------------------------------------------------------------------------#
@app.route('/debug')
def debug():
    print('==>', request.args.get('log'))
    return '{"status": 0}'


#------------------------------------------------------------------------------#
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
