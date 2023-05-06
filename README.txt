Welcome to the README page that describes the code and datasets used in this project.

Please note that this page is not a comment on how the code works, but rather a step by step guide on which code to run and what repositories are necessary to run our code. 

In order to run the code in this repository, please ensure you have installed the following dependencies;

numpy, matplotlib, seaborn, pandas, json, plotly, dash, jupyter_dash.

The first part of this project comprised of collecting the earthquake data. This was done using an API through a free API website with a request limit. The code used to collect this information and store it in the dataset called "earthquakeAPI_data.csv" can be found in the "data_scraping.py" python file. This might take some time as the request rate is limited. If you don not want to run this file, all of the necessary data is already stored in the file "earthquakeAPI_data.csv"

After collecting the dataset, some exploratory data analysis was applied to the data, which included looking for nans, duplicated columns and adding some useful columns to the data. This process is done in the python script entitled "add_continent.py" which takes some time to run as one of the APIs has a strict request limit of 1 request per second. The processed data can thereafter be found in the "Earthquake_with_continents.csv" file. This is the file that contains all of the necessary data for the graphics that we generated. 

"Graphing.ipybn" contains all of the code that we used to generate the graphs of the project and can be run if the file "Earthquake_with_continents.csv" is found in the same repository. "app_bar.py" and "app_map.py" contain the code necessary to generate the interactive maps, this code is encompassed in the "Graphing.ipybn", but we needed a .py function in order to host the apps online in order to create an iframe to show our apps on our final webpage. 

We used the platform Render to host our Dash apps. The first Dash app (https://earthquake-dataviz.onrender.com) uses the main branch to run the code "app_bar.py". The second Dash app (https://earthquake-dataviz-map.onrender.com) uses the app2 branch to run the code "app_map.py".

index.html contains the html and css code we used to host our webpage on github pages. In order to see the webpage for this report please wither scroll down on the github page and click the "github-pages" button, following this on the page you are taken to click on the "View deployment" button. This will take you to our webpage containing all of our static and interactive graphs for the project. Or simply following the link: https://jane-hernandez.github.io/earthquake_dataviz/

Please note that due to the size of the data and the fact that we used a free hosting service for our Dash apps, there may be some delay in some of the interactivity of the data.

Group members: Giacomo Collesei, Angela Jane Salazar Hernandez, Spencer Patrick Gengis Marcinko
