from preswald import text, plotly, connect, get_df, table, query, slider, sidebar, topbar, playground
import pandas as pd
import plotly.express as px


connect() 
df = get_df('health_activity_data')

sql = "SELECT * FROM health_activity_data WHERE Age > 50"
filtered_df = query(sql, "health_activity_data")



text("Table containing health information about individuals who are over 50")
table(filtered_df, title="Filtered Data")


text("Select a threshold value for heart rate")
threshold = slider("Threshold", min_val=0, max_val=200, default=70)
table(filtered_df[filtered_df["Heart_Rate"] > threshold], title="Dynamic Data View")



text("Scatter plot of Calories Consumed vs Blood Pressure")
fig = px.scatter(filtered_df, x="Calories_Intake", y="Blood_Pressure", title = "Scatter plot of Calories Consumed vs Blood Pressure",
labels = {"Calories_Intake": "Calories Consumed Per Day", "Blood_Pressure":"Blood_Pressure"}, color = "Gender"
)
plotly(fig)


playground(
    label="User Age Filter", 
    query="SELECT Age, Height_cm FROM health_activity_data WHERE Age > 45"
)