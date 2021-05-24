import sys
sys.path.append("C:\\Users\\otkin\\dwx_connector\\dwx-zeromq-connector\\v2.0.1\\python\\api")
from DWX_ZeroMQ_Connector_v2_0_1_RC8 import DWX_ZeroMQ_Connector

_zmq = DWX_ZeroMQ_Connector()

# _zmq._DWX_MTX_SUBSCRIBE_MARKETDATA_(DWX_ZeroMQ_Connector, 'EURUSD')
my_trade={
    '_lots':0.05,
    '_SL':250,
    '_TP':750,
    '_comment':'we made a trade!'
}

_zmq._DWX_MTX_NEW_TRADE_(_order=my_trade)

# Notes:
# MQL4 location C:\Users\otkin\AppData\Roaming\MetaQuotes\Terminal\3B534B10135CFEDF8CD1AAB8BD994B13\MQL4
# mql-zmq-master.zip C:\Users\otkin\dwx_connector