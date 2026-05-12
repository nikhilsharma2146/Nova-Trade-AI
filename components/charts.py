import plotly.graph_objects as go

def plot_candlestick(df, title="Stock Price"):
    fig = go.Figure(data=[go.Candlestick(x=df.index,
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close'],
                increasing_line_color='#10b981', 
                decreasing_line_color='#ef4444')])

    fig.update_layout(
        title=dict(text=title, font=dict(color='#f8fafc', size=16)),
        template="plotly_dark",
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=10, r=10, t=40, b=10),
        height=650, # Massive height for terminal feel
        xaxis_rangeslider_visible=False,
        xaxis=dict(
            showgrid=False, color='#94a3b8', 
            showspikes=True, spikemode='across', spikesnap='cursor', spikecolor='#f8fafc', spikethickness=1
        ),
        yaxis=dict(
            showgrid=True, gridcolor='rgba(255,255,255,0.05)', color='#94a3b8',
            showspikes=True, spikemode='across', spikesnap='cursor', spikecolor='#f8fafc', spikethickness=1,
            side='right' # Price scale on right side like pro terminals
        ),
        hovermode="x unified"
    )
    return fig

def plot_line_chart(df, title="Trend"):
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df.index, 
        y=df['Close'], 
        mode='lines', 
        line=dict(color='#0ea5e9', width=3),
        fill='tozeroy',
        fillcolor='rgba(14, 165, 233, 0.1)'
    ))
    fig.update_layout(
        title=dict(text=title, font=dict(color='#f8fafc', size=16)),
        template="plotly_dark",
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=10, r=10, t=40, b=10),
        height=650,
        xaxis=dict(
            showgrid=False, color='#94a3b8',
            showspikes=True, spikemode='across', spikesnap='cursor', spikecolor='#f8fafc', spikethickness=1
        ),
        yaxis=dict(
            showgrid=True, gridcolor='rgba(255,255,255,0.05)', color='#94a3b8',
            showspikes=True, spikemode='across', spikesnap='cursor', spikecolor='#f8fafc', spikethickness=1,
            side='right'
        ),
        hovermode="x unified"
    )
    return fig
