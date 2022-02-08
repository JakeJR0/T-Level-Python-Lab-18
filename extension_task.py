import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

plt.title("Height and Weight Correlation")  # Sets the title
plt.xlabel("Weight in Kilograms")  # Sets the x-axis label
plt.ylabel("Height in Centimetres")  # Sets the y-axis label

height = [[159], [164], [169], [173], [179]]  # sets the training data
weight = [[59], [66], [72.2], [75], [80]]  # sets the training data

model = LinearRegression()  # Creates the model
model.fit(X=height, y=weight)  # Trains the model

plt.plot(height, weight, "k.")  # Plots training data
plt.plot(height, model.predict(height), color="r")  # Plots Prediction

plt.grid(True)  # Shows the Grid
plt.show()  # Displays the graph
