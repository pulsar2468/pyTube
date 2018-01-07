from collections import Counter
import pygal


def labeling(fr):
    return [i[1] for i in fr]  # I get only nameCategory


def compact_data(fr,CategoryId):
    alignment=[]
    for i in CategoryId:
        wall=True
        for j in fr.items():
            if j[0] == i[1]:
                alignment.append(j[1])
                wall=False
                break
        if wall:
            alignment.append(0)
    n_cat = sum(alignment)
    normalized = [i / n_cat for i in alignment]
    return normalized


def start_radar(videos_info, user,CategoryYoutube):

    from pygal.style import Style
    custom_style = Style(
    background='black',
    plot_background='black',
    foreground='#53E89B',
    foreground_strong='#53A0E8',
    foreground_subtle='#630C0D',
    opacity='.6',
    opacity_hover='.9',
    label_font_size=7,
    transition='400ms ease-in',
    colors=('#E853A0', '#E8537A', '#E95355', '#E87653', '#E89B53'))

    #from test_area import CategoryYoutube
    label = labeling(CategoryYoutube)  # Category=IdCategory,nameCategory
    normalized1 = compact_data(videos_info,CategoryYoutube)
    # normalized2=compact_data(fr1)
    # fr=Counter(i[3] for i in a)
    radar_chart = pygal.Radar(show_legend=True, fill=True,style=custom_style)
    radar_chart.x_labels = label
    radar_chart.add('user1', normalized1)
    # radar_chart.add('user2', normalized2)
    radar_chart.render_to_file(user + '.svg')
    return 1
