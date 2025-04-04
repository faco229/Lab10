# Lab10



Introduction:
In this lab, we used Python, pandas, matplotlib, and Streamlit to analyze water quality data. By
leveraging large language model (LLM) AI tools, we generated Python functions to filter and
visualize data for contaminants such as Escherichia coli, turbidity, and pH. We also built a full web
application that allows users to explore and visualize data interactively.


results

Part 1 - Map it
Goal:
Extract unique station names and locations from the station.csv database using Python and display
them on an interactive map.
Model:
ChatGPT-4
Prompt:
Write Python code to read a CSV file containing water quality monitoring stations using pandas, and
extract a list of unique station identifiers and their names. Drop any duplicates and prepare the data
for mapping.
Part 1 - Map it
Goal:
Create a map using Folium that shows the location of each monitoring station from the dataset.
Model:
ChatGPT-4
Prompt:
Write Python code to create an interactive map of water monitoring stations using folium. Assume
the stations have dummy latitude and longitude values generated within Kentucky. Add a marker for
each unique station with a popup label showing the station name.
Part 2 - What's Normal
Goal:
Filter for one water quality characteristic and plot the results over time for each site using different
colored lines.
Model:
ChatGPT-4
Prompt:
Write Python code using pandas and matplotlib to:
- Load a CSV of water quality data
- Filter for a single contaminant (e.g., Escherichia coli)
- Convert the date column to datetime format
- Plot the contaminant values over time, using one line per station
Part 2 - What's Normal
Goal:
Modify the plotting function to support two characteristics at once, each displayed in its own subplot.
Model:
ChatGPT-4
Prompt:
Update the existing plot function to support up to two contaminants. Each should have its own
subplot. Use pandas and matplotlib to show trends over time per station for each contaminant.
Part 2 - What's Normal
Goal:
Plot two water quality characteristics - Turbidity and pH - over time, averaged across all monitoring
stations.
Model:
ChatGPT-4
Prompt:
Write Python code using pandas and matplotlib to plot two water quality characteristics (Turbidity
and pH) over time on the same chart. Average the values across all stations for each date. Use one
line per characteristic.
Part 3 - Streamlit
Goal:
Create a web app using Streamlit that loads two CSVs, allows the user to select up to two
contaminants, set date and value filters, and displays a map and trend plot.
Model:
ChatGPT-4
Prompt:
Write a Streamlit app that:
- Loads two water quality CSV files
- Lets the user select up to 2 contaminants
- Allows filtering by date range and value range
- Filters the stations based on the selected contaminant(s)
- Displays a map of stations with markers
- Plots the measured contaminant values over time for each station


## 🔹 Part 1 – Mapping Stations

| Goal | Model | Prompt |
|------|--------|--------|
| Extract unique water quality monitoring stations from `station.csv` and display them on an interactive map. | ChatGPT-4 | `Write Python code to read a CSV file containing water quality monitoring stations using pandas, and extract a list of unique station identifiers and their names. Drop any duplicates and prepare the data for mapping.` |
| Create an interactive map using Folium that shows station names and locations from the extracted dataset. | ChatGPT-4 | `Write Python code to create an interactive map of water monitoring stations using folium. Assume the stations have dummy latitude and longitude values generated within Kentucky. Add a marker for each unique station with a popup label showing the station name.` |

---

## 🔹 Part 2 – Plotting Contaminant Trends

| Goal | Model | Prompt |
|------|--------|--------|
| Plot *Escherichia coli* levels over time using one line per monitoring station. | ChatGPT-4 | `Write Python code using pandas and matplotlib to:\n- Load a CSV of water quality data\n- Filter for a single contaminant (e.g., Escherichia coli)\n- Convert the date column to datetime format\n- Plot the contaminant values over time, using one line per station` |
| Modify the previous plot function to allow displaying two different contaminants side-by-side in subplots. | ChatGPT-4 | `Update the existing plot function to support up to two contaminants. Each should have its own subplot. Use pandas and matplotlib to show trends over time per station for each contaminant.` |
| Compare pH and Turbidity by plotting their average values across all stations over time in a single plot. | ChatGPT-4 | `Write Python code using pandas and matplotlib to plot two water quality characteristics (Turbidity and pH) over time on the same chart. Average the values across all stations for each date. Use one line per characteristic.` |

---

## 🔹 Part 3 – Streamlit App

| Goal | Model | Prompt |
|------|--------|--------|
| Build a Streamlit web app that lets users upload both water quality datasets, select a contaminant, filter by date and value range, and display a map and trend graph based on the filtered data. | ChatGPT-4 | `Develop a streamlit app that allows the user to upload both data bases used in part 1 and part 2 (station.csv and narrowresult.csv), to search for a contaminant in the databases. Once the contaminant has been selected, you should be able to define the range of values and dates that you want to show. After modifying the ranges, update the map showing the location of the stations with the contaminant within that range and measured during the time frame. It should also show you a trend over time of the contaminant in all the stations shown.` |





Conclusion:
This lab demonstrated how LLM-based prompt engineering can streamline data science tasks such
as cleaning, visualization, and app development. The use of AI to generate code allowed for faster
and more structured analysis, culminating in a working Streamlit app that enables dynamic
exploration of water quality datasets. The final tool is a powerful foundation for future environmental
monitoring apps or dashboards.


## Links

- [Live Streamlit App](https://organic-zebra-696gx7gjg492r5w9-8501.app.github.dev/)

  
- [View All AI Prompts (RESULTS_PROMPTS.md)](RESULTS_PROMPTS.md)
