# Vehicle Registration Dashboard

An interactive dashboard for analyzing vehicle registration data with an investor's perspective. This dashboard provides insights into vehicle registration trends, year-over-year (YoY) and quarter-over-quarter (QoQ) growth rates, and manufacturer performance.

## 🎯 Project Overview

This dashboard is designed to help investors analyze vehicle registration trends across different categories (2W/3W/4W) and manufacturers. It provides:
- Real-time visualization of registration trends
- YoY and QoQ growth analysis
- Manufacturer performance metrics
- Interactive filtering and data exploration

## ✅ Requirements Met

### Data Source
- [x] Uses vehicle registration data (currently synthetic data simulating Vahan Dashboard)
- [x] Focuses on vehicle types: 2W (Two-Wheelers), 3W (Three-Wheelers), 4W (Four-Wheelers)
- [x] Includes manufacturer-wise registration data

### Key Features
- [x] **Growth Metrics**
  - YoY (Year-over-Year) growth calculations
  - QoQ (Quarter-over-Quarter) growth calculations
  - Category-wise and manufacturer-wise analysis

- [x] **Interactive UI**
  - Date range selection
  - Vehicle category filters
  - Manufacturer filters
  - Responsive design for different screen sizes

- [x] **Visualizations**
  - Time series trends
  - Category distribution (pie chart)
  - Yearly comparison (bar chart)
  - Data table with sorting capabilities

### Technical Implementation
- [x] Built with Python and Streamlit
- [x] Modular code structure
- [x] Version controlled with Git
- [x] Comprehensive documentation

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd vehicle-dashboard
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```

2. Open your web browser and navigate to the URL shown in the terminal (usually http://localhost:8501)

3. Use the sidebar to:
   - Select date range for analysis
   - Filter by vehicle categories (2W/3W/4W)
   - Filter by specific manufacturers

## 📊 Data Insights

### Key Observations
1. **Market Trends**
   - 2W (Two-Wheelers) dominate the market share
   - 4W (Four-Wheelers) show the highest growth rate
   - Seasonal patterns in registrations (higher in Q4)

2. **Manufacturer Performance**
   - Top performers in each category
   - Emerging manufacturers with high growth rates
   - Market share distribution

3. **Investment Opportunities**
   - Fastest growing vehicle segments
   - Manufacturers with increasing market share
   - Seasonal investment opportunities

## 🔄 Data Source Integration

### Current Implementation
- Uses synthetic data that simulates real-world patterns
- Data structure mimics Vahan Dashboard's format
- Easy to replace with actual API integration

#### About the Sample Data
The dashboard currently uses programmatically generated sample data that includes:
- **Time Period**: 5 years of monthly data up to current date
- **Vehicle Categories**:
  - 2W (Two-Wheelers): Hero, Honda, Bajaj, TVS, Royal Enfield
  - 3W (Three-Wheelers): Bajaj, Piaggio, Mahindra, TVS
  - 4W (Four-Wheelers): Maruti, Hyundai, Tata, Mahindra, Toyota, Honda
- **Data Points**:
  - Base registration numbers with realistic growth patterns
  - Annual growth rate: ~10%
  - Quarterly variations: ~2%
  - Manufacturer-specific variations

### Connecting to Vahan Dashboard
To connect to the actual Vahan Dashboard:
1. Obtain API credentials
2. Update the data loading functions in `app.py`
3. Add credentials to `.env` file (not included in version control)

## 📈 Feature Roadmap

### Short-term
- [ ] Connect to real Vahan Dashboard API
- [ ] Add export functionality for reports
- [ ] Include regional analysis

### Long-term
- [ ] Implement user authentication
- [ ] Add forecasting capabilities
- [ ] Create investor alert system
- [ ] Add competitive analysis features

## 📂 Project Structure

```
vehicle-dashboard/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
└── data/               # Data directory (for future use)
    └── sample_data.py  # Sample data generation
```

## 📝 Data Assumptions

1. **Data Format**
   - Monthly registration data
   - Consistent categories: 2W, 3W, 4W
   - Standard manufacturer names

2. **Growth Calculations**
   - YoY compares same months across years
   - QoQ compares consecutive quarters
   - Growth rates are percentage changes

## 📹 Video Walkthrough

[Link to video walkthrough will be added here]

## 📄 License

This project is open source and available under the MIT License.

## 📬 Contact

For any questions or feedback, please open an issue in the repository.
