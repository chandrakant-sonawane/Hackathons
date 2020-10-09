# JanataHack - NLP Hackathon
### [Hackathon Link](https://datahack.analyticsvidhya.com/contest/janatahack-nlp-hackathon/#About)
![alt text](https://github.com/chandrakant-sonawane/Hackathons/blob/master/JanataHack%20-%20NLP%20Hackathon/image.png)

## Hackathon Rank: 104th rank out of 2697 participants

## Problem Statement
### Sentiment Analysis for Steam Reviews
Steam is a video game digital distribution service with a vast community of gamers globally. A lot of gamers write reviews at the game page and have an option of choosing whether they would recommend this game to others or not. However, determining this sentiment automatically from text can help Steam to automatically tag such reviews extracted from other forums across the internet and can help them better judge the popularity of games.

Given the review text with user recommendation and other information related to each game for 64 game titles, the task is to predict whether the reviewer recommended the game titles available in the test set on the basis of review text and other information.

Game overview information for both train and test are available in single file game_overview.csv inside train.zip

### About Data Source:
Steam Platform

### Data Dictionary:

1. train.csv

| Column Name | Description |
| --------------- | --------------- |
| review_id | Unique ID for each review |
| title | Title of the game |
| year | Year in which the review was posted |
| user_review | Full Text of the review posted by a user |
| user_suggestion | (Target) Game marked Recommended(1) and Not Recommended(0) by the user |


2. game_overview.csv

| Column Name | Description |
| --------------- | --------------- |
| developer | Name of the developer of the game |
| publisher | Name of the publisher of the game |
| tags | Popular user defined tags for the game |
| overview | Overview of the game provided by the publisher |


3. test.csv

| Column Name | Description |
| --------------- | --------------- |
| review_id | Unique ID for each review |
| title | Title of the game |
| year | Year in which the review was posted |
| user_review | Full Text of the review posted by a user |

