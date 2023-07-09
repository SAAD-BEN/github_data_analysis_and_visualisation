# define funcltions to plot graphs with seaborn with professional style

import seaborn as sns
import matplotlib.pyplot as plt

# set seaborn style
sns.set(style="whitegrid", palette="muted", color_codes=True)

# set seaborn style
sns.set(style="whitegrid", palette="muted", color_codes=True)


def plot_barplot(data, x, y, hue, title, xlabel, ylabel):
    # plot the barplot
    ax = sns.barplot(x=x, y=y, hue=hue, data=data)
    # set title
    ax.set_title(title)
    # set x axis label
    ax.set_xlabel(xlabel)
    # set y axis lab
    ax.set_ylabel(ylabel)
    # show the values on the top of the bars
    for p in ax.patches:
        height = p.get_height()
        ax.text(p.get_x()+p.get_width()/2., height + 0.1, '{:1.2f}'.format(height), ha="center")
    # rotate the x axis labels
    plt.xticks(rotation=45)
    # show the plot
    plt.show()



# export the functions
__all__ = ['plot_barplot']