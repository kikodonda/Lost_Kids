import BTC_ETH_Gen
import os
import numpy as np
import threading
import multiprocessing
from multiprocessing import Process

print("Cargando direcciones Bitcoins ...")
BTC_Array = np.loadtxt("BTC_PSKP.txt", dtype=str)
arr = BTC_Array
# print(BTC_Array)
print(len(BTC_Array))
print("Carga BTC terminada.")

# print("Cargando direcciones Ethereum ...")
# eth_arr = np.loadtxt("ETH_Address.txt", dtype=str)
# print(len(eth_arr))
# print("Carga ETH terminada.")


def binary_search(arr, x, n):
    lo = 0
    hi = n - 1
    mid = 0

    while lo <= hi:
        mid = (hi + lo) // 2
        if arr[mid] < x:
            lo = mid + 1
        elif arr[mid] > x:
            hi = mid - 1
        else:
            return mid
    return -1


# def binary_search_eth(eth_arr, x, n):
#     lo = 0
#     hi = n - 1
#     mid = 0
#
#     while lo <= hi:
#         mid = (hi + lo) // 2
#         if eth_arr[mid] < x:
#             lo = mid + 1
#         elif eth_arr[mid] > x:
#             hi = mid - 1
#         else:
#             return mid
#     return -1


def loop():
    while True:

        kg = BTC_ETH_Gen.KeyGenerator()
        kg.seed_input('Truly random string. I rolled a dice and got 4.')
        key = kg.generate_key()
        # print(key)

        btc_address = BTC_ETH_Gen.BitcoinWallet.generate_address(key)
        # print(btc_address)
        arr = BTC_Array
        x = btc_address
        n = len(arr)
        result = binary_search(arr, x, n)
        if result == -1:
            print("BTC: ", btc_address, "-", key, "Clave no encontrada")
        else:
            print("Elemento esta presente en el indice", str(result))
            print(btc_address, "-", key, " Clave Encontrada")
            with open('Btc_Wallets.txt', 'a') as f:
                f.write(btc_address)
                f.write(', ')
                f.write(key)
                f.write('\n')
                f.close()
                print('Felicidades lo has encontrado ')
                time.sleep(30)

        # eth_address = BTC_ETH_Gen.EthereumWallet.generate_address(key)
        # e = eth_address
        # n = len(eth_arr)
        # result = binary_search_eth(eth_arr, e, n)
        # if result == -1:
        #     print("ETH: ", eth_address, "-", key, "Clave no encontrada")
        # else:
        #     print("Elemento esta presente en el indice", str(result))
        #     print(eth_address, "-", key, " Clave Encontrada")
        #     with open('Eth_Wallets.txt', 'a') as f:
        #         f.write(eth_address)
        #         f.write(', ')
        #         f.write(key)
        #         f.write('\n')
        #         f.close()
        #         print('Felicidades lo has encontrado ')
        #         time.sleep(30)


if __name__ == '__main__':
    for i in range(multiprocessing.cpu_count()):
        t = Process(target=loop)
        t.start()


# bitcoin
# bitcoin-abc
# bitcoin-cash
# bitcoin-sv
# dashcore
# dogecoin
# litecoin
# zcash
