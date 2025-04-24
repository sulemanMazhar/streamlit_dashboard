# 📊 Streamlit Sales Dashboard

An interactive and modular sales analytics dashboard built with **Streamlit** and **Plotly**, powered by clean Python architecture.

---

## 📁 Project Structure

```text
streamlit_dashboard/
├── app.py                  # Main Streamlit entrypoint
├── dashboard/
│   ├── data_loader.py      # Loads and caches CSV data
│   ├── kpi_section.py      # KPI rendering logic
│   ├── charts.py           # Plotly chart rendering
│   └── utils.py            # Data filtering utilities
├── data/
│   └── sales.csv           # Sample dataset
├── requirements.txt        # Python dependencies
└── Dockerfile              # Docker config
```

## 🚀 Features

- 🔍 Filter data by date and category
- 📈 Visualize revenue trends and category breakdowns
- 📊 Display KPIs like total revenue, AOV, and order count
- ✅ Built with modular classes for scalability
- 🐳 Deployable via Docker or run standalone

## 🔧 Prerequisites

- Python 3.8+
- [Streamlit](https://streamlit.io/)
- [Docker](https://www.docker.com/) (optional)

---

## ▶️ Run as a Standalone App

1. **Create a virtual environment** (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Run the app:

```bash
streamlit run app.py
```
Visit http://localhost:8501 to view the dashboard.

## 🐳 Run in Docker
1. **Build the Docker image:**
```bash
docker build -t streamlit-dashboard .
``` 
2. **Run the container:**
```bash
docker run -p 8501:8501 streamlit-dashboard
```

3. **Visit the app in your browser:**
```bash
http://localhost:8501
```

## 📦 Install Additional Dependencies
If you're extending the app, update requirements.txt:
```bash
pip install new-library
pip freeze > requirements.txt
```

