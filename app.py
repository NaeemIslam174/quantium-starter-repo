import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc, Input, Output

# ---------- Data ----------
df = pd.read_csv("formatted_sales_data.csv")
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

# ---------- Styles ----------
COLORS = {
    "background": "#fdf2f8",   # soft pink
    "card": "#ffffff",
    "primary": "#be185d",      # deep pink
    "text": "#1f2937",         # dark grey
    "accent": "#9d174d",
}

app_style = {
    "backgroundColor": COLORS["background"],
    "minHeight": "100vh",
    "fontFamily": "'Segoe UI', Tahoma, sans-serif",
    "padding": "40px",
    "color": COLORS["text"],
}

card_style = {
    "backgroundColor": COLORS["card"],
    "borderRadius": "12px",
    "padding": "30px",
    "maxWidth": "1100px",
    "margin": "0 auto",
    "boxShadow": "0 4px 20px rgba(0, 0, 0, 0.08)",
}

header_style = {
    "textAlign": "center",
    "color": COLORS["primary"],
    "marginBottom": "10px",
    "fontSize": "32px",
}

subheader_style = {
    "textAlign": "center",
    "color": COLORS["text"],
    "marginBottom": "30px",
    "fontWeight": "normal",
}

radio_style = {
    "display": "flex",
    "justifyContent": "center",
    "gap": "20px",
    "marginBottom": "20px",
    "fontSize": "16px",
}

# ---------- App ----------
app = Dash(__name__)

app.layout = html.Div(style=app_style, children=[
    html.Div(style=card_style, children=[
        html.H1("Soul Foods — Pink Morsel Sales Visualiser", id="header", style=header_style),
        html.H3("Filter by region to see how sales changed before and after the price increase",
                style=subheader_style),
        dcc.RadioItems(
            id="region-filter",
            options=[
                {"label": "North", "value": "north"},
                {"label": "East",  "value": "east"},
                {"label": "South", "value": "south"},
                {"label": "West",  "value": "west"},
                {"label": "All",   "value": "all"},
            ],
            value="all",
            inline=True,
            style=radio_style,
            inputStyle={"marginRight": "6px", "accentColor": COLORS["primary"]},
            labelStyle={"marginRight": "15px", "cursor": "pointer"},
        ),
        dcc.Graph(id="sales-line-chart"),
    ]),
])

# ---------- Callback ----------
@app.callback(
    Output("sales-line-chart", "figure"),
    Input("region-filter", "value"),
)
def update_chart(region):
    filtered = df if region == "all" else df[df["region"] == region]

    fig = px.line(filtered, x="date", y="sales",
                  title=f"Pink Morsel Sales — {region.capitalize()} Region",
                  labels={"date": "Date", "sales": "Sales ($)"})

    fig.update_traces(line_color=COLORS["primary"])
    fig.add_vline(x=pd.Timestamp("2021-01-15").timestamp() * 1000,
                  line_dash="dash", line_color=COLORS["accent"],
                  annotation_text="Price increase",
                  annotation_position="top right")
    fig.update_layout(plot_bgcolor="white", paper_bgcolor="white",
                      title_x=0.5, title_font_size=20)
    return fig

if __name__ == "__main__":
    app.run(debug=True)