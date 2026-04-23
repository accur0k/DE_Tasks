import json
from pathlib import Path

import pandas as pd
import streamlit as st

st.set_page_config(page_title="Task 4 Data Dashboard", layout="wide")

RESULTS_FILE = Path(__file__).parent / "output" / "results.json"

if not RESULTS_FILE.exists():
    st.error("output/results.json not found. Run the notebook first.")
    st.stop()

results = json.loads(RESULTS_FILE.read_text(encoding="utf-8"))

st.title("Task 4 Data Dashboard")
st.caption("Source: output/results.json")

for tab, (name, data) in zip(st.tabs(list(results)), results.items()):
    with tab:
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Unique users", f"{data['unique_users']:,}")
        c2.metric("Unique author sets", f"{data['unique_author_sets']:,}")
        c3.metric("Most popular author(s)", ", ".join(data["most_popular_authors"]))
        c4.metric("Best buyer total", f"${data['best_buyer_total_spent']:,.2f}")

        left, right = st.columns([1, 2])

        with left:
            st.markdown("#### Top 5 days by revenue")
            st.dataframe(
                pd.DataFrame(data["top_5_days_by_revenue"]),
                hide_index=True,
                use_container_width=True,
                column_config={
                    "date": "Date",
                    "revenue": st.column_config.NumberColumn("Revenue", format="$%.2f"),
                },
            )
            st.markdown("#### Best buyer IDs")
            st.write(data["best_buyer_ids"])

        with right:
            st.markdown("#### Daily revenue")
            chart = pd.DataFrame(data["daily_revenue"])
            chart["date"] = pd.to_datetime(chart["date"])
            st.line_chart(chart, x="date", y="revenue", use_container_width=True)