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