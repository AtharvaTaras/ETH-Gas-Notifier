from time import sleep
from pushbullet import Pushbullet
import requests

PUSH_API = "Your PushBullet API KEY goes here"
ETH_API = "Your Etherscan API KEY goes here"
URL = "https://api.etherscan.io/api?module=gastracker&action=gasoracle&apikey=ETH_API"

interval = 1
gas_limit = 75

def get_data():
    global gas

    try:
        response = requests.get(URL)
        data = response.json()

        gas = float(data['result']['SafeGasPrice'])

    except:
        print('Error')
        sleep(1)


def compare():
    global gas

    try:
        if gas <= gas_limit:
            gas = str(gas)
            notify = "Current gas price is "
            notify = notify + gas
            print(notify)

            pb = Pushbullet(PUSH_API)
            push = pb.push_note('Gas Price Changed', notify)

    except:
        print('Error.')
        sleep(1)


while True:
    get_data()
    compare()
    sleep(interval)
