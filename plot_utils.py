import seaborn as sns
import matplotlib.pyplot as plt
from bokeh.plotting import figure, show
from bokeh.models import HoverTool

# set seaborn style
sns.set(style="whitegrid", palette="muted", color_codes=True)

# define function to plot barplot
def plot_barplot(data, x, y, hue, title, xlabel, ylabel):
    # plot the barplot
    ax = sns.barplot(x=x, y=y, hue=hue, data=data)
    # set title
    ax.set_title(title)
    # set x axis label
    ax.set_xlabel(xlabel)
    # set y axis lab
    ax.set_ylabel(ylabel)
    # rotate the x axis labels
    plt.xticks(rotation=45)
    # show the plot
    plt.show()

# define function to plot pie chart
def plot_piechart(data, x, title):
    # plot the pie chart
    ax = sns.countplot(x=x, data=data)
    # set title
    ax.set_title(title)
    # rotate the x axis labels
    plt.xticks(rotation=45)
    # show the plot
    plt.show()

# define function to plot points graph
def draw_points_graph(x, y, average=True, title="Graph"):
    if average:
        x = x.groupby(x.index // 1000).mean()
        y = y.groupby(y.index // 1000).mean()

    # create a new plot with a specific size
    p = figure(sizing_mode="stretch_width", max_width=500, height=250, title=title)

    # add a circle renderer
    circle = p.circle(x, y, fill_color="red", size=4)

    # define the hover tool
    hover = HoverTool(tooltips=[("Forks", "@x"), ("Stars", "@y")], renderers=[circle])

    # add the hover tool to the plot
    p.add_tools(hover)

    # show the plot
    show(p)

# export the functions
__all__ = ['plot_barplot', 'plot_piechart', 'draw_points_graph']
