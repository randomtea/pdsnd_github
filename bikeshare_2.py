#pycharm is used as IDE
#the latest pandas version 2.0.3 is used

import datetime
import time
import pandas as pd
import numpy as np

#git comment 1


CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():

    print('Hello! Let\'s explore some US bikeshare data!')

    cityName = input('Name of the city to analyze\n')
    while cityName.lower() not in ['chicago', 'washington', 'new york city']:
        print('invalid input, please select between chicago, washington, or new york city')
        cityName = input('Name of the city to analyze\n')

    month = input('name of the month to filter by, or "all" to apply no month filter\n')
    while month.lower() not in ['all', 'january', 'february','march','april','may','june']:
        print('invalid input, please select months from january to december or "all"')
        month = input('name of the month to filter by, or "all" to apply no month filter\n')

    day = input('name of the day of week to filter by, or "all" to apply no day filter\n')
    while day.lower() not in ['all','monday', 'tuesday', 'wednesday','thursday','friday','saturday','sunday']:
        print('invalid input, please select day of the week from monday to sunday or "all')
        day = input('name of the day of week to filter by, or "all" to apply no day filter\n')

    print('-' * 40)
    return cityName, month, day


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
    df['day_of_week'] = df['Start Time'].dt.day_name()
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    common_month = df['month'].mode()[0]
    print('Most common month: ', common_month)

    # display the most common month
    common_day = df['day_of_week'].mode()[0]
    print('Most common day of the week: ', common_day)

    # display the most common day of week

    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    common_hour_count = df['hour'].value_counts()[common_hour]

    print('Most common start time: ',  common_hour,'| Count:',common_hour_count)

    # display the most common start hour

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    common_start_station_count = df['Start Station'].value_counts()[common_start_station]
    print('Most common start station is ',common_start_station, '| Count: ',common_start_station_count)

    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    common_end_station_count = df['End Station'].value_counts()[common_end_station]

    print('Most common end station is ',common_end_station,'| Count: ',common_end_station_count)

    # display most frequent combination of start station and end station trip
    most_combination = df.groupby(['Start Station','End Station']).size().idxmax()

    print('The most frequent combination is: ', most_combination)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()

    avg_travel_time = df['Trip Duration'].mean()

    print('The total duration is:',datetime.timedelta(seconds=int(total_travel_time)),'\nThe average duration is:',datetime.timedelta(seconds=int(avg_travel_time)))



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)



def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # Display counts of user types

    subscriber_count = df['User Type'].value_counts()['Subscriber']
    customer_count = df['User Type'].value_counts()['Customer']

    print('Subscriber count: ',subscriber_count)
    print('Customer count: ',customer_count)

    # Display counts of gender

    if city != 'washington':
        male_count = df['Gender'].value_counts()['Male']
        print('Total male count: ',male_count)
        female_count = df['Gender'].value_counts()['Female']
        print('Total female count: ',female_count)

        earliest_year_birth = df['Birth Year'].min()
        recent_year_birth = df['Birth Year'].max()
        most_common_birth = df['Birth Year'].mode()[0]

        print('The earliest birth year is: ', earliest_year_birth)
        print('The most recent birth year is: ', recent_year_birth)
        print('The most common birth year is: ', most_common_birth)

    if city == 'washington':
        print('Gender and Birth Year data not available for Washington')

    # Display earliest, most recent, and most common year of birth




    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def show_stats(df,city):

    view_data = input('Would you like to see detailed statistics?\n')

    while view_data.lower() not in ['yes','no']:
        print('invalid input, please select between yes and no')
        view_data = input('Would you like to see detailed statistics?\n')
    i = 0

    while view_data.lower() == 'yes' and city != 'washington':
        row_count = 5

        for x in range(row_count):

            print('Start Time is: ', df['Start Time'].iloc[i])
            print('End Time is: ',df['End Time'].iloc[i])
            print('Trip Duration is: ',df['Trip Duration'].iloc[i])
            print('Start Station is: ', df['Start Station'].iloc[i])
            print('End Station is: ',df['End Station'].iloc[i])
            print('User Type is: ',df['User Type'].iloc[i])
            print('Gender is: ',df['Gender'].iloc[i])
            print('Birth year is: ',df['Birth Year'].iloc[i])
            i = i+1

            print('-' * 40)
        view_data = input('Would you like to see detailed statistics?\n')
        while view_data.lower() not in ['yes','no']:
            print('invalid input, please select between yes and no')
            view_data = input('Would you like to see detailed statistics?\n')

    while view_data.lower() == 'yes' and city == 'washington':
        row_count = 5

        for x in range(row_count):

            print('Start Time is: ', df['Start Time'].iloc[i])
            print('End Time is: ',df['End Time'].iloc[i])
            print('Trip Duration is: ',df['Trip Duration'].iloc[i])
            print('Start Station is: ', df['Start Station'].iloc[i])
            print('End Station is: ',df['End Station'].iloc[i])
            print('User Type is: ',df['User Type'].iloc[i])
            i = i+1

            print('-' * 40)
        view_data = input('Would you like to see detailed statistics?\n')

        while view_data.lower() not in ['yes','no']:
            print('invalid input, please select between yes and no')
            view_data = input('Would you like to see detailed statistics?\n')


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city.lower(), month.lower(), day.lower())

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city.lower())
        show_stats(df,city.lower())

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
