import streamlit as st
import pandas as pd

# Load data
clean_df_hour = pd.read_csv('dashboard/final_hour.csv')
clean_df_day = pd.read_csv('dashboard/final_day.csv')

# Rename columns
clean_df_day = clean_df_day.rename(columns={
    'instant': 'instance_id',
    'dteday': 'date',
    'yr': 'year',
    'mnth': 'month',
    'holiday': 'holiday',
    'weekday': 'day_of_week',
    'workingday': 'working_day',
    'weathersit': 'weather_condition',
    'temp': 'temperature',
    'atemp': 'feeling_temperature',
    'hum': 'humidity',
    'windspeed': 'wind_speed',
    'casual': 'casual_riders',
    'registered': 'registered_riders',
    'cnt': 'total_rentals'
})

clean_df_hour = clean_df_hour.rename(columns={
    'instant': 'instance_id',
    'dteday': 'date',
    'yr': 'year',
    'mnth': 'month',
    'hr': 'hour',
    'weekday': 'day_of_week',
    'workingday': 'working_day',
    'weathersit': 'weather_condition',
    'temp': 'temperature',
    'atemp': 'feeling_temperature',
    'hum': 'humidity',
    'windspeed': 'wind_speed',
    'casual': 'casual_riders',
    'registered': 'registered_riders',
    'cnt': 'total_rentals'
})

# Convert date column to datetime
clean_df_hour['date'] = pd.to_datetime(clean_df_hour['date'])
clean_df_day['date'] = pd.to_datetime(clean_df_day['date'])

# Set page title
st.title("Bike Rentals Analysis Dashboard")

# Sidebar for Date Filtering
st.sidebar.title("Filters")
st.sidebar.header("Date Range")
min_date = clean_df_day['date'].min()
max_date = clean_df_day['date'].max()

start_date, end_date = st.sidebar.date_input(
    label="Select Date Range",
    min_value=min_date,
    max_value=max_date,
    value=[min_date, max_date]
)

# Weather condition selection
weather_conditions = clean_df_day['weather_condition'].unique()
selected_weather = st.sidebar.multiselect(
    "Select Weather Condition",
    weather_conditions,
    default=weather_conditions
)

# Filter dataset based on the selected date range and weather conditions
filtered_df_day = clean_df_day[(clean_df_day['date'] >= pd.to_datetime(start_date)) & 
                                 (clean_df_day['date'] <= pd.to_datetime(end_date)) & 
                                 (clean_df_day['weather_condition'].isin(selected_weather))]

filtered_df_hour = clean_df_hour[(clean_df_hour['date'] >= pd.to_datetime(start_date)) & 
                                   (clean_df_hour['date'] <= pd.to_datetime(end_date)) & 
                                   (clean_df_hour['weather_condition'].isin(selected_weather))]

# Display the filtered dataframes
st.subheader(f"Filtered Bike Rentals Data (Daily): {start_date} to {end_date}")
st.dataframe(filtered_df_day.head())

st.subheader(f"Filtered Bike Rentals Data (Hourly): {start_date} to {end_date}")
st.dataframe(filtered_df_hour.head())

# Key Metrics
st.subheader("Key Metrics")
total_rentals_day = filtered_df_day['total_rentals'].sum()
avg_temp_day = filtered_df_day['temperature'].mean()

col1, col2 = st.columns(2)
with col1:
    st.metric("Total Bike Rentals (Day)", value=int(total_rentals_day))
with col2:
    st.metric("Average Temperature (Day)", value=round(avg_temp_day, 2))

# Question 1: How the weather can affect the number of bikes that are rented?
st.header("Question 1: How does the weather affect bike rentals?")

effect_day = filtered_df_day.groupby('weather_condition')['total_rentals'].mean().reset_index()
effect_hour = filtered_df_hour.groupby('weather_condition')['total_rentals'].mean().reset_index()

st.subheader("Average Bike Rentals by Weather Condition")
st.bar_chart(effect_day.set_index('weather_condition')['total_rentals'])
st.bar_chart(effect_hour.set_index('weather_condition')['total_rentals'])

# Question 2: What is the relationship between temperature and bike rentals?
st.header("Question 2: Relationship between Temperature and Bike Rentals")

st.subheader("Daily Data")
st.scatter_chart(filtered_df_day[['temperature', 'total_rentals']])

st.subheader("Hourly Data")
st.scatter_chart(filtered_df_hour[['temperature', 'total_rentals']])

# Question 3: Which days of the week have the highest and lowest bike rental activity?
st.header("Question 3: Bike Rentals by Weekday")

weekday_activity_day = filtered_df_day.groupby('day_of_week')['total_rentals'].mean().reset_index()
weekday_activity_hour = filtered_df_hour.groupby('day_of_week')['total_rentals'].mean().reset_index()

st.subheader("Daily Data")
st.bar_chart(weekday_activity_day.set_index('day_of_week')['total_rentals'])

st.subheader("Hourly Data")
st.bar_chart(weekday_activity_hour.set_index('day_of_week')['total_rentals'])

# Question 4: Influence of time of day on bike rentals on weekdays vs weekends
st.header("Question 4: Hourly Bike Rentals by Working Day")

hourly_workingday = filtered_df_hour.groupby(['hour', 'working_day'])['total_rentals'].mean().reset_index()

st.subheader("Hourly Rentals by Working Day")
st.line_chart(hourly_workingday.pivot(index='hour', columns='working_day', values='total_rentals'))

# Question 5: Bike rental patterns between weekdays and weekends (Clustering)
st.header("Question 5: Bike Rentals by Weekday and Time of Day Clusters")

filtered_df_hour['time_cluster'] = pd.cut(filtered_df_hour['hour'], 
                                 bins=[0, 6, 12, 18, 24], 
                                 labels=['Night', 'Morning', 'Afternoon', 'Evening'], 
                                 right=False)

weekday_time_cluster = filtered_df_hour.groupby(['day_of_week', 'time_cluster'])['total_rentals'].mean().reset_index()

st.subheader("Average Bike Rentals by Weekday and Time Clusters")
st.bar_chart(weekday_time_cluster.pivot(index='day_of_week', columns='time_cluster', values='total_rentals'))
