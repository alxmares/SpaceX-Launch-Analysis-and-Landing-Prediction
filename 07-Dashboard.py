import pandas as pd 
import dash
from dash import dcc, html
import plotly.express as px
from dash.dependencies import Input, Output

spacex_df = pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/spacex_launch_dash.csv") 
#print(spacex_df.columns.tolist())


app = dash.Dash(__name__)

# Crear la disposición de la aplicación Dash
app.layout = html.Div([
    dcc.Dropdown(id='site-dropdown',
                 options=[
                     {'label': 'All Sites', 'value': 'ALL'},
                     *[
                         {'label': site, 'value': site}
                         for site in spacex_df['Launch Site'].unique()
                     ]
                 ],
                 value='ALL',
                 placeholder="Select a Launch Site here",
                 searchable=True
                 ),
    dcc.Graph(id='success-pie-chart'),
    dcc.RangeSlider(id='payload-slider',
                    min=0, max=10000, step=1000,
                    marks={i: str(i) for i in range(0, 10001, 1000)},
                    value=[0, 10000]
                    ),
    dcc.Graph(id='success-payload-scatter-chart')
])

# Callback para actualizar el gráfico de pastel
@app.callback(
    Output(component_id='success-pie-chart', component_property='figure'),
    Input(component_id='site-dropdown', component_property='value')
)
def get_pie_chart(entered_site):
    filtered_df = spacex_df
    if entered_site == 'ALL':
        fig = px.pie(filtered_df, values='class',
                     names='class',
                     title='Total Success Launches for All Sites')
        return fig
    else:
        filtered_df = spacex_df[spacex_df['Launch Site'] == entered_site]
        fig = px.pie(filtered_df, names='class',
                     title=f'Total Success Launches for Site {entered_site}')
        return fig

# Callback para actualizar el gráfico de dispersión
@app.callback(
    Output(component_id='success-payload-scatter-chart', component_property='figure'),
    [Input(component_id='site-dropdown', component_property='value'),
     Input(component_id='payload-slider', component_property='value')]
)
def update_scatter_chart(selected_site, selected_payload):
    filtered_df = spacex_df[(spacex_df['Payload Mass (kg)'] >= selected_payload[0]) &
                            (spacex_df['Payload Mass (kg)'] <= selected_payload[1])]
    if selected_site == 'ALL':
        fig = px.scatter(filtered_df, x='Payload Mass (kg)', y='class',
                         color='Booster Version Category',
                         title='Payload vs. Outcome for All Sites')
        return fig
    else:
        filtered_df = filtered_df[filtered_df['Launch Site'] == selected_site]
        fig = px.scatter(filtered_df, x='Payload Mass (kg)', y='class',
                         color='Booster Version Category',
                         title=f'Payload vs. Outcome for Site {selected_site}')
        return fig

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)