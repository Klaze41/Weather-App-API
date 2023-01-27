from django.test import TestCase

from flask import Flask, render_template
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

app = Flask(__name__)

@app.route('/')
def candlestick_chart():
    # Load the market data into a Pandas DataFrame
    df = pd.read_csv('market_data.csv')

    # Create the candlestick chart using Seaborn
    sns.set_style("darkgrid")
    plt.figure(figsize=(10,5))
    sns.lineplot(x="Date", y="Open", data=df, color='blue')
    sns.lineplot(x="Date", y="Close", data=df, color='red')
    sns.lineplot(x="Date", y="High", data=df, color='green')
    sns.lineplot(x="Date", y="Low", data=df, color='black')
    plt.title("Candlestick Chart")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.xticks(rotation=90)

    # Save the chart to a file
    plt.savefig('candlestick_chart.png')

    # Render the chart in the template
    return render_template('candlestick_chart.html')

if __name__ == '__main__':
    app.run()
