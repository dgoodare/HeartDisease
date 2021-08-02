import matplotlib.pyplot as plt
from IPython.display import display
import pandas as pd
import seaborn as sns

data = pd.read_csv('heart.csv', header=None)

#remove the first row as it is just the label names
data = data.iloc[1:]

data.columns = ['age', 'sex', 'cp', 'trestbps', 'chol',
              'fbs', 'restecg', 'thalach', 'exang', 
              'oldpeak', 'slope', 'ca', 'thal', 'target']

#print the first 5 samples
display("First 5 samples in data: \n", data.head())

#check for null values
print("Checking for null values... \n", data.isnull().sum())

#Map sex to text values (0 = Female, 1 = Male)
#data['sex'] = data.sex.map({0: 'female', 1: 'male'})

#########################
######Data Analysis######
#########################
#distribution of age vs target
sns.catplot(kind='count', data=data, x='age', hue='target', order=data['age'].sort_values().unique())
plt.title("Variation of age for each target class")
plt.show()

#distribution of age vs sex
"""
COME BACK TO THIS
sns.catplot(kind = 'bar', data = data, y = 'age', x = 'sex', hue = 'target')
plt.title('Distribution of age vs sex with the target class')
plt.show()
"""

#########################
########## SVM ##########
#########################
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import classification_report, confusion_matrix

#split the data in 80/20 ratio
x_train, x_test, y_train, y_test = train_test_split(data, data.target, test_size=0.2, random_state=100)

print("X shape: ", x_train.shape)
print("Y shape: ", y_train.shape)

#create classifier for svm
classifier = svm.SVC(kernel='sigmoid')

#train the model using the training set
classifier = classifier.fit(x_train, y_train)

#make predictions using the test set
predictions = classifier.predict(x_test)

#create confusion matrix to compare the model's predictions with the actual results
confMatrix = confusion_matrix(y_test, predictions)
sns.heatmap(confMatrix, annot=True)
plt.title("Confusion Matrix comparing predictions with actual results")
plt.show()

#show classifcation report
print(classification_report(y_test, predictions))

"""
Having tried several different kernal functions (RBF, polynomial, linear and sigmoid), I have found the linear function
to be vastly superior to the others, as the model is able to predict the results with 100% accuracy!
"""