from bokeh.plotting import figure, output_file, show
import pandas

# Read in csv
df = pandas.read_csv('weather.csv')

month = df['month']
rain = df['rainfall']
sun = df['sunshine']
temp = df['temperature']

# x = [1, 2, 3, 4, 5]
# y = [4, 6, 2, 4, 3]

output_file('index.html')

# Add plot
p = figure(
    y_range=month,
    width=800,
    height=600,
    title='Weather in Sheffield',
    x_axis_label='Sunshine',
    tools=''
)

# Render glyph
p.hbar(
    y=month,
    right=sun,
    left=0,
    height=0.4,
    color='orange',
    fill_alpha=0.5
)

# Show results
show(p)