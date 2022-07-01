# Machine Learning Engineer with Azure - Capstone Project

This project aimed to detect fraudulent credit card transactions using machine learning. To solve this problem, and combine the learning from the previous two projects from the nanodegree, both Azure's AutoML and HyperDrive functions were utilised to produce machine learning solutions for this tasks. The best model was then deployed using an azure container instance, where sample data could be fed to and a response on new data could be retrieved. 

## Project Set Up and Installation
*OPTIONAL:* If your project has any special installation steps, this is where you should put it. To turn this project into a professional portfolio project, you are encouraged to explain how to set up this project in AzureML.

## Dataset

### Overview
The data used for this task from obtained from Kaggle [here.](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud?resource=download) The dataset contains transactions made by credit cards in September 2013 by European cardholders. This dataset presents transactions that occurred in two days, where we have 492 frauds out of 284,807 transactions. The dataset is highly unbalanced, the positive class (frauds) account for 0.172% of all transactions. It contains only numerical input variables which are the result of a PCA transformation.

### Task
The use case for this dataset is to determine if a credit card tranaction is deliberate by the customer, or wether it is fraudulent. As the dataset contains information that has been transformed through the use of PCA, the labels are named V1 through 28. The only features which have not been transformed with PCA are 'Time' and 'Amount'. Feature 'Time' contains the seconds elapsed between each transaction and the first transaction in the dataset. The feature 'Amount' is the transaction Amount, this feature can be used for example-dependant cost-sensitive learning. Feature 'Class' is the response variable and it takes value 1 in case of fraud and 0 otherwise.

### Access
The  dataset was downloaded and registered as a dataset in the Azure workspace using the Azure ML Studio GUI. Once uploaded to the 'datasets' section it can utilised within the SDK.

## Automated ML
For the AutoML run, the experiment run time was limited to 20 minutes, as with 5 maximum concurrent runs, this should allow the run to obtain a sifficiently accurate model, before plateuing and potentially hitting a session time out. The primary metric chosen for the autoML run to focus on was weighted AUC (area under the curve). This metric is a recommended evaluation metric where the data is imbalanced within classification tasks, as it accounts for precision and recall of both classes and allows accurate characterisation of the performance of a model.

### Results
1. AUC - 0.99
2. Model Type - Voting Ensemble
3. Improvements - Since the model runs were dealing with a dataset with class imbalance then an approach to improve model output would usually involve balancing the class either by oversampling or under sampling or create synthetic samples of the minority class using the SMOTE algorithm. Once this is done then the usual Area under curve of ROC can be looked at.

Run Details:
![Run details](https://user-images.githubusercontent.com/56005109/176929906-1e2442ab-b752-4d9a-b59a-1aaadbd9a2cd.PNG)

Best Model:
![Best model parameters](https://user-images.githubusercontent.com/56005109/176930227-c482910e-9497-4d5e-b887-3a10c9c331bf.PNG)

## Hyperparameter Tuning
The model chosen for the HyperDrive run was a random forest classifer. RF are versatile ensemble algorithm that is an extension of bagging that also randomly selects subsets of features used in each data sample. Random forests have proven effective on a wide range of different predictive modeling problems. 

Model hyper parameters:
1. n_estimators(trees in the forest): 10 - 200.
2. maximum depth: 10 - 100

The ranges chosen for each hyper parameter was determined to provide a sufficient choice for the random parameter sampling method that was implemented within the hyper drive configuration, while keeping training time fairly short so not to hit a session timeout. The Median Stopping policy was chosen for this tasks. This computes running averages across all runs and cancels runs whose best performance is worse than the median of the running averages. Specifically, a run will be canceled at interval N if its best primary metric reported up to interval N is worse than the median of the running averages for intervals 1:N across all runs.

### Results
1. AUC - 0.984
2. Parameters - {"--max_depth": 78.0, "--n_estimators": 187.0}
3. Improvements - Again, random forest is very effective on a wide range of problems, but like bagging algorithms, performance of the standard algorithm is not great on imbalanced classification problems. One method to improve the algorithms performance could be to change the weight that each class has when calculating the “impurity” score of a chosen split point (This modification of random forest is referred to as Weighted Random Forest).

Run Details:
![RunDetails2](https://user-images.githubusercontent.com/56005109/176933458-fa484a5b-5e34-4ecf-9043-916b1e07be4c.PNG)

Best Model:
![HyperDriveBestModel](https://user-images.githubusercontent.com/56005109/176933616-c70bbc29-3060-46da-9cff-3383902356de.PNG)

## Model Deployment
The automl model was deployed as an Azure Container Instance and was queried using searlised JSON data that was sent to the model's endpoint as an http request. The "Model Deployment" section of the automl.ipynb notebook highlights all the neccessary steps to deploy and query the deployed model with a random sample of data. The score.py file, which receives and unpacks the data submitted as JSON, is used to confirgure the inference of the model endpoint. The data is then converted into a Pandas dataframe, NaN values are dropped, and the model is applied to generate predictions.

Deployed Model Status:
![DeploymentSuccess](https://user-images.githubusercontent.com/56005109/176935117-5fba4072-52aa-4781-aed9-44f40170bff9.PNG)

Random Data Sample:
![SampleDataInput](https://user-images.githubusercontent.com/56005109/176937363-d2da12df-41e4-4305-9249-1a940ff6579c.PNG)

Endpoint Result:

![QueryResult](https://user-images.githubusercontent.com/56005109/176937436-1acc527c-bccd-43dc-baf0-d2da01149c56.PNG)

## Screen Recording
A link to a video outlining the deployed AutoML model can be viwed [here](https://youtu.be/ixpc4gPBwww).
