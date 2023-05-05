import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html  
from dash.dependencies import Input, Output
#import dataset
df= pd.read_csv('Earthquake_with_continents.csv')

df['date']=pd.to_datetime(df['date'])
df['month'] = df['date'].dt.month

df = df[["magnitude","title","date","mmi","tsunami","sig","type","nst","rms","depth",
        "latitude","longitude","continent","month"]]
#using the Dash web framework for building web application
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app_bar = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app_bar.server
colorscale = {'earthquake': '#FF595E','explosion':'#FFCA3A','quarry blast':'#8AC926','ice quake':'#1982C4'}
#sets up the layout of a Dash web application
app_bar.layout = html.Div([
    html.Div([
    html.P( "Select a month:", className = "control_label"),
    dcc.Dropdown(
        id="select_month",
        options=[
            {'label': 'January', 'value': 1},
            {'label': 'February', 'value': 2},
            {'label': 'March', 'value': 3},
            {'label': 'April', 'value': 4},
            {'label': 'May', 'value': 5},
            {'label': 'June', 'value': 6},
            {'label': 'July', 'value': 7},
            {'label': 'August', 'value': 8},
            {'label': 'September', 'value': 9},
            {'label': 'October', 'value': 10},
            {'label': 'November', 'value': 11},
            {'label': 'December', 'value': 12},
        ],
        value=1,
        className="dcc_control"
    )
    ]),
    html.Div([
    dcc.Graph(id='bar_graph')]),
    
    html.Div([
        html.Div([
    dcc.Dropdown(options=['earthquake', 'quarry blast', 'explosion','ice quake'], 
                 value=['earthquake','ice quake'], id='type_select', multi=True),
    html.Div(id='dd-output-container')
]),
				html.Div(
                    [ dcc.Graph(id = 'box_plot1')],
				),
				html.Div(
					[ dcc.Graph(id = 'box_plot2')],
				),
            html.Div(
					[ dcc.Graph(id = 'box_plot3')],
				),
			],
			className="row flex-display",
		),
	],
	id="mainContainer",
	style={"display": "flex", "flex-direction": "column"})
#setting a function that will update the "bar_graph" figure when the user selects a different month in the dropdown
@app_bar.callback(Output("bar_graph","figure"),Input("select_month","value"))

#define a function called bar_graph that takes a single input argument, month_value
def bar_graph(month_value):
    # Filter the dataframe by selected month
    temp = df[df['month'] == int(month_value)]
    # Sort the seismic event types by count and create a dataframe
    order = pd.DataFrame(temp['type'].value_counts(sort=True,ascending=False))
    order.reset_index(inplace=True)
    # Create a bar chart using plotly express
    fig = px.bar(order, y="index", x="type",category_orders=dict(type=order['index']),color="index",color_discrete_map=colorscale)
    fig.update_layout(xaxis_title="Count", yaxis_title="Seismic Event Type", legend_title="Seismic Event Type")
    fig.update_layout(title_text="Number of events per type")
    fig.update_traces(hovertemplate = "<b>%{y}</b><br><br>Count: %{x}")
    return fig

#updating the box_plot in the Dash app, taking two values as inputs
@app_bar.callback(Output("box_plot1","figure"),[Input("select_month","value"),Input("type_select","value")])

# Define a function called "box_magnitude" that takes two input arguments: "month_value" and "type_values"
def box_magnitude(month_value,type_values):
    # Filter the dataframe by selected month and selected seismic event types
    temp = df[(df['month'] == int(month_value))&(df['type'].isin(type_values))]
    # Create a box plot using the "px.box" function from the Plotly Express library
    fig = px.box(temp,x="type", y="magnitude", points="all",hover_name="title",color="type",color_discrete_map=colorscale)
    # Update the chart layout with axis titles and a legend title
    fig.update_layout(yaxis_title="Magnitude", xaxis_title="Seismic Event Type", legend_title="Seismic Event Type")
    # Set a custom hover template that displays the "title" value when the user hovers over a data point
    fig.update_traces(hovertemplate = "<b>%{hovertext}</b>")
    return fig

# Define a callback function for the "box_plot2" figure
@app_bar.callback(Output("box_plot2","figure"),[Input("select_month","value"),Input("type_select","value")])

def box_sig(month_value,type_values):
    # Filter the dataframe by selected month and selected seismic event types
    temp = df[(df['month'] == int(month_value))&(df['type'].isin(type_values))]
    fig = px.box(temp, x="type", y="sig", points="all",hover_name="title",color="type",color_discrete_map=colorscale)
    fig.update_layout(yaxis_title="Significance of the event", xaxis_title="Seismic Event Type", legend_title="Seismic Event Type")
    fig.update_traces(hovertemplate = "<b>%{hovertext}</b><br><b>Significance Score:</b> %{y}")
    return fig

# Define a callback function for the "box_plot3" figure
@app_bar.callback(Output("box_plot3","figure"),[Input("select_month","value"),Input("type_select","value")])

def box_depth(month_value,type_values):
    # Filter the dataframe by selected month and selected seismic event types
    temp = df[(df['month'] == int(month_value))&(df['type'].isin(type_values))]
    fig = px.box(temp,x="type", y="depth", points="all",hover_name="title",color="type",color_discrete_map=colorscale)
    fig.update_layout(yaxis_title="Hypocentrer Depth (KM)", xaxis_title="Seismic Event Type", legend_title="Seismic Event Type")
    fig.update_traces(hovertemplate = "<b>%{hovertext}</b><br><b>Hypocenter Depth:</b> %{y} KM")
    return fig

#run the Dash application
if __name__ == '__main__':
    app_bar.run_server()
