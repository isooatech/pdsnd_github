import time
import pandas as pd
import numpy as np

# define the necessary variables to manage input errors from user

CITY_DATA = { 'chicago': 'chicago.csv', 'new york city': 'new_york_city.csv', 'washington': 'washington.csv' }
Available_months = ['all','january','february','march','april','may','june']
Available_day_of_week = ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']

def get_filters():
    
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    
    print('Hello! Let\'s explore some US bikeshare data!')
    
    #Setting month and day to default No to ensure code doesn't break if user decides to exit from city
    
    month = 'No'
    day = 'No'
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    #Accepting user input for city to explore
    
    city = input('Chicago, New York City and Washington data are available. \nPlease enter the name of the state you would like to explore\n').lower().strip()
    
    #Implementing check to ensure city is correctly entered   
    
    while city not in CITY_DATA:
        print('You have made an incorrect input')
        loop = input('Will you like to continue? Enter Y for Yes or any other character to exit\n').lower().strip()
        if loop == 'y':
           city = input('Now enter the correct city! Available cities are Chicago, New York City and Washington\n').lower().strip()
           continue
        else:
            city = loop
            break
    
    
    
    if city in CITY_DATA:
        
        # TO DO: get user input for month (all, january, february, ... , june)
        
        month = input('Would you like to view all months or a specific month between january and june\n').lower().strip()
        
        while month not in Available_months:
                print('You have made an incorrect input')
                month_loop = input('Will you like to continue with a correct month input? \nEnter Y for Yes or any other character to exit\n').lower().strip()
                if month_loop == 'y':
                    month = input("Now enter the correct month! You can enter 'all' if you want to see for all available months or 'January to June' for a specific month\n").lower().strip()
                    continue
                else:
                    month = month_loop
                    break        
        
        #Handling wrong input errors
        if month in Available_months:
             # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        
            day = input('Would you like to view all days of the week or a specific day of week\n').lower().strip()
        
            #Handling wrong input errors
            
            while day not in Available_day_of_week:
                print('You have made an incorrect input')
                day_loop = input('Will you like to continue with a correct day input? \nEnter Y for Yes or any other character to exit\n').lower().strip()
                if day_loop == 'y':
                    day = input("Now enter the correct day!\n You can enter 'all' for all the days of the week or 'Monday to Friday' for a specific day\n").lower().strip()
                    continue
                else:
                    day = day_loop
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
    df = pd.read_csv(CITY_DATA[city])
    
    # Convert the start time of the database to datetime format
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
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

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    popular_month = df['month'].mode()[0]
    popular_month_name = months[popular_month - 1]
    print('The most popular month is', popular_month_name)

    
    # TO DO: display the most common day of week
    
    popular_day = df['day_of_week'].mode()[0]
    print(popular_day)

    # TO DO: display the most common start hour
    
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print(popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_station= df['Start Station'].mode()[0]
    popular_station_count = df['Start Station'].value_counts()[0]
    print("The most popular start station is", popular_station, "with a count of", popular_station_count)


    # TO DO: display most commonly used end station
    
    popular_end_station = df['End Station'].mode()[0]
    print(popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip

    df['Start to End'] = df['Start Station'] + ' to ' + df ['End Station']
    
    most_start_to_end = df['Start to End'].mode()[0]
    
    print(most_start_to_end)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time:',total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time:',mean_travel_time)

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
    if 'Gender' in df.columns:
        gender_types = df['Gender'].value_counts()
        print(gender_types)
    else:
        pass
    
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        most_recent_year = df['Birth Year'].max()
        earliest_year = df['Birth Year'].min()
        most_common_year = df['Birth Year'].mode()[0]
        print(most_recent_year, earliest_year, most_common_year)
    else:
        pass

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    

def part(df):
    #This function returns the next 5 rows on the request of the user
    start = 0
    end = 5
    
    df_lenght = len(df)
    while input('Enter Y for Yes to view some part of the dataset.\nIf not interested, press any key to continue\n').lower().strip() == 'y' and end < df_lenght :
        print(df.iloc[start:end,:])
        start +=5
        end+=5
        
    
    
    
    
def main():
    while True:
        city, month, day = get_filters()
        #The if block ends allows code to end without breaking if user decides to end program at first stage
        if city in CITY_DATA and month in Available_months and day in Available_day_of_week:
            
        
            df = load_data(city, month, day)

            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)
            part(df)
        else:
            pass
        restart = input('\nWould you like to restart? \nEnter Y for Yes or N for No\n').lower().strip()
        if restart.lower() != 'y':
            break
            
            
if __name__ == "__main__":
	main()
