# 🛒 Sales Data Analysis

## 📌 Project Overview
This project analyzes a sales dataset to uncover trends, category performance, and distribution insights.  
The analysis was done in **Python** using **pandas**, **matplotlib**, and **seaborn** within Jupyter Notebook.

---

## 📊 Key Objectives
- Explore and clean the dataset.  
- Generate summary statistics.  
- Visualize sales performance over time.  
- Compare sales across product categories.  
- Highlight trends, patterns, and actionable insights.  

---

## 📂 Project Structure
.
├── onlinesales.csv# Dataset file (CSV)
├── notebook.ipynb # Main Jupyter Notebook with analysis
├── requirements.txt # Python dependencies
└── README.md # Project documentation

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/sales-analysis.git
cd sales-analysis
2. Create a virtual environment (recommended)
bash
Copy code
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
3. Install dependencies
bash
Copy code
pip install -r requirements.txt
4. Run Jupyter Notebook
bash
Copy code
jupyter notebook
📈 Sample Visualizations
Line Chart: Units Sold over Time

Bar Plot: Average Revenue per Product Category

Histogram: Distribution of Revenue

Scatter plot: Correlations Region and Units sold 

📝 Findings / Observations
Trends over time
Units sold were almost constant in the first 4 months with a peak in March, followed by a slight dip in May–December.

Differences across categories

Electronics consistently outperformed other categories in terms of average sales.
Books had the lowest average sales among all product groups.
Distribution insights

The histogram of Units sold shows a left-skewed distribution, meaning most unit sold are large numbers, but a few very same numbers pull the average downward.
Correlations between variables

Scatter plot of Regions vs Units Sold Asia has the highest sales, followed by North America then Europe.
General insight
This analysis suggests that focusing on electronics and addressing the seasonal dip could improve overall revenue performance.
🚀 Tech Stack
Python 

Pandas

Matplotlib

Seaborn

Jupyter Notebook
