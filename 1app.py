import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
import pandas as pd
import joblib
import numpy as np

# Load the trained model
model = joblib.load('sales_model.pkl')

# Initialize the Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Adidas Sales Prediction"),
    html.Div([
        html.Label("Product"),
        dcc.Input(id='product', type='number', value=0),
    ]),
    html.Div([
        html.Label("Region"),
        dcc.Input(id='region', type='number', value=0),
    ]),
    html.Div([
        html.Label("Units Sold"),
        dcc.Input(id='units_sold', type='number', value=100),
    ]),
    html.Div([
        html.Label("Year"),
        dcc.Input(id='year', type='number', value=2023),
    ]),
    html.Div([
        html.Label("Month"),
        dcc.Input(id='month', type='number', value=10),
    ]),
    html.Div([
        html.Label("Day"),
        dcc.Input(id='day', type='number', value=1),
    ]),
    html.Div([
        html.Label("Day of Week"),
        dcc.Input(id='day_of_week', type='number', value=0),
    ]),
    html.Div([
        html.Label("Week of Year"),
        dcc.Input(id='week_of_year', type='number', value=40),
    ]),
    html.Button('Predict', id='predict-button', n_clicks=0),
    html.Div(id='prediction-output')
])

@app.callback(
    Output('prediction-output', 'children'),
    Input('predict-button', 'n_clicks'),
    State('product', 'value'),
    State('region', 'value'),
    State('units_sold', 'value'),
    State('year', 'value'),
    State('month', 'value'),
    State('day', 'value'),
    State('day_of_week', 'value'),
    State('week_of_year', 'value')
)
def predict_sales(n_clicks, product, region, units_sold, year, month, day, day_of_week, week_of_year):
    if n_clicks > 0:
        input_data = np.array([[product, region, units_sold, year, month, day, day_of_week, week_of_year]])
        prediction = model.predict(input_data)
        return f'Predicted Total Sales: ${prediction[0]:,.2f}'
    return ''

if __name__ == '__main__':
    app.run_server(debug=True)