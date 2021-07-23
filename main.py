import cryptocompare
import matplotlib.pyplot as plt

def get_crypto_price(cryptocurrency, currency):
    return cryptocompare.get_price(cryptocurrency, currency)[cryptocurrency][currency]

def get_crypto_name(cryptocurrency):
    return cryptocompare.get_coin_list()[cryptocurrency]['FullName']

print(get_crypto_price('BTC', 'USD'))
print(get_crypto_name('ETH'))

