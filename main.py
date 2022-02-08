import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression

height = [[143], [158], [159], [164], [166], [180], [190]]  # Sets training data
shoe_size = [[3.5], [4], [5], [6.5], [7], [9], [10]]  # Sets the training data

model = LinearRegression()  # Creates the model
model.fit(X=height, y=shoe_size)  # Trains the model

plt.title("Height and Shoe Size Correlation")  # Sets the graph title
plt.xlabel("Height in Centimeters")  # Sets the graph x-axis label
plt.ylabel("Shoe Size")  # Sets the graph y-axis label

plt.plot(height, shoe_size, "k.")  # Plots the training data
plt.plot(height, model.predict(height), color="r")  # Plots the predicted data
plt.axis([100, 200, 0, 15])  # Sets the axis

plt.grid(True)  # Turns on the grid
plt.show()  # Shows the graph

prediction = pd.DataFrame({  # Creates a DataFrame
    "height": [170, 151, 200, 169, 179],
    "shoe_size": [0, 0, 0, 0, 0]
})

for i in prediction.index:  # Loops through the DataFrame
    h = prediction.loc[i, "height"]  # Gets the height from the row
    s = round(model.predict([[h]])[0][0], 1)  # Predicts the height
    prediction.loc[i, "shoe_size"] = s  # Sets the height in the DataFrame

print(prediction.to_string())  # Prints the DataFrame
