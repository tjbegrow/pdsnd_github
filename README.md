### Date created
7/20/22

### Project Title
Bike Share Analysis

### Description
This program analyzes bike share data from Chicago, New York and Washington.
The user indicates what city, month and day of the week they would like to see
results for. Once the stats are shown, the user has the option to see the DataFrames 5 at a time until they decide to stop. The application will then ask if it should be reset or not. If it is reset, the user will be brought back to the first prompt.

### Files used
bikeshare.py
chicago.csv
new_york_city.csv
washington.csv

### Credits
I didn't know how get Pandas to display a DataFrame in the terminal with all of its columns. I found out how here:
https://stackoverflow.com/questions/11707586/how-do-i-expand-the-output-display-to-see-more-columns-of-a-pandas-dataframe

pd.options.display.max_columns = None

