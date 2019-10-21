This project uses Ohio voter registration and data from the US Census Bureau to determine the precincts within a state congressional district which have a large number of likely 2020 voters. The goal is to suggest regions for political canvassing. This project was made for the Insight Data Science program.

The State of Ohio publishes state-wide voter registration files containing lists of registered voters, including their name, age, date of registration, party affiliation, voting history, and which districts and precincts they are registered to vote in. The US Census Burea provides zip-code-level demographic information. I used this information to predict whether someone would vote in the 2020 election. From the Ohio voter files I look at age, (#elections voted in)/(#elections eligible to vote in), and whether someone voted in the previous presidential year election. From the census bureau I looked at zip-code-level education information: the percentage of people who had high school diplomas, and the percentage who had a bachelor's degree or higher.

I used these features to train a logistic regression. I used 60% of the data as a training set, and trained using the 2016 election as the training election. I used the 2000 to 2016 time window for the election participation fraction in the training set, and then moved the time window to 2004 to 2020 when running the prediction. 

The prediction was used to select the three precincts inside of the state congressional district that had the most likely voters. The app, located at https://canvassohio.herokuapp.com/, displays the precincts on a map of the district, and lists them with their party lean. The party lean is determined from the likely voters who are registered with a particular party. Of the voters who are registered with a party, if more than 52.5% are registered Republican or Libertarian, the precinct is labeled "lean right". If more than 52.5% are registered Democrat or Green, it is labeled "lean left". If the margin is smaller than that, the label is "lean neutral".

The app was implemented in Flask and hosted using Heroku.

Data courtesy of the Secretary of State of Ohio and the US Census Bureau. District shape files from census.gov.

Precinct shapefiles courtesy of the Metric Geometry and Gerrymandering Group. Find the github repository at https://github.com/mggg/ohio-precincts.
