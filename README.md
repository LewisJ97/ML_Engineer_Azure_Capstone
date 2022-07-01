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

*TODO* Remeber to provide screenshots of the `RunDetails` widget as well as a screenshot of the best model trained with it's parameters.
![Run details](https://user-images.githubusercontent.com/56005109/176929906-1e2442ab-b752-4d9a-b59a-1aaadbd9a2cd.PNG)
![Best model parameters]([BestModel1](https://user-images.githubusercontent.com/56005109/176930227-c482910e-9497-4d5e-b887-3a10c9c331bf.PNG)

## Hyperparameter Tuning
*TODO*: What kind of model did you choose for this experiment and why? Give an overview of the types of parameters and their ranges used for the hyperparameter search


### Results
*TODO*: What are the results you got with your model? What were the parameters of the model? How could you have improved it?

*TODO* Remeber to provide screenshots of the `RunDetails` widget as well as a screenshot of the best model trained with it's parameters.

## Model Deployment
*TODO*: Give an overview of the deployed model and instructions on how to query the endpoint with a sample input.

## Screen Recording
*TODO* Provide a link to a screen recording of the project in action. Remember that the screencast should demonstrate:
- A working model
- Demo of the deployed  model
- Demo of a sample request sent to the endpoint and its response

## Standout Suggestions
*TODO (Optional):* This is where you can provide information about any standout suggestions that you have attempted.
