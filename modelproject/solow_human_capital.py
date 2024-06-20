**Solow model with technological growth and human capital - Long run equlibrium**

import numpy as np
import matplotlib.pyplot as plt


def plot_solow_model():
    # Parameters for Technological Growth
    s_tech = 0.2       # Savings rate
    alpha_tech = 0.3   # Output elasticity of capital
    delta_tech = 0.05  # Depreciation rate
    n_tech = 0.01      # Population growth rate
    g_tech = 0.02      # Technological growth rate


    # Parameters for Human Capital
    s_hum = 0.2        # Savings rate
    alpha_hum = 0.3    # Output elasticity of capital
    delta_hum = 0.05   # Depreciation rate
    n_hum = 0.01       # Population growth rate
    g_hum = 0.02       # Technological growth rate
    h_hum = 1.2        # Average human capital per worker


    # Capital per effective worker (k)
    k = np.linspace(0, 10, 100)


    # Output per effective worker (y) for Technological Growth
    y_tech = k ** alpha_tech


    # Investment per effective worker (i) for Technological Growth
    i_tech = s_tech * y_tech


    # Depreciation line for Technological Growth
    dep_tech = (n_tech + g_tech + delta_tech) * k


    # Steady state k* for Technological Growth
    k_star_tech = (s_tech / (n_tech + g_tech + delta_tech)) ** (1 / (1 - alpha_tech))


    # Output per effective worker (y) for Human Capital
    y_hum = (k ** alpha_hum) * (h_hum ** (1 - alpha_hum))


    # Investment per effective worker (i) for Human Capital
    i_hum = s_hum * y_hum


    # Depreciation line for Human Capital
    dep_hum = (n_hum + g_hum + delta_hum) * k


    # Steady state k* for Human Capital
    k_star_hum = ((s_hum * (h_hum ** (1 - alpha_hum))) / (n_hum + g_hum + delta_hum)) ** (1 / (1 - alpha_hum))


    # Plotting the diagram
    plt.figure(figsize=(10, 6))


    # Plot for Technological Growth
    plt.plot(k, i_tech, label='Capital accumulation per effective worker (Tech Growth)', color='blue')
    plt.axvline(x=k_star_tech, color='green', linestyle='--', label=f'Steady State k* (Tech Growth) = {k_star_tech:.2f}')
    plt.scatter([k_star_tech], [s_tech * (k_star_tech ** alpha_tech)], color='black')  # Steady state point (Tech Growth)


    # Plot for Human Capital
    plt.plot(k, i_hum, label='Capital accumulation per effective worker (Human Capital)', color='purple')
    plt.axvline(x=k_star_hum, color='brown', linestyle='--', label=f'Steady State k* (Human Capital) = {k_star_hum:.2f}')
    plt.scatter([k_star_hum], [s_hum * (k_star_hum ** alpha_hum) * (h_hum ** (1 - alpha_hum))], color='black')  # Steady state point (Human Capital)
    plt.plot(k, dep_hum, label='45° line', color='orange')


    # Titles and labels
    plt.title('Solow Model with Technological Growth and Human Capital - Long Run Equilibrium')
    plt.xlabel('Capital per Effective Worker (k)')
    plt.ylabel('Investment per Effective Worker')
    plt.legend()
    plt.grid(True)
    plt.show()


# Uncomment the lines below to execute when running the script directly
# if __name__ == "__main__":
#     plot_solow_model()
