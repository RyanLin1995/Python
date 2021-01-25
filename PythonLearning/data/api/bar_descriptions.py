import pygal
from pygal.style import LightColorizedStyle as LCS, LightStyle as LS

my_style = LS(base=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)

chart.title = 'Python Projects'
chart.x_labels = ['httpie', 'django', 'flask']

polt_dicts = [
    {"value": 16101, 'label': 'Description of httpie.'},
    {"value": 15028, 'label': 'Description of django.'},
    {"value": 14798, 'label': 'Description of flask.'}
]
chart.add('', polt_dicts)
chart.render_to_file('bar_descriptions.svg')
chart.render_in_browser()