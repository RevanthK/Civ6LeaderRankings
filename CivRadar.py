import matplotlib.pyplot as plt
import pandas as pd
from math import pi
from matplotlib.lines import Line2D

RED = (0.984313725490196, 0.5019607843137255, 0.4470588235294118, 1.0)
BLUE = (0.5019607843137255, 0.6941176470588235, 0.8274509803921568, 1.0)
TEAL = (0.5529411764705883, 0.8274509803921568, 0.7803921568627451, 1.0)
GREEN = (0.7019607843137254, 0.8705882352941177, 0.4117647058823529, 1.0)
YELLOW = (1.0, 0.9294117647058824, 0.43529411764705883, 1.0)
ORANGE = (0.9921568627450981, 0.7058823529411765, 0.3843137254901961, 1.0)


CivData = pd.read_csv("CivLeaderData.csv") 
categories = list(CivData.columns[2:7])
Civdict = {}
Civdict['Civ\'s'] = list(CivData.iloc[:, 0])

for i in range(0,len(categories)):	
	Civdict[str(categories[i])] = list(CivData.loc[:,categories[i]])

Leaders = list(CivData.iloc[:, 1])
Tier = list(CivData.iloc[:, 10])

df = pd.DataFrame(Civdict)


# ------- PART 1: Define a function that do a plot for one line of the dataset!
 
def make_spider(row, title, color):
 
	# number of variable
	categories=list(df)[1:]
	N = len(categories)
	 
	# What will be the angle of each axis in the plot? (we divide the plot / number of variable)
	angles = [n / float(N) * 2 * pi for n in range(N)]
	angles += angles[:1]
	 
	# Initialise the spider plot
	ax = plt.subplot(6,8,row+1, polar=True, )
	plt.subplots_adjust(wspace=1, hspace=0)
	 
	# If you want the first axis to be on top:
	ax.set_theta_offset(pi / 2)
	ax.set_theta_direction(-1)
	 
	# Draw one axe per variable + add labels labels yet
	plt.xticks(angles[:-1], categories, color='grey', size=8, fontsize='x-small')
	 
	# Draw ylabels
	ax.set_rlabel_position(50)
	plt.yticks([1,3,5], ["1","3","5"], color="grey", size=5)
	plt.ylim(0,5)
	 
	# Ind1
	values=df.loc[row].drop('Civ\'s').values.flatten().tolist()
	values += values[:1]
	ax.plot(angles, values, color=color, linewidth=2, linestyle='solid')
	ax.fill(angles, values, color=color, alpha=0.4)
	 
	# Add a title
	plt.title(title, size=11, color=color, y=1.25)
 
# ------- PART 2: Apply to all individuals
# initialize the figure
my_dpi=250
plt.figure(figsize=(5000/my_dpi, 5000/my_dpi), dpi=my_dpi)
 
# Create a color palette:
my_palette = plt.cm.get_cmap("Set3", len(df.index))
plt.title("Ranking Civ 6 Leaders based on Victory Strength", size=25, color="grey", y=1.25)

# Loop to plot
for row in range(0, len(df.index)):
	Color = RED #Red
	if Tier[row] == 'S':
		Color = BLUE #Blue
	if Tier[row] == 'A':
		Color = TEAL #Teal
	if Tier[row] == 'B':
		Color = GREEN #Green
	if Tier[row] == 'C':
		Color =  YELLOW #Yellow
	if Tier[row] == 'D':
		Color = ORANGE #Orange

	# make_spider(row=row, title= str(row+1) + '. ' + df['Civ\'s'][row] + "\n" + Leaders[row], color=Color)
	make_spider(row=row, title= str(row + 1) + '. ' + df['Civ\'s'][row] + "\n" + Leaders[row], color=Color)
# plt.show()

# plt.text(200,150,"Civ 6 Rankings based on Victory Strength's")

legend_elements = [Line2D([0], [0], color=BLUE, lw=4, label='S'),
					Line2D([0], [0], color=TEAL, lw=4, label='A'),
					Line2D([0], [0], color=GREEN, lw=4, label='B'),
					Line2D([0], [0], color=YELLOW, lw=4, label='C'),
					Line2D([0], [0], color=ORANGE, lw=4, label='D'),
					Line2D([0], [0], color=RED, lw=4, label='F'),]

plt.legend(handles=legend_elements, title = "Class", bbox_to_anchor=(3, 0), loc='lower right', borderaxespad=0.)
plt.savefig('Civ_Ratings.png')