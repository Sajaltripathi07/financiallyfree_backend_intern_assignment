import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime, timedelta


# page config
st.set_page_config(
    page_title="Vehicle Registration Dashboard",
    page_icon="🚗",
    layout="wide"
)

# title
st.title("🚗 Vehicle Registration Dashboard")
st.markdown("""
Welcome to the Vehicle Registration Dashboard!  
This interactive tool helps investors analyze vehicle registration 
trends across different categories and manufacturers.

*Note: This dashboard uses **synthetic data** for demonstration.*
""")


# data generation function
@st.cache_data
def load_sample_data():
    """Generates synthetic monthly registration data for 5 years."""

    categories = ['2W', '3W', '4W']  # Vehicle types
    manufacturers = {
        '2W': ['Hero', 'Honda', 'Bajaj', 'TVS', 'Royal Enfield'],
        '3W': ['Bajaj', 'Piaggio', 'Mahindra', 'TVS'],
        '4W': ['Maruti', 'Hyundai', 'Tata', 'Mahindra', 'Toyota', 'Honda']
    }

    end_date = datetime.now()
    start_date = end_date - timedelta(days=365*5)  # Last 5 years
    dates = pd.date_range(start=start_date, end=end_date, freq='M')

    data = []
    for date in dates:
        year = date.year
        quarter = (date.month - 1) // 3 + 1

        for category in categories:
            base = 1000 if category == '2W' else 500 if category == '3W' else 200

            for manufacturer in manufacturers[category]:
                # growth factors
                annual_growth = 1 + 0.1 * (year - start_date.year)
                quarterly_variation = 1 + 0.02 * quarter
                manufacturer_factor = 0.8 + 0.4 * ((hash(manufacturer + category) % 100) / 100)

                registrations = int(base * annual_growth * quarterly_variation * manufacturer_factor)

                data.append({
                    'Date': date,
                    'Year': year,
                    'Quarter': f"Q{quarter}",
                    'Category': category,
                    'Manufacturer': manufacturer,
                    'Registrations': registrations
                })

    return pd.DataFrame(data)


# load data
df = load_sample_data()


# sidebar filters
st.sidebar.header('Filters')

# date range filter
min_date = df['Date'].min().date()
max_date = df['Date'].max().date()
date_range = st.sidebar.date_input(
    'Select Date Range',
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

# category filter
categories = sorted(df['Category'].unique())
selected_categories = st.sidebar.multiselect(
    'Select Vehicle Categories',
    options=categories,
    default=categories
)

# manufacturer filter
manufacturers = sorted(df['Manufacturer'].unique())
selected_manufacturers = st.sidebar.multiselect(
    'Select Manufacturers',
    options=manufacturers,
    default=manufacturers
)

# apply filters
filtered_df = df[
    (df['Date'].dt.date >= date_range[0]) &
    (df['Date'].dt.date <= date_range[1]) &
    (df['Category'].isin(selected_categories)) &
    (df['Manufacturer'].isin(selected_manufacturers))
]


# kpi metrics
st.subheader('📊 Key Performance Indicators')
col1, col2, col3 = st.columns(3)

with col1:
    total_reg = filtered_df['Registrations'].sum()
    st.metric("Total Registrations", f"{total_reg:,}")

with col2:
    latest_year = filtered_df['Year'].max()
    prev_year = latest_year - 1
    current_year_total = filtered_df[filtered_df['Year'] == latest_year]['Registrations'].sum()
    prev_year_total = filtered_df[filtered_df['Year'] == prev_year]['Registrations'].sum()
    yoy_growth = ((current_year_total - prev_year_total) / prev_year_total * 100) if prev_year_total > 0 else 0
    st.metric("YoY Growth", f"{yoy_growth:.1f}%")

with col3:
    latest_date = filtered_df['Date'].max()
    prev_quarter_date = latest_date - pd.DateOffset(months=3)
    latest_quarter_total = filtered_df[filtered_df['Date'] == latest_date]['Registrations'].sum()
    prev_quarter_total = filtered_df[filtered_df['Date'] == prev_quarter_date]['Registrations'].sum()
    qoq_growth = ((latest_quarter_total - prev_quarter_total) / prev_quarter_total * 100) if prev_quarter_total > 0 else 0
    st.metric("QoQ Growth", f"{qoq_growth:.1f}%")



# time series trend
st.subheader('📈 Registration Trends')
trend_data = filtered_df.groupby(['Date', 'Category'])['Registrations'].sum().reset_index()

fig_trend = go.Figure()
for category in trend_data['Category'].unique():
    category_data = trend_data[trend_data['Category'] == category]
    fig_trend.add_trace(go.Scatter(
        x=category_data['Date'],
        y=category_data['Registrations'],
        mode='lines+markers',
        name=category
    ))

fig_trend.update_layout(
    title='Monthly Vehicle Registrations by Category',
    xaxis_title='Date',
    yaxis_title='Registrations',
    hovermode='x unified'
)
st.plotly_chart(fig_trend, use_container_width=True)



# category distribution
st.subheader('📊 Category-wise Distribution')
col1, col2 = st.columns(2)


# pie chart
with col1:
    pie_data = filtered_df.groupby('Category')['Registrations'].sum().reset_index()
    fig_pie = go.Figure(data=[go.Pie(
        labels=pie_data['Category'],
        values=pie_data['Registrations'],
        hole=.3
    )])
    fig_pie.update_layout(title_text='Registration Share by Category')
    st.plotly_chart(fig_pie, use_container_width=True)

# bar chart
with col2:
    bar_data = filtered_df.groupby(['Year', 'Category'])['Registrations'].sum().reset_index()
    fig_bar = go.Figure()
    for category in bar_data['Category'].unique():
        category_data = bar_data[bar_data['Category'] == category]
        fig_bar.add_trace(go.Bar(
            x=category_data['Year'],
            y=category_data['Registrations'],
            name=category
        ))
    fig_bar.update_layout(
        title='Yearly Registrations by Category',
        xaxis_title='Year',
        yaxis_title='Registrations',
        barmode='group'
    )
    st.plotly_chart(fig_bar, use_container_width=True)


# raw data view
if st.checkbox('Show Raw Data'):
    st.dataframe(filtered_df.sort_values('Date', ascending=False), use_container_width=True)



# footer
st.markdown("---")
st.markdown("*Data Source: Synthetic data for demonstration purposes*")
