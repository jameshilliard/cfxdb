##############################################################################
#
#                        Crossbar.io FX
#     Copyright (C) Crossbar.io Technologies GmbH. All rights reserved.
#
##############################################################################

import pytest
import os
import random
import uuid
import timeit
import platform

import flatbuffers

import txaio
txaio.use_twisted()  # noqa

from txaio import time_ns
from autobahn import util
import zlmdb

from cfxdb.eventstore import Session, Publication, Event

zlmdb.TABLES_BY_UUID = {}


@pytest.fixture(scope='function')
def builder():
    _builder = flatbuffers.Builder(0)
    return _builder


#
# Session
#


def fill_session(session):
    session.session = util.id()
    session.joined_at = time_ns() - 723 * 10**9
    session.left_at = time_ns()
    session.realm = 'realm-{}'.format(uuid.uuid4())
    session.authid = util.generate_serial_number()
    session.authrole = random.choice(['admin', 'user*', 'guest', 'anon*'])


@pytest.fixture(scope='function')
def session():
    _session = Session()
    fill_session(_session)
    return _session


def test_session_roundtrip(session, builder):
    # serialize to bytes (flatbuffers) from python object
    obj = session.build(builder)
    builder.Finish(obj)
    data = builder.Output()
    assert len(data) == 160

    # create python object from bytes (flatbuffes)
    _session = Session.cast(data)

    assert _session.session == session.session
    assert _session.joined_at == session.joined_at
    assert _session.left_at == session.left_at
    assert _session.realm == session.realm
    assert _session.authid == session.authid
    assert _session.authrole == session.authrole


def test_session_roundtrip_perf(session, builder):
    obj = session.build(builder)
    builder.Finish(obj)
    data = builder.Output()
    scratch = {'joined_at': 0}

    def loop():
        _session = Session.cast(data)
        if True:
            assert _session.session == session.session
            assert _session.joined_at == session.joined_at
            assert _session.left_at == session.left_at
            assert _session.realm == session.realm
            assert _session.authid == session.authid
            assert _session.authrole == session.authrole

            scratch['joined_at'] += session.joined_at

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
    assert scratch['joined_at'] > 0


#
# Publication
#


def fill_publication(publication):

    publication.timestamp = time_ns()
    publication.publication = util.id()
    publication.publisher = util.id()
    publication.topic = 'com.example.foobar.{}.doit'.format(uuid.uuid4())

    publication.args = [23, 'hello', {'foo': 0.5}]
    publication.kwargs = {'bar': 23, 'baz': [1, 2, 3]}
    publication.payload = os.urandom(32)

    publication.acknowledge = random.choice([True, False])
    publication.retain = random.choice([True, False])
    publication.exclude_me = random.choice([True, False])

    i0 = util.id()
    publication.exclude = [i0 + j + 1000 for j in range(5)]
    publication.exclude_authid = ['user1', 'user2', 'user3']
    publication.exclude_authrole = ['roleA', 'roleB', 'roleC']

    i0 = util.id()
    publication.eligible = [i0 + j + 1000 for j in range(5)]
    publication.eligible_authid = ['user4', 'user5', 'user6']
    publication.eligible_authrole = ['roleD', 'roleE', 'roleF']

    publication.enc_algo = Publication.ENC_ALGO_XBR
    publication.enc_key = os.urandom(32)
    publication.enc_serializer = Publication.ENC_SER_CBOR


@pytest.fixture(scope='function')
def publication():
    _publication = Publication()
    fill_publication(_publication)
    return _publication


