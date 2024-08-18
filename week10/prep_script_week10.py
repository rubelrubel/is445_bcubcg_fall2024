###############################################
#  1. Starting off building streamlit apps 
###############################################
# Start off in PL!  Open up the "ungraded VSCode" space and make the "inclass" notebook

# For Streamlit apps, we'll need to write our apps in .py files, not notebook files like we've been doing so far.
# For this, we'll be using VSCode to do this.
# (Note: there is technically a jupyterlab wrapper for Streamlit, but its just been developed so we won't be using it for this class.)

# Let's start with running a very simple streamlit app:
import streamlit as st

st.title('This is my fancy app!')

# after this point, things will be a little different if you are on PL or running the code locally on your computer
# I'll be running locally usually, but let's look at PL first:

# INSTRUCTIONS FOR RUNNING ON PL:
# 1. Open a "Terminal" by: View --> Terminal OR just the "Terminal" through the hamburger menu
# 2. run in terminal with: "streamlit run <the app .py file>"
# 3. click the "Open in Browser" link that pops up OR click on "Ports" and copy the URL
# 4. Open a Simple Browswer with View --> Command Palette --> Simple Browser: Show
# 5. use the URL from prior steps as intput into this simple browser

#**HERE** -- more about streamlit like here:
#* https://docs.streamlit.io/get-started/fundamentals/main-concepts (add to reading in syllabus & day page)
# do different text types!
# Altair plots

# day 2/3
# touch on widgets! -- do quick example of plot + widget, say we'll focus on Altair
# multi-page apps? ==> maybe day 2? ==> does this work with HF apps??
# matplotlib plots
#* https://docs.streamlit.io/develop/tutorials/databases <- touch on but say we'll be just doing csv files

###############################################
#  2. Vega-lite in Streamlit
###############################################

# While we'll be focusing on making Altair-based plots in Streamlit, if vega-lite is your jam,
# you can absolutely make vega-lite based plots with "st.vega_lite_chart": 
# https://docs.streamlit.io/develop/api-reference/charts/st.vega_lite_chart
# st.vega_lite_chart(data=None, spec=None, *, use_container_width=False, 
#    theme="streamlit", key=None, on_select="ignore", selection_mode=None, **kwargs)

# Example 1: from the st.vega_lite_chart docs -- you can pass data from Python + the vega-lite specification
import pandas as pd
import numpy as np

chart_data = pd.DataFrame(np.random.randn(200, 3), columns=["a", "b", "c"])

st.vega_lite_chart(
   chart_data,
   {
       "mark": {"type": "circle", "tooltip": True},
       "encoding": {
           "x": {"field": "a", "type": "quantitative"},
           "y": {"field": "b", "type": "quantitative"},
           "size": {"field": "c", "type": "quantitative"},
           "color": {"field": "c", "type": "quantitative"},
       },
   },
)

# Example 2: From our prior Altair work, we can also pass linked data through the specification.
#  This example is from when we built our dashboard:
spec = {
  # Data
  "data": {"url":"https://raw.githubusercontent.com/UIUC-iSchool-DataViz/is445_data/main/mobility.csv"},
  # Mark
  "mark": "bar",
  # Encoding
  "encoding":{
    "x":{"field":"Mobility", "type":"quantitative", "bin":True, "axis":{"title":"Mobility Score"}},
    "y":{"aggregate":"count","type":"quantitative", "axis":{"title":"Mobility Score Distribution"}}
  }
}

st.vega_lite_chart(spec=spec)

###############################################
#  3. JavaScript in Streamlit (not covered)
###############################################

# We also won't cover JavaScript, but it is also possible to use JavaScript in Streamlit.
# Here are some resources to play around with this on your own if you are interested:
# https://discuss.streamlit.io/t/how-to-embed-javascript-into-streamlit/20152/3
# https://discuss.streamlit.io/t/how-to-run-a-javascript-code-in-streamlit/51556

# We won't be covering this in this class however.

###############################################
#  4. Altair in Streamlit
###############################################

# We will spend most of our focus will be on 

import altair as alt




# ****HERE****
# from vega_datasets import data
 

# source = data.seattle_weather()

# scale = alt.Scale(
#     domain=["sun", "fog", "drizzle", "rain", "snow"],
#     range=["#e7ba52", "#a7a7a7", "#aec7e8", "#1f77b4", "#9467bd"],
# )
# color = alt.Color("weather:N", scale=scale)

# # We create two selections:
# # - a brush that is active on the top panel
# # - a multi-click that is active on the bottom panel
# brush = alt.selection_interval(encodings=["x"])
# click = alt.selection_point(encodings=["color"])

# # Top panel is scatter plot of temperature vs time
# points = (
#     alt.Chart()
#     .mark_point()
#     .encode(
#         alt.X("monthdate(date):T", title="Date"),
#         alt.Y(
#             "temp_max:Q",
#             title="Maximum Daily Temperature (C)",
#             scale=alt.Scale(domain=[-5, 40]),
#         ),
#         color=alt.condition(brush, color, alt.value("lightgray")),
#         size=alt.Size("precipitation:Q", scale=alt.Scale(range=[5, 200])),
#     )
#     .properties(width=550, height=300)
#     .add_params(brush)
#     .transform_filter(click)
# )

# # Bottom panel is a bar chart of weather type
# bars = (
#     alt.Chart()
#     .mark_bar()
#     .encode(
#         x="count()",
#         y="weather:N",
#         color=alt.condition(click, color, alt.value("lightgray")),
#     )
#     .transform_filter(brush)
#     .properties(
#         width=550,
#     )
#     .add_params(click)
# )

# chart = alt.vconcat(points, bars, data=source, title="Seattle Weather: 2012-2015")

# tab1, tab2 = st.tabs(["Streamlit theme (default)", "Altair native theme"])

# with tab1:
#     st.altair_chart(chart, theme="streamlit", use_container_width=True)
# with tab2:
#     st.altair_chart(chart, theme=None, use_container_width=True)