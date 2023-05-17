from datetime import datetime, timedelta

import streamlit as st


# Function to get the calendar for a given month and year
def get_calendar(year, month):
    month_start = datetime(year, month, 1)
    next_month = month_start + timedelta(days=32)
    month_end = datetime(next_month.year, next_month.month, 1) - timedelta(days=1)
    return month_start, month_end


# Function to render the calendar
def render_calendar(year, month):
    month_start, month_end = get_calendar(year, month)
    st.title(f"Calendar - {month_start.strftime('%B %Y')}")

    # Display the calendar table
    col1, col2, col3, col4, col5, col6, col7 = st.beta_columns(7)
    col1.header("Mon")
    col2.header("Tue")
    col3.header("Wed")
    col4.header("Thu")
    col5.header("Fri")
    col6.header("Sat")
    col7.header("Sun")

    current_date = month_start
    while current_date <= month_end:
        col_index = current_date.weekday()
        if col_index == 0:
            col = col1
        elif col_index == 1:
            col = col2
        elif col_index == 2:
            col = col3
        elif col_index == 3:
            col = col4
        elif col_index == 4:
            col = col5
        elif col_index == 5:
            col = col6
        else:
            col = col7

        col.write(current_date.strftime("%d"))
        current_date += timedelta(days=1)


# Main application
def main():
    st.write("# Calendar App")

    # Get the current year and month
    current_date = datetime.now()
    year = st.sidebar.number_input("Year", value=current_date.year, min_value=1900, max_value=2100)
    month = st.sidebar.number_input("Month", value=current_date.month, min_value=1, max_value=12)

    # Render the calendar
    render_calendar(year, month)


if __name__ == "__main__":
    main()