def test_publication_roundtrip(publication, builder):
    obj = publication.build(builder)
    builder.Finish(obj)
    data = builder.Output()
    assert len(data) in [624, 632, 640]

    _publication = Publication.cast(data)

    assert _publication.timestamp == publication.timestamp
    assert _publication.publication == publication.publication
    assert _publication.publisher == publication.publisher
    assert _publication.topic == publication.topic
    assert _publication.args == publication.args
    assert _publication.kwargs == publication.kwargs
    assert _publication.payload == publication.payload
    assert _publication.acknowledge == publication.acknowledge
    assert _publication.retain == publication.retain
    assert _publication.exclude_me == publication.exclude_me
    assert _publication.exclude == publication.exclude
    assert _publication.exclude_authid == publication.exclude_authid
    assert _publication.exclude_authrole == publication.exclude_authrole
    assert _publication.eligible == publication.eligible
    assert _publication.eligible_authid == publication.eligible_authid
    assert _publication.eligible_authrole == publication.eligible_authrole
    assert _publication.enc_algo == publication.enc_algo
    assert _publication.enc_key == publication.enc_key
    assert _publication.enc_serializer == publication.enc_serializer


def test_publication_roundtrip_perf(publication, builder):
    obj = publication.build(builder)
    builder.Finish(obj)
    data = builder.Output()
    scratch = {'timestamp': 0}

    def loop():
        _publication = Publication.cast(data)
        if True:
            assert _publication.timestamp == publication.timestamp
            assert _publication.publication == publication.publication
            assert _publication.publisher == publication.publisher
            assert _publication.topic == publication.topic
            assert _publication.args == publication.args
            assert _publication.kwargs == publication.kwargs
            assert _publication.payload == publication.payload
            assert _publication.acknowledge == publication.acknowledge
            assert _publication.retain == publication.retain
            assert _publication.exclude_me == publication.exclude_me
            assert _publication.exclude == publication.exclude
            assert _publication.exclude_authid == publication.exclude_authid
            assert _publication.exclude_authrole == publication.exclude_authrole
            assert _publication.eligible == publication.eligible
            assert _publication.eligible_authid == publication.eligible_authid
            assert _publication.eligible_authrole == publication.eligible_authrole
            assert _publication.enc_algo == publication.enc_algo
            assert _publication.enc_key == publication.enc_key
            assert _publication.enc_serializer == publication.enc_serializer

            scratch['timestamp'] += publication.timestamp

    N = 5

    if platform.python_implementation() == 'PyPy':
        M = 100000
    else:
        M = 10000
    samples = []
    print('measuring with N={}, M={}:'.format(N, M))
    for i in range(N):
        secs = timeit.timeit(loop, number=M)
        ops = round(float(M) / secs, 1)
        samples.append(ops)
        print('{} objects/sec performance'.format(ops))

    samples = sorted(samples)
    ops50 = samples[int(len(samples) / 2)]
    print('RESULT: {} objects/sec median performance ({} objects total)'.format(ops50, N * M))

    assert ops50 > 1000
    assert scratch['timestamp'] > 0


#
# Event
#


def fill_event(event):
    event.timestamp = time_ns()
    event.subscription = util.id()
    event.publication = util.id()
    event.receiver = util.id()
    event.retained = random.choice([True, False])
    event.acknowledged_delivery = random.choice([True, False])


@pytest.fixture(scope='function')
def event():
    _event = Event()
    fill_event(_event)
    return _event


def test_event_roundtrip(event, builder):
    obj = event.build(builder)
    builder.Finish(obj)
    data = builder.Output()
    assert len(data) in [64, 56]

    _event = Event.cast(data)

    assert _event.timestamp == event.timestamp
    assert _event.subscription == event.subscription
    assert _event.publication == event.publication
    assert _event.receiver == event.receiver
    assert _event.retained == event.retained
    assert _event.acknowledged_delivery == event.acknowledged_delivery


def test_event_roundtrip_perf(event, builder):
    obj = event.build(builder)
    builder.Finish(obj)
    data = builder.Output()
    scratch = {'timestamp': 0}

    def loop():
        _event = Event.cast(data)
        if True:
            assert _event.timestamp == event.timestamp
            assert _event.subscription == event.subscription
            assert _event.publication == event.publication
            assert _event.receiver == event.receiver
            assert _event.retained == event.retained
            assert _event.acknowledged_delivery == event.acknowledged_delivery

            scratch['timestamp'] += event.timestamp

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
    assert scratch['timestamp'] > 0
