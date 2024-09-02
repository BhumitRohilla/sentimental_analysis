import pandas as pd
import json
from matplotlib import pyplot
from scipy import stats
from datetime import datetime

def legend(pct, allvalues):
    absolute = int(pct / 100.*sum(allvalues))
    return f'{absolute} ({pct:.1f}%)'

    
if __name__ == '__main__':
    result = []
    with open('analysisResult/finalData.json') as file:
        result = json.load(file)

    positive_threshold = 0.1
    negative_threshold = -0.1

    positive_count = 0
    negative_count = 0
    neutral_count = 0

    for element in result:
        compound_score = element['compound']
        if compound_score >= positive_threshold:
            positive_count += 1
        elif compound_score <= negative_threshold:
            negative_count += 1
        else:
            neutral_count += 1

    labels = ['Positive', 'Negative', 'Neutral']
    sizes = [positive_count, negative_count, neutral_count]
    colors = ['#ff9999','#66b3ff','#99ff99']

    fig, ax = pyplot.subplots()
    ax.pie(sizes, labels=labels, colors=colors, autopct=lambda pct: legend(pct, sizes), startangle=140)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    # Save the pie chart to a PDF file
    pyplot.savefig('sentiment_distribution_pie_chart.pdf', format='pdf')


    my_dict = {}

    
    for element in result:
        print(element["date"])
        date_obj = datetime.strptime(element["date"], "%a %b %d %H:%M:%S %z %Y")
        formatted_date = date_obj.strftime("%Y-%m-%d")
        my_dict.setdefault(formatted_date, {
            "neutral": 0,
            "positive": 0,
            "negative": 0,
        })
        compound_score = element['compound']
        if compound_score >= positive_threshold:
            my_dict[formatted_date]["positive"] += 1
        elif compound_score <= negative_threshold:
            my_dict[formatted_date]["negative"] += 1
        else:
            my_dict[formatted_date]["neutral"] += 1


    rows = []


    for key in my_dict:
        value = my_dict[key]
        rows.append({
            "date": key,
            "neutral": value["neutral"],
            "positive": value["positive"],
            "negative": value["negative"]
        })


    date_data_frame = pd.DataFrame(rows)
    date_data_frame['date'] = pd.to_datetime(date_data_frame['date'])
    date_data_frame = date_data_frame.sort_values(by='date')

    date_range = pd.date_range(start=date_data_frame['date'].min(), end=date_data_frame['date'].max(), freq='D')

    date_data_frame = date_data_frame.set_index('date').reindex(date_range).fillna(0).reset_index()

    date_data_frame.rename(columns={'index': 'date'}, inplace=True)
    # Display the DataFrame
    print(date_data_frame)

    pyplot.figure(figsize=(20, 6))
    pyplot.scatter(date_data_frame['date'], date_data_frame['neutral'], label='Neutral', marker='o')
    pyplot.scatter(date_data_frame['date'], date_data_frame['positive'], label='Positive', marker='o')
    pyplot.scatter(date_data_frame['date'], date_data_frame['negative'], label='Negative', marker='o')

    pyplot.xlabel('Date')
    pyplot.ylabel('Count')
    pyplot.title('Sentiment Counts Over Time')
    pyplot.legend()
    pyplot.grid(True)

    # Save the plot to a PDF file
    pyplot.savefig('sentiment_trends_line_graph.pdf', format='pdf')

    pyplot.show()