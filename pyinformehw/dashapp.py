# -*- coding: utf-8 -*-
"""
Created on 26/03/2020

@author: Ignacio Lopez Martinez (@ignasilm)
"""
from os import path, chdir
import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_daq as daq
import pandas as pd
from dash.dependencies import Input, Output, State
from pyinformehw.dao.base import Session, engine, Base, borrar_todo, exportar


def leer_to_cargar_tabla():
    print('Entrando en leer_to_cargar_tabla ')

    records = []

    db_df = pd.read_sql_query("SELECT * FROM informehw;", engine)

    records = db_df.to_dict("rows")

    return records

app = dash.Dash(__name__)
server = app.server

columnas = [
    {"name": "Name", "id": "name", "type": "text", "editable": False},
    {"name": "usuario", "id": "usuario", "type": "text", "editable": False},
    {"name": "complet_name", "id": "complet_name", "type": "text", "editable": False},
    {"name": "model", "id": "model", "type": "text", "editable": False},
    {"name": "memorydevices", "id": "memorydevices", "type": "text", "editable": False},
    {"name": "zocalos_usados", "id": "zocalos_usados", "type": "text", "editable": False},
    {"name": "mem_instalada", "id": "mem_instalada", "type": "text", "editable": False},
    {"name": "speed", "id": "speed", "type": "text", "editable": False},
    {"name": "CPU", "id": "CPU", "type": "text", "editable": False},
    {"name": "ssd", "id": "ssd", "type": "text", "editable": False},
    {"name": "HD", "id": "HD", "type": "text", "editable": False},
    {"name": "capacidad_hd", "id": "capacidad_hd", "type": "text", "editable": False},
    {"name": "libre_hd", "id": "libre_hd", "type": "text", "editable": False},
    {"name": "uso_hd", "id": "uso_hd", "type": "text", "editable": False},
    {"name": "fecha", "id": "fecha", "type": "text", "editable": False},
    {"name": "core", "id": "core", "type": "text", "editable": False},
    {"name": "multicore", "id": "multicore", "type": "text", "editable": False}
    ]

app.layout = dbc.Container(
    children=[
        dbc.Row(
            [
                dbc.Col(
                    html.A(
                        id="dash-logo",
                        children=[html.Img(src=app.get_asset_url("logo_everis.png"))],
                        href="/",
                    ),
                    width=3
                ),
                dbc.Col(
                    html.Center(html.H2("Completar descripciones de SI/SE")),
                    width=9
                )
            ],
            justify="center"
        ),
        dbc.Row(
            [
                dbc.Col(
                    dash_table.DataTable(
                        id="data-table",
                        editable=False,
                        columns=columnas,
                        data=leer_to_cargar_tabla(),
                        fixed_rows={ 'headers': True, 'data': 0 },
                        style_table={
                                'maxHeight': '500px'
                        },
                        style_header= {
                            "backgroundColor": "rgb(2,21,70)",
                            "color": "white",
                            "textAlign": "center",
                        },
                        style_data={
                            'whiteSpace': 'normal',
                            'height': 'auto'
                        },
                        style_cell={'textAlign': 'left'},
                        
                    ),
                    width=12
                ),
            ],
            


        ),
    ],
)



@app.callback(
    [Output("data-table", "data")],
    [],
    []
)
def recargar_tabla():
    print('Entrando en recargar_tabla ')

    return leer_to_cargar_tabla()


#Si se ejecuta el package arranca por este metodo
def run():
    print('Iniciamos ejecucion de PyInformeHW Web')
    app.run_server(debug=True, dev_tools_hot_reload=True)
    leer_to_cargar_tabla()


if __name__ == "__main__":
    run()
    