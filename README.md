# Lab 10 – AI-Powered Water Quality Visualization Using Python and Streamlit

---

## Names of People Involved (Group Members)
Faith Cox

---

## Date Work Was Submitted
4/4/25


## Introduction:
In this lab, we used Python, pandas, matplotlib, and Streamlit to analyze water quality data. By
leveraging large language model (LLM) AI tools, we generated Python functions to filter and
visualize data for contaminants such as Escherichia coli, turbidity, and pH. We also built a full web
application that allows users to explore and visualize data interactively.

## Methods/Tests
The core functionality was built using Python and the Streamlit framework. Data was loaded from two `.csv` files (`station.csv` and `narrowresult.csv`) which were uploaded directly by the user in the app interface. One file contained station metadata, while the other contained contaminant test results.

Key steps included:

- Using `pandas` for data filtering and cleaning  
- Generating time-series plots with `matplotlib`  
- Creating interactive maps with `folium`  
- Building a front-end interface with Streamlit, allowing users to:
  - Upload files
  - Select one contaminant to analyze
  - Define a numeric range and a date range
  - View stations with filtered results on a map
  - View a trend graph of measurements by site over time

The AI model **ChatGPT-4** was used to generate all Python code and Streamlit logic in an iterative, step-by-step format to meet all design requirements. Prompts were documented and formatted for reproducibility in the Results section.

---

## Results




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

[Deployed Streamlit App](https://organic-zebra-696gx7gjg492r5w9-8501.app.github.dev/)

[GitHub Repository with Full Code]()

## Discussion

The data visualizations provided by the application reveal clear differences in contaminant levels between monitoring stations and over time. Trends like spikes in E. coli levels or variations in turbidity and pH can be identified quickly using the visual tools.

This project also demonstrates the ability of generative AI to effectively scaffold software tools by interpreting human instructions. The code generated was both functional and adaptable, requiring only minor debugging. Additionally, working with live data sets emphasized the importance of data cleaning and handling missing values, as many rows contained NaNs or inconsistent entries.

By filtering and mapping contaminants, the application provides a valuable interface for environmental scientists or decision-makers who need to quickly assess water quality conditions across large spatial regions.

---


## Conclusion:
This lab demonstrated how LLM-based prompt engineering can streamline data science tasks such as cleaning, visualization, and app development. The use of AI to generate code allowed for faster and more structured analysis, culminating in a working Streamlit app that enables dynamic exploration of water quality datasets. The final tool is a powerful foundation for future environmental monitoring apps or dashboards.

---

## References

[1] Streamlit. (n.d.). *Streamlit – Turn data scripts into shareable web apps in minutes*. Retrieved from https://streamlit.io/

[2] Python Software Foundation. (2024). *Python Language Reference, version 3.x*. Retrieved from https://www.python.org/

[3] pandas development team. (2024). *pandas: powerful Python data analysis toolkit*. https://pandas.pydata.org/

[4] Hunter, J. D. (2007). *Matplotlib: A 2D graphics environment*. Computing in Science & Engineering, 9(3), 90-95. https://doi.org/10.1109/MCSE.2007.55

[5] Python Folium Developers. (n.d.). *Folium – Python Data, Leaflet.js Maps*. Retrieved from https://python-visualization.github.io/folium/

[6] OpenAI. (2024). *ChatGPT-4 Model*. Accessed via https://chat.openai.com

[7] U.S. Geological Survey (USGS). (n.d.). *Water Quality Data*. Retrieved from https://www.usgs.gov/mission-areas/water-resources

[8] Water Quality Portal. (n.d.). *National Water Quality Monitoring Council*. Retrieved from https://www.waterqualitydata.us/

  
