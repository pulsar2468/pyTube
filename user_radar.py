from collections import Counter
import pygal

def labeling(fr):
    return [i[0] for i in fr.items()]


def compact_data(fr):
    data=[i[1] for i in fr.items()]
    n_cat=sum(data)
    normalized=[i/n_cat for i in data]
    return normalized


fr=Counter({'Gaming': 1350, 'Education': 820, 'Science & Technology': 697, 'Music': 544, 'Entertainment': 388, 'Comedy': 304, 'People & Blogs': 212, 'Film & Animation': 196, 'Pets & Animals': 143, 'News & Politics': 123, 'Howto & Style': 49, 'Nonprofits & Activism': 44, 'Travel & Events': 31, 'Shows': 12, 'Autos & Vehicles': 10, 'Sports': 6})
fr1=Counter({'Music': 632, 'Gaming': 273, 'Entertainment': 147, 'Comedy': 115, 'People & Blogs': 76, 'Science & Technology': 31, 'Education': 24, 'Howto & Style': 23, 'Film & Animation': 15, 'News & Politics': 4, 'Autos & Vehicles': 4, 'Shows': 3, 'Nonprofits & Activism': 2, 'Travel & Events': 1})
label=labeling(fr)
normalized1=compact_data(fr)
normalized2=compact_data(fr1)
#fr=Counter(i[3] for i in a)
radar_chart = pygal.Radar(show_legend=True,fill=True)
radar_chart.x_labels = label
radar_chart.add('user1', normalized1)
radar_chart.add('user2', normalized2)

radar_chart.render_to_file('radar_chart.svg')