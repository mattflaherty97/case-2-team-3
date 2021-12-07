# Loan Prediction

## Key Objectives
We have two goals for this project. First, we would like to predict the probability that an individual defaults on a loan. The second is to determine the features that are most important in determining if an individual will default on a loan. We think that it will be important to determine important features along with probabilities because individuals might want to know the areas which are holding them back from having a lower probability of defaulting on a loan.

## Approach
* Exploratory data analysis and feature engineering on data provided
* Balanced training data using SMOTE
* Modeling using decision tree classifier, random forest classifier, logistic regression, and ridge classifier
* Creation of dashboard to allow for user functionality

## Findings
Important features for predicting a default on a loan:
* Income
* Age
* Experience
* Years at current job
* GDP (state)
* Years in current house

## Next Steps
* Integrate additional features to improve predictive power of model
* Include loan amounts as this will likely influence default rates
* Improve dashboard functionality for users
---
## Background
This project uses consumer data belonging to a Hackathon organized by "Univ.AI". This project is targeted to benefit loan givers, borrowers, and government institutions. We believe that it will benefit those distributing the loans because they will be able to determine the likelihood of an individual defautling on a loan and will be able to distirbute loans more efficiently. Borrowers will be able to benefit from this analysis as well becuase they will be able to determine areas in which they need to improve in order for their likelihood to default to decrease. Government institutions will also benefit from this because they will be able to determine where to provide aid.

## Data
All values were provided at the time of the loan application. It contains 12 columns, including income, age, experience, profession, marriage, house ownership, car ownership, risk flag, job years, house tears, city and state. 

## Relative Recources
* **Dataset:** [Loan Prediction Based on Customer Behavior](https://www.kaggle.com/subhamjain/loan-prediction-based-on-customer-behavior?select=Training+Data.csv)
* **Topic Selection:** [Topic Selection Google Docs](https://docs.google.com/document/d/19xLIllcyRP5w9erRgP2w27jL7wbaO581z5OsHeHq9GI/edit)
* **Team Charter:** [Team Charter Google Docs](https://docs.google.com/document/d/1Kb17YtmSjuI7ESMgf-fG6SVkB027VWkTum1VQCMPtMo/edit)
* **Project Plan:** [Project Plan Google Docs](https://docs.google.com/document/d/1jOURIGWK7Eu6EH9hPWfGwKOmz_ZKquQbvK2M-ODjXpg/edit)
* **Application:** [Streamlit Loan Default Web App](https://share.streamlit.io/mattflaherty97/case-2-team-3/main/app.py)
* **Presentation:** [Slideshow](https://docs.google.com/presentation/d/19141gmb6tx4gKJis2-VZAPTrDiECTHeAuwADPThrxuA/edit#slide=id.gfc271f9619_0_2254)
