import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html  
from dash.dependencies import Input, Output

df= pd.read_csv('Earthquake_with_continents.csv')

# Convert 'date' column to datetime format and create new 'month' column
df['date']=pd.to_datetime(df['date'])
df['month'] = df['date'].dt.month

# Select only relevant columns
df = df[["magnitude","title","date","mmi","tsunami","sig","type","nst","rms","depth",
        "latitude","longitude","continent","month"]]

# Set external stylesheets for the Dash app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
# Initialize the Dash app and server
app_map = dash.Dash(__name__, external_stylesheets = external_stylesheets)
server = app_map.server

list_continents = list(df['continent'].unique())

# Define the layout of the Dash app
app_map.layout = html.Div([
    html.Div([
    html.P( "Select a continent:", className = "control_label"),
    dcc.RadioItems(
        id="select_continent",
        options=list_continents,
        value="Europe",
        className="dcc_control",inline=True
    )
    ]),
    html.Div([
    dcc.Graph(id='map_graph')]),
    
    html.Div([
            html.Div(
                    [ dcc.Graph(id = 'scatter_graph')]),
            html.Div(
                    [ dcc.Graph(id = 'pie_graph')]),],
    className="row flex-display",),
    ],
id="mainContainer",
style={"display": "flex", "flex-direction": "column"})

# Define callback function to update the map graph when a new continent is selected
@app_map.callback(Output("map_graph","figure"),Input("select_continent","value"))
def map_events (continent): 
    # Filter dataframe to only include data from the selected continent
    temp = df[df['continent']==continent]
    # Set Mapbox access token
    px.set_mapbox_access_token(open(".mapbox_token").read())
    # Create scatter mapbox plot with magnitude and location of earthquakes on the selected continent
    fig = px.scatter_mapbox(temp, lat="latitude", lon="longitude", color="magnitude", size ="magnitude",
                      color_continuous_scale=px.colors.sequential.Redor, size_max = 5,zoom=2,hover_name="title",hover_data=['date'])
    fig.update_traces(hovertemplate = "<b>%{hovertext}</b><br><br>Date: %{customdata[0]}<extra></extra>")
    return fig

# Define callback function to update the scatter graph when a new continent is selected
@app_map.callback(Output("scatter_graph","figure"),Input("select_continent","value"))

def scatter_graph(continent):
    # Filter dataframe to only include data from the selected continent
    temp = df[(df['continent']==continent)&(df['type']=="earthquake")]
    # Create scatter plot of earthquake significance (sig) and root mean square (rms)
    fig = px.scatter(temp, x='sig', y='rms', color='depth',color_continuous_scale=px.colors.sequential.Emrld,hover_name="title",hover_data=['date','depth'])
    # Customize layout and hovertext on the scatter graph
    fig.update_layout(plot_bgcolor='#E7ECEF',yaxis_title="Root Mean Square (Seismic Waves)", xaxis_title="Significance of the event")
    fig.update_traces(hovertemplate = "<b>%{hovertext}</b><br><br>Date: %{customdata[0]}<br>RMS: %{y} <br>Significance Score: %{x}<br>Hypocenter Depth: %{customdata[1]} KM")
    fig.update_coloraxes(colorbar_title="Depth")
    return fig

# Define callback function to update the pie graph when a new continent is selected
@app_map.callback(Output("pie_graph","figure"),Input("select_continent","value"))

def pie_graph(continent):
    temp = df[(df['continent']==continent)&(df['type']=="earthquake")]
    # Create a dictionary to assign colors to each value of tsunami column
    tsunami_pal = {"No Tsunami":"#F5853F","Tsunami Event":"#0E34A0"}
    counts = pd.DataFrame(temp['tsunami'].value_counts()).reset_index()
    counts.replace({0:"No Tsunami",1:"Tsunami Event"},inplace=True)
    # Create a pie chart using Plotly Express with the count of tsunamis and color assigned based on the tsunami_pal dictionary
    fig = px.pie(counts, values='tsunami', names='index', color_discrete_map=tsunami_pal,color='index')
    fig.update_traces(hovertemplate = "<b>%{label}</b><br>Count: %{value}<br><br>")
    fig.update_layout(title_text="Number of tsunamis caused by the earthquakes")
    return fig

if __name__ == '__main__':
    app_map.run_server()
