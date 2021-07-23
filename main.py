import cryptocompare
import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib.animation import FuncAnimation

def get_crypto_price(cryptocurrency, currency):
    return cryptocompare.get_price(cryptocurrency, currency)[cryptocurrency][currency]

def get_crypto_name(cryptocurrency):
    return cryptocompare.get_coin_list()[cryptocurrency]['FullName']

plt.style.use('seaborn')

x_vals = []
y_vals = []

# Animate Function
def animate(i):
    x_vals.append(datetime.now())
    y_vals.append(get_crypto_price('BTC', 'USD'))

    plt.cla()

    # Specify plot title
    plt.title(get_crypto_name('BTC') + ' Price Live Plotting')
    plt.gcf().canvas.set_window_title('Live Plotting Cryptocurrency')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')

    # Actual Plotting
    plt.plot_date(x_vals, y_vals, linestyle="solid", ms=0)
    plt.tight_layout()

# Call Animate Function (Every sec)
ani = FuncAnimation(plt.gcf(), animate, interval=1000)

# Show the Plot
plt.show()
