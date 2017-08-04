#!/usr/bin/env python

"""
  bittrex_autotrader.py
  Bittrex currency exchange autotrading script in a nutshell.

  Copyright 2017, Marc S. Brooks (https://mbrooks.info)
  Licensed under the MIT license:
  http://www.opensource.org/licenses/mit-license.php

  .. note::
   - This script has been tested to work with Unix-like operating systems
   - This script can be run via cronjob

  .. seealso:: https://bittrex.com/Home/Api
"""

import argparse
import json
import requests
import time

BASE_URL = 'https://bittrex.com/api/v1.1/'

def main():
    """
    Process command-line arguments and initialize trading routines.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-k', '--key')
    parser.add_argument('-s', '--secret')
    args = parser.parse_args()

def sign(key, secret):
    """
    Create the apikey using HMAC-SHA512 signing.

    :param key: Bittrex issued API key.
    :param secret: Bittrex issued API secret.

    :return: string

    .. seealso:: https://www.bittrex.com/Manage#sectionApi
    """
    noonce = int(time.time())

def request(method, params=None):
    """
    Compose a request and send to the Bittrex API.

    :param method: URI resource that references an API service.
    :param params: Object that contains key/value parameters (optional).

    :return: dict
    """
    params = ('?' + params if params else '')

    req = requests.get(BASE_URL + method + params)
    return json.loads(req.text)

def public_markets():
    """
    Get the open and available trading markets along with other meta data.

    :return: dict
    """
    return request('public/getmarkets')

def public_currencies():
    """
    Get all supported currencies along with other meta data.

    :return: dict
    """
    return request('public/getcurrencies')

def public_ticker():
    """
    Get the current tick values for a market.

    :return: dict
    """
    return request('public/getticker')

def public_market_summaries():
    """
    Get the last 24 hour summary of all active exchanges.

    :return: dict
    """
    return request('public/getmarketsummaries')

def public_market_summary(market):
    """
    Get the last 24 hour summary of all active exchanges.

    :param market: String literal (ie. BTC-LTC). If omitted, return all markets.

    :return: dict
    """
    return request('public/getmarketsummary', {
        'market': market
    })

def public_market_history(market):
    """
    Get the latest trades that have occured for a specific market.

    :param market: String literal (ie. BTC-LTC). If omitted, return all markets.

    :return: dict
    """
    return request('public/getmarkethistory', {
        'market': market
    })

def public_order_book(market, book_type):
    """
    Get the orderbook for a given market.

    :param market: String literal (ie. BTC-LTC). If omitted, return all markets.
    :param book_type: buy, sell or both to identify the type of orderbook.

    :return: dict
    """
    return request('public/getorderbook', {
        'market': market,
        'type': book_type
    })

def market_buy_limit(market, quantity, rate):
    """
    Send a buy order in a specific market.

    :param market: String literal (ie. BTC-LTC). If omitted, return all markets.
    :param quantity: The amount to purchase.
    :param rate: Rate at which to place the order.

    :return: dict
    """
    return request('market/buylimit', {
        'market': market,
        'quantity': quantity,
        'rate': rate
    })

def market_sell_limit(market, quantity, rate):
    """
    Send a sell order in a specific market.

    :param market: String literal (ie. BTC-LTC). If omitted, return all markets.
    :param quantity: The amount to sell.
    :param rate: Rate at which to place the order.

    :return: dict
    """
    return request('market/selllimit', {
        'market': market,
        'quantity': quantity,
        'rate': rate
    })

def market_cancel(uuid):
    """
    Send a cancel a buy or sell order.

    :param uuid: UUID of buy or sell order.
    """
    return request('market/cancel', {
        'uuid': uuid
    })

def market_open_orders(market):
    """
    Get all orders that you currently have opened.

    :param market: String literal (ie. BTC-LTC). If omitted, return all markets.

    :return: dict
    """
    return request('market/getopenorders', {
        'market': market
    })

def account_balances():
    """
    Get all balances from your account.

    :return: dict
    """
    return request('account/getbalances')

def account_balance(currency):
    """
    Get the balance from your account for a specific currency.

    :param currency: String literal (ie. BTC). If omitted, return all currency.

    :return: dict
    """
    return request('account/getbalance', {
        'currency': currency
    })

def account_deposit_address(currency):
    """
    Get existing, or generate new address for a specific currency.

    :param currency: String literal (ie. BTC). If omitted, return all currency.

    :return: dict
    """
    return request('account/getdepositaddress', {
        'currency': currency
    })

def account_withdraw(currency, quantity, address, paymentid):
    """
    Send request to withdraw funds from your account.

    :param currency: String literal (ie. BTC). If omitted, return all currency.
    :param quantity: The amount to withdrawl.
    :param address: The address where to send the funds.
    :param paymentid: CryptoNotes/BitShareX/Nxt field (memo/paymentid optional).

    :return: dict
    """
    return request('account/getwithdraw', {
        'currency': currency,
        'quantity': quantity,
        'address': address,
        'paymentid': paymentid
    })

def account_order(uuid):
    """
    Get a single order by uuid.

    :param uuid: UUID of buy or sell order.

    :return: dict
    """
    return request('account/getorder', {
        'uuid': uuid
    })

def account_order_history(market):
    """
    Get order history.

    :param market: String literal (ie. BTC-LTC). If omitted, return all markets.

    :return: dict
    """
    return request('account/getorderhistory', {
        'market': market
    })

def account_deposit_history(currency):
    """
    Get deposit history.

    :param currency: String literal (ie. BTC). If omitted, return all currency.

    :return: dict
    """
    return request('account/getdeposithistory', {
        'currency': currency
    })

def account_withdrawl_history(currency):
    """
    Get withdrawl history.

    :param currency: String literal (ie. BTC). If omitted, return all currency.

    :return: dict
    """
    return request('account/getwithdrawlhistory', {
        'currency': currency
    })

if __name__ == '__main__':
    main()
