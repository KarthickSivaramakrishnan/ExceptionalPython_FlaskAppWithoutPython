from flask import Flask

app = Flask('SampleFlaskApp')

@app.route('/',methods=['GET'])
def index():
    return 'Welcome to Exceptional Python!!'

if __name__ == '__main__':
    app.run()