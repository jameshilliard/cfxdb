##############################################################################
#
#                        Crossbar.io Database
#     Copyright (c) Crossbar.io Technologies GmbH. Licensed under MIT.
#
##############################################################################

import pytest
import random
import uuid
import timeit

import flatbuffers
import numpy as np

from txaio import with_twisted, time_ns  # noqa

from autobahn import util
from autobahn.wamp.types import TransportDetails
from cfxdb.realmstore import AppSession

DATA1 = {
    'authextra': {
        'transport': {
            'channel_framing':
            'websocket',
            'channel_id': {},
            'channel_serializer':
            None,
            'channel_type':
            'tcp',
            'http_cbtid':
            'ch0oFqC4EQMCqpYmj/78bQ5D',
            'http_headers_received': {
                'cache-control': 'no-cache',
                'connection': 'Upgrade',
                'host': 'localhost:8080',
                'pragma': 'no-cache',
                'sec-websocket-extensions': 'permessage-deflate; '
                'client_no_context_takeover; '
                'client_max_window_bits',
                'sec-websocket-key': 'FG9K1Vx44MqEE9c37YgPEw==',
                'sec-websocket-protocol': 'wamp.2.json',
                'sec-websocket-version': '13',
                'upgrade': 'WebSocket',
                'user-agent': 'AutobahnPython/22.4.1.dev7'
            },
            'http_headers_sent': {
                'Set-Cookie': 'cbtid=ch0oFqC4EQMCqpYmj/78bQ5D;max-age=604800'
            },
            'is_secure':
            False,
            'is_server':
            True,
            'own':
            None,
            'own_fd':
            -1,
            'own_pid':
            28806,
            'own_tid':
            28806,
            'peer':
            'tcp4:127.0.0.1:48812',
            'peer_cert':
            None,
            'websocket_extensions_in_use': [{
                'client_max_window_bits': 13,
                'client_no_context_takeover': False,
                'extension': 'permessage-deflate',
                'is_server': True,
                'mem_level': 5,
                'server_max_window_bits': 13,
                'server_no_context_takeover': False
            }],
            'websocket_protocol':
            'wamp.2.json'
        },
        'x_cb_node': 'intel-nuci7-28788',
        'x_cb_peer': 'unix',
        'x_cb_pid': 28797,
        'x_cb_worker': 'test_router1'
    },
    'authid': 'client1',
    'authmethod': 'anonymous-proxy',
    'authprovider': 'static',
    'authrole': 'frontend',
    'session': 941369063710961,
    'transport': {
        'channel_framing': 'rawsocket',
        'channel_id': {},
        'channel_serializer': 'cbor',
        'channel_type': 'tcp',
        'http_cbtid': None,
        'http_headers_received': None,
        'http_headers_sent': None,
        'is_secure': False,
        'is_server': None,
        'own': None,
        'own_fd': -1,
        'own_pid': 28797,
        'own_tid': 28797,
        'peer': 'unix',
        'peer_cert': None,
        'websocket_extensions_in_use': None,
        'websocket_protocol': 'wamp.2.cbor'
    }
}


def fill_app_session(app_session):
    _td1 = TransportDetails.parse(DATA1['transport'])
    _td2 = TransportDetails.parse(DATA1['authextra']['transport'])

    app_session.arealm_oid = uuid.uuid4()
    app_session.oid = uuid.uuid4()
    app_session.session = util.id()
    app_session.joined_at = np.datetime64(time_ns() - 723 * 10**9, 'ns')
    app_session.left_at = np.datetime64(time_ns(), 'ns')
    app_session.node_oid = uuid.uuid4()
    app_session.node_authid = 'intel-nuci7'
    app_session.worker_name = 'router1'
    app_session.worker_pid = 28797
    app_session.transport = _td1.marshal()
    app_session.realm = 'realm-{}'.format(uuid.uuid4())
    app_session.authid = util.generate_serial_number()
    app_session.authrole = random.choice(['admin', 'user*', 'guest', 'anon*'])
    app_session.authmethod = random.choice(['wampcra', 'cookie', 'anonymous-proxy'])
    app_session.authprovider = random.choice(['static', 'dynamic'])
    app_session.authextra = {
        'transport': _td2.marshal(),
        'x_cb_node': DATA1['authextra'].get('x_cb_node', None),
        'x_cb_peer': DATA1['authextra'].get('x_cb_peer', None),
        'x_cb_pid': DATA1['authextra'].get('x_cb_pid', None),
        'x_cb_worker': DATA1['authextra'].get('x_cb_worker', None),
    }


@pytest.fixture(scope='function')
def builder():
    _builder = flatbuffers.Builder(0)
    return _builder


@pytest.fixture(scope='function')
def app_session():
    _app_session = AppSession()
    fill_app_session(_app_session)
    return _app_session


def test_app_session_roundtrip(app_session, builder):
    # serialize to bytes (flatbuffers) from python object
    obj = app_session.build(builder)
    builder.Finish(obj)
    data = builder.Output()
    assert len(data) in [1584, 1592]

    # create python object from bytes (flatbuffers)
    _app_session = AppSession.cast(data)

    assert _app_session.arealm_oid == app_session.arealm_oid
    assert _app_session.oid == app_session.oid
    assert _app_session.session == app_session.session
    assert _app_session.joined_at == app_session.joined_at
    assert _app_session.left_at == app_session.left_at
    assert _app_session.node_oid == app_session.node_oid
    assert _app_session.node_authid == app_session.node_authid
    assert _app_session.worker_name == app_session.worker_name
    assert _app_session.worker_pid == app_session.worker_pid
    assert _app_session.transport == app_session.transport
    assert _app_session.realm == app_session.realm
    assert _app_session.authid == app_session.authid
    assert _app_session.authrole == app_session.authrole
    assert _app_session.authmethod == app_session.authmethod
    assert _app_session.authprovider == app_session.authprovider
    assert _app_session.authextra == app_session.authextra


def test_app_session_roundtrip_perf(app_session, builder):
    obj = app_session.build(builder)
    builder.Finish(obj)
    data = builder.Output()
    scratch = {'session': 0}

    def loop():
        _app_session = AppSession.cast(data)
        if True:
            assert _app_session.arealm_oid == app_session.arealm_oid
            assert _app_session.oid == app_session.oid
            assert _app_session.session == app_session.session
            assert _app_session.joined_at == app_session.joined_at
            assert _app_session.left_at == app_session.left_at
            assert _app_session.node_oid == app_session.node_oid
            assert _app_session.node_authid == app_session.node_authid
            assert _app_session.worker_name == app_session.worker_name
            assert _app_session.worker_pid == app_session.worker_pid
            assert _app_session.transport == app_session.transport
            assert _app_session.realm == app_session.realm
            assert _app_session.authid == app_session.authid
            assert _app_session.authrole == app_session.authrole
            assert _app_session.authmethod == app_session.authmethod
            assert _app_session.authprovider == app_session.authprovider
            assert _app_session.authextra == app_session.authextra

            scratch['session'] += app_session.session

    N = 5
    M = 100000
    samples = []
    print('measuring:')
    for i in range(N):
        secs = timeit.timeit(loop, number=M)
        ops = round(float(M) / secs, 1)
        samples.append(ops)
        print('{} objects/sec performance'.format(ops))

    samples = sorted(samples)
    ops50 = samples[int(len(samples) / 2)]
    print('RESULT: {} objects/sec median performance'.format(ops50))

    assert ops50 > 1000
    assert scratch['session'] > 0
