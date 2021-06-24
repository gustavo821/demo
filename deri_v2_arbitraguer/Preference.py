import os
import json
import logging
from decimal import Decimal

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s.%(msecs)03d] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers = [
        logging.StreamHandler(),
        logging.FileHandler('Logs.log')
    ]
)

DIR_ABIS = 'Abis'
os.makedirs(DIR_ABIS, exist_ok=True)

ONE = 10**18
ZERO_ADDRESS = '0x0000000000000000000000000000000000000000'

RPCS = {
    'bsc': [

    ]
}

ARBITRAGUERS_V2 = [
    {
        'defiNetwork': '',
        'defiPoolAddress':  '',
        'defiPoolRouterAddress': '',
        'defiPoolPTokenAddress': '',
        'defiAccount': '',
        'defiPrivate': '',
        'defiSymbolId': 0,
        'defiMultiplier': ,
        'defiMinVolume': ,
        'defiMaxVolume': ,

        'cefiExchange': '',
        'cefiUrl': '',
        'cefiKey': '',
        'cefiSecret': '',
        'cefiSymbol': '',
        'cefiMiltiplier': ,
        'cefiMinVolume': ,
    },
    {
        'defiNetwork': '',
        'defiPoolAddress':  '',
        'defiPoolRouterAddress': '',
        'defiPoolPTokenAddress': '',
        'defiAccount': '',
        'defiPrivate': '',
        'defiSymbolId': 1,
        'defiMultiplier': ,
        'defiMinVolume': ,
        'defiMaxVolume': ,

        'cefiExchange': '',
        'cefiUrl': '',
        'cefiKey': '',
        'cefiSecret': '',
        'cefiSymbol': '',
        'cefiMiltiplier': ,
        'cefiMinVolume': ,
    }
]
