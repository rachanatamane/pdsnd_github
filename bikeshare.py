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
    
    
    
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Which city would you like to look at: Chicago, New York City, or Washington?\n")
        
        if city.lower() not in ('chicago', 'new york city', 'washington'):
            print('You chose the wrong city. Please try again')
        else:
            break
       
    city = city.lower()

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input("Which month from January to June would you like to search?\n"
                     "Or type 'all' to search all available months.\n")
        
        if month.lower() not in('january', 'february', 'march', 'april', 'may', 'june', 'all'):
            print('You chose the wrong month. Please try again')
        else:
            break

   
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Which day of the week would you like to go to?\n"
                   "Or type 'all' to search all days of the week\n")
        if day.lower() not in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all'):
            print('You chose the wrong day. Please try again')
        else:
            break
    


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
    #load data file into DataFrame
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    
    
    # filter by month if applicable
    if month != 'all':
        # use the index of month list to get the corresponding into
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create new DataFrame
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        #filter by day of week to create new DataFrame
        df = df[df['day_of_week'] == day.title()]

    #print(df['Start Time'])
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month 
    popular_month = df['month'].mode()[0]
    print('Most common month is:',popular_month)


    # display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Most common day of the week is:',popular_day)


    # display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('Most common start hour of the day is:', popular_hour,':00')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].value_counts().index[0]
    print('The most commonly used starting station is:',popular_start_station)


    # display most commonly used end station
    popular_end_station = df['End Station'].value_counts().index[0]
    print('The most commonly used ending station is:',popular_end_station)


    # display most frequent combination of start station and end station trip
    popular_trip = df['Start Station'].mode()[0] + ' -to- ' + df['End Station'].mode()[0]
    print('The most popular trip:', popular_trip)
    
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel = df['Trip Duration'].sum()
    total_travel_m = total_travel / 60 #minutes conversion
    total_travel_h = total_travel / 60 #hours conversion
    print('The total travel time is', total_travel_h, 'hours')


    # display mean travel time
    mean_travel = df['Trip Duration'].mean()
    mean_travel = mean_travel / 60
    print('The mean travel time is', mean_travel,'minutes')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    
    # Display counts of gender
    gender_types = df['Gender'].value_counts()
    print(gender_types)


    # Display earliest, most recent, and most common year of birth
    oldest_rider = df['Birth Year'].min()
    print('The oldest rider was born in', oldest_rider)
    
    
    youngest_rider = df['Birth Year'].max()
    print('The youngest rider was born in', youngest_rider)
    
    
    common_age_rider = df['Birth Year'].mode()[0]
    print('The average year most riders were born is',common_age_rider)
    
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats_wash(df):
    """Displays statistics on bikeshare users in Washington since data is missing gender/age groups."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        # Display raw data with user input
        more_data = True
        line_count = 5
        while more_data:
            see_data = input("Would you like to see the first 5 lines of raw data ('Yes' or 'No')\n>>>")
            see_data = see_data.lower()

            if see_data == 'yes':
                print(df.head())
                while True:
                    see_data = input("Would you like to see 5 more lines of raw data (Press ENTER for Yes or enter 'No')\n>>>")
                    see_data = see_data.lower()
                    if see_data == '' or see_data == 'yes':
                        print(df.iloc[line_count:line_count+5, :])
                        line_count += 5
                        if line_count > df.shape[0]:
                            more_data = False
                            print('End of Data')
                            break
                    elif see_data == 'no':
                        more_data = False
                        break
                    else:
                        print("'{}' is an invalid entry.  Please enter ('Yes' or 'No')".format(see_data))
                        
            elif see_data == 'no':
                break
            else:
                print("'{}' is an invalid entry.  Please enter ('Yes' or 'No')".format(see_data))       
         
        print('\n' + '-'*60)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()