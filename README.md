# Social Media Analytics
The Social Media Analytics Dashboard is a data analytics project developed using Python, Pandas, and Matplotlib to analyze social media engagement across different platforms. The dashboard processes data related to likes, comments, and shares, helping users understand audience engagement patterns and identify the best-performing social media platform. Through data visualization and performance metrics, the project provides valuable insights for improving social media marketing strategies and decision-making.

# Key Features
# Data Collection and Processing
  Import social media data from CSV files.
  Clean and organize datasets for analysis.
  Handle missing or inconsistent data.
# Engagement Analysis
  Calculate total likes, comments, and shares.
  Measure overall engagement for each platform.
  Compare engagement metrics across platforms.
# Platform Performance Comparison
  Identify the highest-performing platform.
  Rank platforms based on engagement levels.
  Analyze audience interaction trends.
# Data Visualization
  Interactive bar charts for likes, comments, and shares.
  Pie charts showing engagement distribution.
  Clear graphical representation of social media performance.
#  Dashboard Reporting
  Generate summarized reports.
  Present insights in an easy-to-understand format.
  Support data-driven marketing decisions.
# Performance Insights
  Detect engagement patterns and trends.
  Highlight strengths and weaknesses of each platform.
  Provide recommendations for content strategy improvement.
# Technologies Used
  Python
  Pandas
  Matplotlib
  CSV Dataset
# HOW TO USE CODE
# Create Project Folder
  Social_Media_Analytics
  │
  ├── social_media_data.csv
  ├── analysis.py
# Create CSV File
  Date,Platform,Likes,Comments,Shares
  2026-01-01,Instagram,500,80,40
  2026-01-02,Facebook,300,50,20
  2026-01-03,Twitter,200,30,15
  2026-01-04,Instagram,700,100,60
  2026-01-05,Facebook,450,70,35
  2026-01-06,Twitter,250,40,20
  2026-01-07,Instagram,800,120,70
  2026-01-08,Facebook,600,90,50
  2026-01-09,Twitter,350,45,20
# Create analysis.py
import pandas as pd

df = pd.read_csv("social_media_data.csv")

print(df)
df["Total_Engagement"] = (
    df["Likes"] +
    df["Comments"] +
    df["Shares"]
)

print(df)
summary = df.groupby("Platform")[
    ["Likes","Comments","Shares"]
].sum()

print(summary)
summary["Total"] = summary.sum(axis=1)

print(summary)

best = summary["Total"].idxmax()

print("Best Platform:", best)
import matplotlib.pyplot as plt

summary["Likes"].plot(kind="bar")

plt.title("Likes by Platform")
plt.show()
summary["Total"].plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.title("Engagement Distribution")
plt.ylabel("")
plt.show()
plt.savefig("charts/likes_chart.png")

# OUTPUT
<img width="640" height="480" alt="Figure_2" src="https://github.com/user-attachments/assets/8b3752c3-4f48-416d-ad24-b805d4e7dd10" />

<img width="640" height="480" alt="Figure_1" src="https://github.com/user-attachments/assets/faecc717-c544-4892-a71d-ed642a7171f9" />

<img width="439" height="412" alt="image" src="https://github.com/user-attachments/assets/7b7c6e29-9b00-47fc-bbda-fb83fd29f192" />
