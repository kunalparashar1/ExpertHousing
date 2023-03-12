# Created on - 12-03-2023
# Created by - Kunal Parashar
# Objective - To create a python recommender that suggests whether to buy the property or not
# Last edited on - 12-03-2023

# Import necessary libraries
import pandas as pd

# Load real estate data into pandas dataframe
real_estate_data = pd.read_csv('real_estate_data.csv')

# Define metrics and sub-metrics
metrics = {'Location': ['Distance from city center', 'Access to public transport', 'Nearby amenities', 'Safety'],
           'Property features': ['Condition of property', 'Size of property', 'Age of property', 'Additional features'],
           'Neighborhood': ['Community facilities', 'Quality of schools', 'Sense of community', 'Noise level'],
           'Market trends': ['Price trend', 'Rental demand', 'Supply and demand', 'Market competition'],
           'Property management': ['Maintenance and repairs', 'Tenant screening', 'Vacancy rate', 'Rent collection'],
           'Financing options': ['Mortgage interest rate', 'Down payment', 'Closing costs', 'Loan terms'],
           'Tax implications': ['Property taxes', 'Capital gains taxes', 'Tax deductions', 'Tax credits'],
           'Investment potential': ['Potential for growth', 'Potential for income', 'Potential for resale', 'Risk level']}

# Ask user for input on sub-metrics and store responses in a dictionary
user_responses = {}
for metric, sub_metrics in metrics.items():
    print('\nPlease rate the following sub-metrics for the metric:', metric)
    sub_responses = {}
    for sub_metric in sub_metrics:
        sub_response = input('Please rate ' + sub_metric + ' from 1 to 4, with 4 being the highest: ')
        sub_responses[sub_metric] = int(sub_response)
    user_responses[metric] = sub_responses

# Calculate total score for each property based on user responses and store in dataframe
property_scores = pd.DataFrame(columns=['Property', 'Score'])
for i, row in real_estate_data.iterrows():
    score = 0
    for metric, sub_metrics in metrics.items():
        for sub_metric in sub_metrics:
            score += user_responses[metric][sub_metric] * row[sub_metric]
    property_scores = property_scores.append({'Property': row['Property'], 'Score': score}, ignore_index=True)

# Sort properties by score and display top recommendations
property_scores = property_scores.sort_values(by='Score', ascending=False)
print('\nTop 5 recommended properties based on your responses:')
print(property_scores.head(5))
