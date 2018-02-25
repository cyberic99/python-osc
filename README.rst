==========
python-osc
==========

Open Sound Control server and client implementations in **pure python** (3.4+).

Friendly WIP fork of https://github.com/attwad/python-osc

Current issues:

- verify_request() always returns True

- asyncio stuff not tested (asyncio.DatagramProtocol => asyncio.Protocol) ...

- the new file is named osc_server_tcp.py... should we rename osc_server.py => osc_udp_server.py ?

- maybe use the same def _call_handlers_for_packet(data, dispatcher) for UDP and TCP
