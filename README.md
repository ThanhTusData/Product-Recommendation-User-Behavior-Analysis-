
# 🛒 E-commerce Recommender System & Business Analytics

This project analyzes customer behavior and purchasing patterns in an e-commerce dataset to deliver insights and build a product recommender system. It includes collaborative filtering modeling and dashboards to support strategic decisions.

---

## 🎯 Project Objectives

- Understand customer purchase trends and fulfillment performance.
- Identify business opportunities for cross-selling, regional growth, and process optimization.
- Build a **Matrix Factorization** + **KNN-based recommender system**.
- Visualize performance and insights using Power BI.

---

## 🗂️ Project Structure

```plaintext
E-commerce/
│
├── data/                          # Cleaned and raw datasets
├── models/                        # Trained recommender system artifacts
├── mf_knn_recommender.py         # Core recommendation engine using MF + KNN
├── test_with_user.py             # User-based recommendation simulation script
├── model_training.log            # Training log output for monitoring
├── notebook.ipynb                # EDA, preprocessing, training walkthrough
├── Dashboards.pbix               # Power BI dashboard with visual insights
└── README.md                     # Project documentation
```

---

## 📊 Key Business Insights from EDA

### ✅ High Order Completion Rate (~97.9%)
> Most orders are delivered successfully. The "processing" orders, although small, show high costs and poor reviews.
🔧 Action: Investigate and improve processing orders to optimize expense and customer satisfaction.

### 📍 Geographic Concentration
> São Paulo dominates in both buyers (>40%) and sellers (>70%).
🔧 Action: Target **under-represented regions** for growth and marketing expansion.

### 📦 Single-Item Order Pattern
> ~93% of orders contain just one product (avg = 1.10 items).
🔧 Action: Create **multi-item bundles** and upsell campaigns to increase order value.

### 🧾 Product Category & Pricing
> High-ticket categories like computers have higher item & shipping prices; fashion is lightweight and cheaper.
🔧 Action: Adjust pricing/shipping strategies by product type for optimal margins and user satisfaction.

### 💳 Payment Behavior
> Credit cards lead (78%), boleto (20%), and debit cards (1.6%). “not_defined” category brings poor value.
🔧 Action: Investigate undefined methods and refine payment option offerings.

### 🎟️ Low Voucher Usage
> Only 2.3% of orders use vouchers; little impact on satisfaction or value.
🔧 Action: Redesign voucher strategy—consider minimum spend, time-based deals, or personalized targeting.

### 📅 Temporal Trends & Data Gaps
> Pre-March 2017 data is unstable. Post-2017 is clean and useful, with key events around mid-2018.
🔧 Action: Focus on post-2017 data and align peaks with business events or campaigns.

---

## 🔁 Project Workflow

1. **Data Preparation**: Load and clean data from `data/`, handle missing values, and remove unstable records.
2. **Exploratory Data Analysis (EDA)**: Extract patterns and trends using `notebook.ipynb`.
3. **Recommender Model**: Matrix Factorization with KNN built in `mf_knn_recommender.py`.
4. **Testing**: Simulate recommendations using `test_with_user.py`.
5. **Visualization**: Present insights in `Dashboards.pbix` for business decisions.

---

## 🧠 Future Enhancements

- Integrate content-based and hybrid recommendation models.
- Personalize bundles using user behavior clustering.
- A/B test voucher strategies in live environments.
- Add Streamlit or Flask-based web interface for real-time recommendations.

---

## 📬 Contact

For collaboration or feedback, please reach out or contribute via GitHub.
