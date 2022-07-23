import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # get user input for city (chicago, new york city, washington).
    city = ''
    while True:
        city = input('Which city would you like to explore? Options: (Chicago, New York City, Washington?) ').lower()
        print(city)
        if city != 'chicago' and city != 'new york city' and city != 'washington':
            print("Sorry, I don't understand your response")
            continue
        else:
            break


    # get user input for month (all, january, february, ... , june)
    month = ''
    while True:
        month = input('Which months? Options: (All, January, February, March, April, May, June) ').lower()
        print(month)
        if month != 'all' and month != 'january' and month != 'february' and month != 'march' and month != 'april' and month != 'may' and month != 'june':
            print("Sorry, I don't understand your response")
            continue
        else:
            break


    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = ''
    while True:
        day = input('Which days? Options: (All, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday) ').lower()
        if day != 'all' and day != 'monday' and day != 'tuesday' and day != 'wednesday' and day != 'thursday' and day != 'friday' and day != 'saturday' and day != 'sunday':
            print("Sorry, I don't understand your response")
            continue
        else:
            break


    print('-'*40)
    print(city, month, day)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.strftime("%A")
    
    # use the index of the months list to get the corresponding int
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        print(month)
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week to create the new dataframe
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    month_mode_series = df['month'].mode()
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    mode_month = months[month_mode_series.iloc[0] - 1]
    print('Most common month: ' + str(mode_month.title()))

    # display the most common day of week
    day_mode_series = df['day_of_week'].mode()
    mode_day = day_mode_series.iloc[0]
    print('Most common day:   ' + str(mode_day))

    # display the most common start hour
    df_hours = df['Start Time'].dt.hour
    hours_mode_series = df_hours.mode()
    mode_hour = hours_mode_series.iloc[0]
    print('Most common hour:  ' + str(mode_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('Most common start station: ' + str(df['Start Station'].mode().iloc[0]))

    # display most commonly used end station
    print('Most common end station:   ' + str(df['End Station'].mode().iloc[0]) + '\n')

    # display most frequent combination of start station and end station trip
    print('Most rode route: \n' + 'From: ' +str((df['Start Station'] + '\n' + 'To:   ' + df['End Station']).mode().iloc[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('Total travel time:   ' + str(df['Trip Duration'].sum()))

    # display mean travel time
    print('Average travel time: ' + str(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    # Display counts of user types
    print('Types of users: ')
    user_type_df = df['User Type'].value_counts()
    for ind, val in user_type_df.iteritems():
        print(str(ind) + ': ' + str(val))

    # Display counts of gender
    print('\nNumber of males and females: ')
    try:
        df_gender_counts = df["Gender"].value_counts()
    except:
        print("Error: Gender was not collected for Washington")
    else:
        print('Male:   ' + str(df_gender_counts.iloc[0]))
        print('Female: ' + str(df_gender_counts.iloc[1]))    

    # Display earliest, most recent, and most common year of birth
    print("\nBirth year statistics:")
    try:
        earliest_birth_y_int = int(df["Birth Year"].min())
        earliest_birth_y_str = str(earliest_birth_y_int)
        most_recent_birth_y = str(int(df["Birth Year"].max()))
        most_common_birth_y = str(int(df["Birth Year"].mode().iloc[0]))
    except:
        print("Error: Birth Year was not collected for Washington")
    else:
        print('Earliest:    ' + earliest_birth_y_str)
        print('Most recent: ' + most_recent_birth_y)
        print('Most common: ' + most_common_birth_y)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """
    Displays the filtered DataFrame 5 at a time until the user inputs no.
    This will display all columns.
    """

    #Set display options to have no max column restriction.
    pd.options.display.max_columns = None
    #Have the user input if they want to see 5 rows of data.
    view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?").lower()
    start_loc = 0
    
    #If the user chooses yes, display 5 rows.
    if view_data == 'yes':
        while True:
            print(df.iloc[start_loc: start_loc + 5])
            start_loc += 5
            view_display = input("Do you wish to continue?: ").lower()
            #If the users chooses yes again, display another 5 rows.
            if view_display == 'yes':
                continue
            else:
                break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
