from flask import Flask, render_template
import pandas as pd;
from dao.base import Session, engine, Base, borrar_todo, exportar

app = Flask(__name__)


@app.route('/', methods=("POST", "GET"))
def html_table():

    db_df = pd.read_sql_query("SELECT * FROM informehw;", engine)
    #db_df.to_html(header="true", table_id="table")

    return render_template('lista.html',  tables=[db_df.to_html(classes='data')], titles=db_df.columns.values)


if __name__ == '__main__':
    app.run()