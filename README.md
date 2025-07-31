# SnowPilot
---

**SnowPilot** is an interactive Streamlit application for querying insurance prices, vehicle data, and analytics using Snowflake as the backend. It leverages OpenAI for conversational SQL generation, enabling users to ask natural language questions and receive results, visualizations, and insurance price computations for vehicles.

## Features

- **Conversational SQL Assistant**: Ask questions about insurance pricing, vehicle risk, VIN details, and more. SnowPilot generates and executes Snowflake SQL queries via OpenAI’s API.
- **Insurance Price Quotation**: Calculate basic insurance price based on car model, manufacture year, and distance traveled.
- **Data Visualization**: Generate bar charts, line charts, scatter plots, pie charts, and 3D plots from query results.
- **FAQ Sidebar**: Quick-access queries for common insurance and vehicle questions.
- **VIN(Vehicle Identification Number) Validation**: Checks VIN format and database presence, provides feedback or pricing options.
- **Extensible Prompts**: Custom prompt logic for Snowflake SQL generation, table/column context, and strict rules to ensure SQL safety and relevance.

## Getting Started

1. **Install Dependencies**
   ```bash
   pip install streamlit openai snowflake-snowpark-python pandas plotly altair streamlit-option-menu
   ```
2. **Configure Snowflake Connection**
   - Edit `config.py` with your Snowflake connection details:
     ```python
     conn_params = {
         "account": "...",
         "user": "...",
         "password": "...",
         "database": "...",
         "db_schema": "...",
         ...
     }
     ```
   - Add your OpenAI API key to Streamlit secrets:
     ```
     [secrets]
     api_key = "sk-..."
     ```

3. **Run the Application**
   ```bash
   streamlit run app.py
   ```

## How It Works

- On startup, SnowPilot loads insurance table metadata from Snowflake and sets up the OpenAI prompt (see `prompts.py`).
- Users interact via chat or sidebar FAQs; their queries are converted to SQL and executed on the Snowflake backend.
- Results are displayed as tables or interactive charts using Plotly and Altair.
- The Insurance Price Quotation page computes basic prices based on user selections and vehicle age.

## Example Queries

- “Show me Insurance Price for ‘Vehicle Number’”
- “Tell me the VIN numbers of vehicles with an age greater than 5 years.”
- “Show me Risky Vehicles based on Driving pattern”

## Customization

You can extend `prompts.py` to add new prompt rules or table context, or modify `test_price.py` for different pricing logic.

---

Let me know if you want to add installation screenshots, data samples, or any usage tips!
