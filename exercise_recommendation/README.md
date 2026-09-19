# Exercise Recommendation System Using Machine Learning

A Flask web app that estimates body fat percentage from body measurements using a Random Forest Regression model, then recommends either a fat-burning or a maintenance workout plan.

Developed as part of an Industry Oriented Mini Project at CMR Technical Campus (2024-25).

## Overview

Generic fitness advice ignores where a person starts. This app takes body measurements, predicts body fat percentage with a trained model, and turns that number into an exercise recommendation: high-intensity workouts for higher body fat, maintenance workouts for a healthy level.

## How It Works

1. The user enters five measurements: body density, abdomen circumference, chest circumference, weight (lbs), and hip circumference.
2. The Flask app loads a pre-trained Random Forest Regression model (saved as a pickle file) and predicts body fat percentage.
3. Based on the predicted value and a body-fat threshold in the code, the app shows a matching exercise plan:
   - Higher body fat: HIIT, running, cycling, jump rope, swimming, and weightlifting
   - Healthy range: walking, jogging, push-ups, squats, lunges, planks, and stretching

## Model

- Algorithm: Random Forest Regression (Scikit-learn), saved with `pickle`
- Training data: body-measurement dataset with density, abdomen, chest, weight, and hip columns, and body fat percentage as the target

## Tech Stack

- Python, Flask
- Scikit-learn, Pandas, NumPy
- HTML
- Can run locally or be deployed to a cloud platform such as AWS

## Project Status and Future Work

- Report test-set metrics (MAE, RMSE, R²) for the model
- Body density normally comes from underwater weighing, which most users do not have; replace it with easy inputs such as height, weight, waist, and age
- Add user accounts, progress tracking with a database, and more exercise plans
- Deploy the app to the cloud

## Author

Busani Chaitanya
B.Tech CSE (Design), CMR Technical Campus
Contact: busani.chay@gmail.com
