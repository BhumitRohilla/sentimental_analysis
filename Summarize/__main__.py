import numpy
import json
from matplotlib import pyplot
from scipy import stats


def calculate_statistics(scores):
    mean = numpy.mean(scores)
    median = numpy.median(scores)
    mode = stats.mode(scores, keepdims=False)[0]
    return mean, median, mode


def summarize(anaResult):
    compoundScore = []
    positiveScore = []
    neutralScore  = []
    negativeScore = []
    for singleAna in anaResult:
        compoundScore.append(singleAna['compound'])
        positiveScore.append(singleAna['positive'])
        neutralScore.append(singleAna['neutral'])
        negativeScore.append(singleAna['negative'])

    mean_compound, median_compound, mode_compound = calculate_statistics(compoundScore)
    print(f"Compound Scores - Mean: {mean_compound}, Median: {median_compound}, Mode: {mode_compound}")

    # Positive Scores
    mean_positive, median_positive, mode_positive = calculate_statistics(positiveScore)
    print(f"Positive Scores - Mean: {mean_positive}, Median: {median_positive}, Mode: {mode_positive}")

    # Neutral Scores
    mean_neutral, median_neutral, mode_neutral = calculate_statistics(neutralScore)
    print(f"Neutral Scores - Mean: {mean_neutral}, Median: {median_neutral}, Mode: {mode_neutral}")

    # Negative Scores
    mean_negative, median_negative, mode_negative = calculate_statistics(negativeScore)
    print(f"Negative Scores - Mean: {mean_negative}, Median: {median_negative}, Mode: {mode_negative}")

    # Plotting
    labels = ['Compound', 'Positive', 'Neutral', 'Negative']
    means = [mean_compound, mean_positive, mean_neutral, mean_negative]
    medians = [median_compound, median_positive, median_neutral, median_negative]
    modes = [mode_compound, mode_positive, mode_neutral, mode_negative]
        
    x = numpy.arange(len(labels))
    width = 0.25

    fig, ax = pyplot.subplots()
    bars1 = ax.bar(x - width, means, width, label='Mean')
    bars2 = ax.bar(x, medians, width, label='Median')
    bars3 = ax.bar(x + width, modes, width, label='Mode')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_xlabel('Sentiment Scores')
    ax.set_title('Sentiment Score Statistics')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    fig.tight_layout()
    return pyplot
    
if __name__ == '__main__':
    result = []
    with open('analysis/everton_tweets.json') as file:
        result = json.load(file)
    plot = summarize(result)
    plot.savefig('summary.pdf', format='pdf')