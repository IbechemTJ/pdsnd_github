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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Please input a city, chicago, new york city, or washington? ' ).lower()
        if city in ['chicago', 'new york city', 'washington']:
            break
        else:
            print('Please input a valid city; Input only either chicago, new york city or washington')

    print('Value entered: ', city)

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Please input a month of the year from January to June, or input "all" for all months? ' ).lower()
        if month in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
            break
        else:
            print('Please input a valid month; Input only a month of the year from January to June, or input "all" for all months')

    print('Value entered: ', month)

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Please input a day of the week from Monday to Sunday, or input "all" for all days? ' ).lower()
        if day in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
            break
        else:
            print('Please input a valid day of the week from Monday to Sunday, or input "all" for all days')

    print('Value entered: ', day)
    print('-'*40)
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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most  Frequent Times of Travel...\n')
    start_time = time.time()

    # Converting the Start Time column to datetime.
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # TO DO: display the most common month
    # Extracting month from the Start Time column to create a month column
    df['month'] = df['Start Time'].dt.month
    # Finding the most common month
    most_common_month = df['month'].mode()[0]
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    print('\nThe most common month is: ', months[most_common_month - 1])

    # TO DO: display the most common day of week
    # Extracting dayofweek from the Start Time column to create a day_of_week column
    df['day_of_week'] = df['Start Time'].dt.dayofweek
    # Finding the most common day of the week
    most_common_day = df['day_of_week'].mode()[0]
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    print('\nThe most common day of week is: ', days[most_common_day])

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    # Finding the most common hour
    most_common_hour = df['hour'].mode()[0]
    print('\nThe most common hour is: ', most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('Most Commonly Used Start Station: ', df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print('Most Commonly Used End Station: ', df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    print('\nMost Frequent Combination of Start and End Station Trips:\n\n',df.groupby(['Start Station', 'End Station']).size().nlargest(1))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total Trip Duration:', df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print('Mean Trip Duration:', df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types,'\n')

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender = df['Gender'].value_counts()
        print(gender,'\n')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print('Earliest year of Birth:', df['Birth Year'].min())
        print('Most Recent year of Birth:', df['Birth Year'].max())
        print('Most Common year of Birth:', df['Birth Year'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_raw_data(df):
    """ Displays the raw data of bikeshare data 5 rows at a time after the various computations"""
    i = 0
    pd.set_option('display.max_columns',200)

    # TO DO: convert the user input to lower case using lower() function
    raw = input("Do you want to view the raw data? Please type only 'yes' or 'no'\n").lower()

    while True:
        if raw == 'no':
            break
        elif raw == 'yes':
            # TO DO: appropriately subset/slice your dataframe to display next five rows
            print(df.iloc[i : i + 5])
            # TO DO: convert the user input to lower case using lower() function
            raw = input("Do you want to view more raw data? Please type only 'yes' or 'no'\n").lower()
            i += 5
        else:
            raw = input("\nYour input is invalid. Please enter only 'yes' or 'no'\n").lower()

    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)


        while True:
            restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
            if restart == 'yes' or restart == 'no':
                break
            else:
                print('Please Enter Yes or No:\n')

        if restart == 'no':
            print('BYE!')
            break
        else:
            print("Restarting______________________")


if __name__ == "__main__":
	main()
