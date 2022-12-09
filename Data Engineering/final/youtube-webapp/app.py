
import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, json, request, redirect
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://<username>:<password>@<IP>/<database>?host=/cloudsql/<project_id>:<region>:<sql_instance_id>'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

engine = db.create_engine('postgresql://<username>:<password>@<IP>/<database>?host=/cloudsql/<project_id>:<region>:<sql_instance_id>')
results = engine.execute('select * from videos;')
videos = results.fetchall()

@app.route('/')
def index():
    return render_template('bootstrap_table.html', title='YouTube Cyber Security Videos', videos=videos)

if __name__ == '__main__':
    server_port = os.environ.get('PORT', '8080')
    app.run(debug=False, port=server_port, host='0.0.0.0')
