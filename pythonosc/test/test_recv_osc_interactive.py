#!/usr/bin/env python3

from collections import Iterable
import socket
from enum import IntEnum

from pythonosc import osc_message_builder
from pythonosc import dispatcher
from pythonosc import osc_server
from pythonosc import osc_server_tcp
import threading
import time
from pythonosc import osc_message_builder
from pythonosc import udp_client
from pythonosc import dispatcher
from pythonosc import osc_server

# same values as liblo
class TransportProto(IntEnum):
    TCP = 4
    UDP = 1
    UNIX = 2


OSC_PROTO = TransportProto.UDP
OSC_PROTO = TransportProto.TCP

ip = "0.0.0.0"
port = 5555

def recv_osc(*args):
    print("recv: %s" % (" ".join([str(arg) for arg in args])))

if __name__ == '__main__':
    disp = dispatcher.Dispatcher()
    disp.set_default_handler(recv_osc)

    if OSC_PROTO == TransportProto.TCP:
        server = osc_server_tcp.OSCTCPServer((ip, port), disp)
    elif OSC_PROTO == TransportProto.UDP:
        server = osc_server.OSCUDPServer((ip, port), disp)
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.setDaemon(True)
    server_thread.start()

    print("Listening for OSC on tcp port %i" % port)
    while True:
        time.sleep(1)
