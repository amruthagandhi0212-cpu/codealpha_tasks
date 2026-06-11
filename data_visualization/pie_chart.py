import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_excel("students.csv.xlsx")

# Convert Marks column to numbers
df["Marks"] = pd.to_numeric(df["Marks"], errors="coerce")

# Remove empty values if any
df = df.dropna(subset=["Marks"])

# Create Pie Chart
plt.figure(figsize=(8, 8))

plt.pie(
    df["Marks"],
    labels=df["Student"],
    autopct="%1.1f%%"
)

plt.title("Marks Distribution Among Students")

# Save chart
plt.savefig("pie_chart.png")

# Display chart
plt.show()

print("Pie chart created successfully!")