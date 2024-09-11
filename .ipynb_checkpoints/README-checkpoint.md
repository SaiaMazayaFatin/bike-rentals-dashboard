# Bike Rentals Analysis Dashboard

This **Bike Rentals Analysis Dashboard** is built using Streamlit. It visualizes the relationship between bike rentals and several factors such as weather, temperature, and time of day. The project follows a cycle from data wrangling, exploratory data analysis, data visualization, and dashboard development.

## Project Cycle

1. **Data Wrangling**  
   In this phase, data is cleaned and prepared for analysis, including the following steps:  
   - Gathering Data  
   - Assessing Data  
   - Cleaning Data  

2. **Exploratory Data Analysis (EDA)**  
   This step involves understanding the data through descriptive, univariate, and multivariate analyses to uncover insights.

3. **Data Visualization**  
   After performing EDA, visualizations are created to answer the questions raised during the analysis.

4. **Dashboard**  
   The final step involves building a dashboard to display the results of the analysis interactively using Streamlit.

## Features
- **Date Range Filter**: Filter bike rental data by selecting a date range.
- **Weather Condition Filter**: Analyze bike rentals based on weather conditions.
- **Interactive Visualizations**:
  - Bar charts, line charts, and scatter plots using Streamlit's built-in charting functions.
  - Key metrics displaying total rentals and average temperature.
- **Analysis**:
  1. How weather conditions impact bike rentals.
  2. The relationship between temperature and bike rentals (Scatter plot).
  3. Bike rentals by day of the week.
  4. Bike rental patterns across different hours of the day.
  5. Bike rentals segmented by weekday, time of day, and clustering.

## Data Sources
This dashboard uses two CSV datasets:
- `day.csv` (daily bike rentals data)
- `hour.csv` (hourly bike rentals data)

Ensure these datasets are placed in the project directory.

## Installation

1. **Install Python and Streamlit**:
   - First, ensure that Python is installed. If not, download it from [python.org](https://www.python.org/downloads/).
   - Install Streamlit using the following command:
     ```bash
     pip install streamlit
     ```

2. **Verify Streamlit Installation**:
   To verify that Streamlit is installed correctly, run the following command:
   ```bash
   streamlit hello
   ```
   
3.  **Run your Python File**:
    Syntax to run program
    ```bash
    streamlit run [your_file].py
    ```
