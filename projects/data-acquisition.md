# Data exploration and EDA Blog

## Introduction / why this project is relevant and interesting
This project explores a large amount of data from The Census Bureau API. I pulled data from the state of California (my home state). I manipulated the data and cleaned it and then began to research questions I had. A lot of these questions are things that I wondered about in high school and ones that arose as I explored the dataset that I had curated.

## Motivating question (what are you hoping to learn from this data?)

 - Is there a correlation between peoples income and if they own a cell phone or not?
 - Is there a correlation between income and age?
 - Is there a correlation between race and if they own a cell phone or not.

I explored all of these questions but in the end I chose to focus more on the correlation between income and smartphone ownership.

### How do I know this was ethical?
The process for getting this data was actually quite simple. I agreed to their terms and conditions and then applied for an API key which I received in about 2 min. The data is all public the main concern the terms and conditions focused on is that no one uses the data to try and figure out who individuals are. I was using this data for a much higher level analysis of the dataset as a whole so this was not an issue.

### Good scraping practices
To avoid overloading their servers I did my best to only use the API once for each year of data I pulled. I also did not ever put it in a loop so that I didn't pull the data over and over again without needing to. My API key is also saved in seperate folder that won't be uploaded to github to protect it.

## Summary of the steps needed to get your data with an emphasis on teaching other how they could get started with a similar project
The API call: One of the benefits I learned about APIs is that it makes collecting the data a lot simpler than if I were to webscrape it piece by piece from a website. I had to scan through a list of all the different variables that were available and choose the ones that I wanted included and from there it was only a matter of 1 API call that gave me all the data I could ever want and more for each year.

Cleaning the data: The grunt of what I had to do to clean this data was renaming columns to be less clunky and using provided tables to convert the numbers used for race and sex to be the strings associated with those values. This improved the readability of the data and allowed me to get more comfortable with it. 

Interpretation and summary: I then went through and wrote code that would work on all my years of data to plot and explore the data. While a lot of the charts and graphs I created showed little to nothing due to a lack of correlation I got very familiar with the data and was able to see what was going on inside of it. 

## EDA highlights: 

### summary statistics, 

### summary graphics, and/or 

### information about final dataset (e.g., total sample size, counts of categorical variables, numerical summaries of numeric variables)
## What are the most interesting findings of your EDA?
## Links to find further information and /or resources
## A link to your code in a separate GitHub repo