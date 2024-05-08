"""
====================================================================

                         SEC API KEY

85294cd37cab79bfb998150677fb52b9c0daa2682b2c32d2cec15aeeb5da5f4b

======================================================================

{
    "query": "formType:4 AND NOT formType:\"N-4\" AND NOT formType:\"4/A\"",
    "from": "0",
    "size": "10",
    "sort": [{ "filedAt": { "order": "desc" } }]

    'https://api.sec-api.io/insider-trading'

    Query API:https://api.sec-api.io
    Stream API: NEWwss://stream.sec-api.io
}
"""
#PACKAGES
import asyncio
import websockets
import json
import sec_api

def grab_form4s():
    """
    """
    pass









