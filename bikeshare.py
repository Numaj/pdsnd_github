import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
                  'new york city': 'new_york_city.csv',
                  'washington': 'washington.csv' }
def get_filters():
    month_dict={'jan':'january','feb':'february','mar':'march','apr':'april','may':'may','jun':'june','jul':'july','aug':'august','sep':'september','oct':'october','nov':'november','dec':'december'}
    day_dict={'mon':'monday','tue':'tuesday','wed':'wednesday','thu':'thursday','fri':'friday','sat':'saturday','sun':'sunday'}

    print('Hello! Let\'s explore some US bikeshare data!')
        # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city=input('Which city would you like to choose ? press chicago, new york city,washington \n').lower()
    while (city !='chicago' and city !='new york city'and city !='washington'):
        city=input('Please choose by typing chicago, new york city or washington \n').lower()

    if (city=='chicago'):
        print('You chose Chicago')
    if (city=='new york city'):
        print('You chose New York City')
    if (city=='washington'):
        print('You chose Washington')
        # TO DO: get user input for month (all, january, february, ... , june)
    month=input("Which month would you like to choose ? press jan for January, feb for February, etc. Press 'all' to apply no month filter \n").lower()
    while (month not in month_dict and month!='all'):
        month=input("Please press jan/fev/mar/apr/may/jun/all \n").lower()
    for key, value in month_dict.items():
        if key == month:
            print ('You chose month {}' .format(month_dict[month]))
            break

            # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    day=input("Which day would you like to choose ? press mon for Monday, tue for Tuesday, etc. Press 'all' to apply no day filter \n").lower()
    while (day not in day_dict and day!='all'):
        day=input("Please press mon/tue/wed/thu/fri/sat/sun/all \n").lower()
    for key, value in day_dict.items():
        if key == day:
            print ('you chose {}' .format(day_dict[day]))
            break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    filename = CITY_DATA[city]
    df = pd.read_csv(filename)

    month_dict={'jan':1,'feb':2,'mar':3,'apr':4,'may':5,'jun':6}

    day_dict={'mon':'monday','tue':'tuesday','wed':'wednesday','thu':'thursday','fri':'friday','sat':'saturday','sun':'sunday'}

        # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

        # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

        # filter by month if applicable
    if month != 'all':
            # use the value of month_dict to get the corresponding int
        month = month_dict[month]

            # filter by month to create the new dataframe
        df = df[df['month'] == month]

        # filter by day of week if applicable
    if day != 'all':
        day=day_dict[day]
            # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])

        # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print('Most Popular month:', popular_month)

        # TO DO: display the most common day of week
    df['week'] = df['Start Time'].dt.week
    popular_week = df['week'].mode()[0]
    print('Most Popular week:', popular_week)

        # TO DO: display the most common start hour

        # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
        # find the most popular hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):

    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

        # TO DO: display most commonly used start station
    start_station=df['Start Station'].mode()[0]
    print('Most common start station: {}' .format(start_station))

        # TO DO: display most commonly used end station
    end_station=df['End Station'].mode()[0]
    print('Most common end station: {}' .format(end_station))

        # TO DO: display most frequent combination of start station and end station trip
    combin_station=df['Start Station'].astype(str) + ' to ' + df['End Station']
    most_combin_station= combin_station.mode()[0]
    print('Most frequent combination of start station and end station trip: {}' .format(most_combin_station))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):

    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

        # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time: {}' .format(total_travel_time))

        # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time: {}' .format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):

    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

        # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

        # TO DO: Display counts of gender
    try:
        genders = df['Gender'].value_counts()
        print(genders)
    except:
        print('There is no data available regarding the gender for this city')


    try:    # TO DO: Display earliest, most recent, and most common year of birth
        birth_earliest = df['Birth Year'].min()
        birth_most_recent = df['Birth Year'].max()
        birth_mode = df['Birth Year'].mode()[0]
        print('Earliest year of birth: {}'.format(birth_earliest))
        print('Most recent year of birth: {}'.format(birth_most_recent))
        print('Most common year of birth: {}'.format(birth_mode))
    except:
        print('There is no data available regarding the birth dates for this city')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):

    """Displays raw data on demand of the user."""

    i=0
    display_input=input("Would you like to see 5 first rows of raw data ? press yes or no \n").lower()
    while (display_input == 'yes'):
        print(df.iloc[i:i+5])
        i+=5
        display_input=input("Would you like to see 5 more rows of raw data ? press yes or no \n").lower()


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
