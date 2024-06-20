import numpy as np
import plotly.graph_objs as go
from plotly.subplots import make_subplots

# Parameters
s = 0.2       # Savings rate
alpha = 0.3   # Output elasticity of capital
delta = 0.05  # Depreciation rate
n = 0.01      # Population growth rate
K0 = 100      # Initial capital stock
L0 = 100      # Initial labor
T = 100       # Number of time periods to simulate

def solow_model_simulation(g):
    # Initialize arrays to store the time series of capital, labor, output, and technology
    K = np.zeros(T)
    L = np.zeros(T)
    Y_base = np.zeros(T)
    A = np.zeros(T)
    K[0] = K0
    L[0] = L0
    A[0] = 1

    # Simulation
    for t in range(T-1):
        Y_base[t] = A[t] * K[t]**alpha * L[t]**(1-alpha)  # Production function with technology
        K[t+1] = s * Y_base[t] + (1 - delta) * K[t]  # Capital accumulation
        L[t+1] = (1 + n) * L[t]  # Population growth
        A[t+1] = (1 + g) * A[t]  # Technological growth

    # Output in the last period
    Y_base[T-1] = A[T-1] * K[T-1]**alpha * L[T-1]**(1-alpha)
    
    return K, L, Y_base, A

def create_solow_plot(g_initial=0.02):
    # Create subplots
    fig = make_subplots(rows=2, cols=2, subplot_titles=("Capital Over Time", "Labor Over Time", "Output Over Time", "Technology Over Time"))

    # Initialize with g_initial
    K, L, Y_base, A = solow_model_simulation(g_initial)

    # Add traces
    fig.add_trace(go.Scatter(x=np.arange(T), y=K, mode='lines', name='Capital', line=dict(color='blue')), row=1, col=1)
    fig.add_trace(go.Scatter(x=np.arange(T), y=L, mode='lines', name='Labor', line=dict(color='orange')), row=1, col=2)
    fig.add_trace(go.Scatter(x=np.arange(T), y=Y_base, mode='lines', name='Output', line=dict(color='green')), row=2, col=1)
    fig.add_trace(go.Scatter(x=np.arange(T), y=A, mode='lines', name='Technology', line=dict(color='red')), row=2, col=2)

    # Create sliders
    sliders = [
        {
            "steps": [
                {
                    "args": [
                        [str(g_val)],
                        {
                            "frame": {"duration": 0, "redraw": True},
                            "mode": "immediate",
                            "transition": {"duration": 0}
                        }
                    ],
                    "label": str(g_val),
                    "method": "animate"
                }
                for g_val in np.linspace(0.01, 0.05, 5)
            ],
            "x": 0.1,
            "xanchor": "left",
            "y": -0.15,
            "yanchor": "top",
            "currentvalue": {
                "font": {"size": 20},
                "prefix": "Technological Growth Rate (g): ",
                "visible": True,
                "xanchor": "right"
            },
            "pad": {"b": 10}
        }
    ]

    # Update layout
    fig.update_layout(
        height=600, 
        width=800, 
        title_text="Solow Model Simulation with Technological Growth",
        sliders=sliders
    )

    # Update x and y axes
    fig.update_xaxes(title_text="Time", row=1, col=1)
    fig.update_xaxes(title_text="Time", row=1, col=2)
    fig.update_xaxes(title_text="Time", row=2, col=1)
    fig.update_xaxes(title_text="Time", row=2, col=2)

    fig.update_yaxes(title_text="Capital", row=1, col=1)
    fig.update_yaxes(title_text="Labor", row=1, col=2)
    fig.update_yaxes(title_text="Output", row=2, col=1)
    fig.update_yaxes(title_text="Technology", row=2, col=2)

    # Create animation frames
    frames = [
        go.Frame(
            data=[
                go.Scatter(x=np.arange(T), y=solow_model_simulation(g_val)[0], mode='lines', line=dict(color='blue')),
                go.Scatter(x=np.arange(T), y=solow_model_simulation(g_val)[1], mode='lines', line=dict(color='orange')),
                go.Scatter(x=np.arange(T), y=solow_model_simulation(g_val)[2], mode='lines', line=dict(color='green')),
                go.Scatter(x=np.arange(T), y=solow_model_simulation(g_val)[3], mode='lines', line=dict(color='red'))
            ],
            name=str(g_val)
        )
        for g_val in np.linspace(0.01, 0.05, 5)
    ]

    fig.frames = frames

    fig.show()
