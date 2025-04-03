import pandas as pd
import matplotlib.pyplot as plt

# Load your data (make sure narrowresult.csv is in the same folder)
df = pd.read_csv("narrowresult.csv")

# Filter for Escherichia coli only
ecoli_df = df[df["CharacteristicName"] == "Escherichia coli"].copy()

# Clean and convert columns
ecoli_df["ActivityStartDate"] = pd.to_datetime(ecoli_df["ActivityStartDate"], errors="coerce")
ecoli_df["ResultMeasureValue"] = pd.to_numeric(ecoli_df["ResultMeasureValue"], errors="coerce")

# Drop rows with missing values
ecoli_df.dropna(subset=["ActivityStartDate", "ResultMeasureValue"], inplace=True)

# Plot
plt.figure(figsize=(12, 6))
for station_id, group in ecoli_df.groupby("MonitoringLocationIdentifier"):
    plt.plot(group["ActivityStartDate"], group["ResultMeasureValue"], label=station_id)

plt.title("Escherichia coli Levels Over Time by Station")
plt.xlabel("Date")
plt.ylabel("E. coli Level")
plt.legend(fontsize="x-small", bbox_to_anchor=(1.01, 1), loc="upper left")
plt.grid(True)
plt.tight_layout()

# Save or show the plot
plt.savefig("ecoli_trend_plot.png")
plt.show()
