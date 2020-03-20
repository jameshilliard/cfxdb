##############################################################################
#
#                        Crossbar.io FX
#     Copyright (C) Crossbar.io Technologies GmbH. All rights reserved.
#
##############################################################################

import os
import random
import timeit

import txaio
txaio.use_twisted()  # noqa

import flatbuffers
import pytest
import numpy as np
from txaio import time_ns

from cfxdb.xbr import PayingChannelRequest


def fill_paying_channel_req(paying_channel_req):
    paying_channel_req.request = os.urandom(16)
    paying_channel_req.timestamp = np.datetime64(time_ns(), 'ns')
    paying_channel_req.market = os.urandom(16)
    paying_channel_req.sender = os.urandom(20)
    paying_channel_req.delegate = os.urandom(20)
    paying_channel_req.recipient = os.urandom(20)
    paying_channel_req.amount = random.randint(0, 2**256 - 1)
    paying_channel_req.timeout = random.randint(0, 2**32 - 1)
    paying_channel_req.state = random.choice([1, 2, 3])
    paying_channel_req.error_msg = 'some error message {}'.format(random.randint(0, 1000))
    paying_channel_req.channel = os.urandom(16)


@pytest.fixture(scope='function')
def paying_channel_req():
    _paying_channel_req = PayingChannelRequest()
    fill_paying_channel_req(_paying_channel_req)
    return _paying_channel_req


@pytest.fixture(scope='function')
def builder():
    _builder = flatbuffers.Builder(0)
    return _builder


def test_paying_channel_req_roundtrip(paying_channel_req, builder):
    # serialize to bytes (flatbuffers) from python object
    obj = paying_channel_req.build(builder)
    builder.Finish(obj)
    data = builder.Output()
    assert len(data) == 352

    # create python object from bytes (flatbuffes)
    _paying_channel_req = PayingChannelRequest.cast(data)

    assert _paying_channel_req.request == paying_channel_req.request
    assert _paying_channel_req.timestamp == paying_channel_req.timestamp
    assert _paying_channel_req.market == paying_channel_req.market
    assert _paying_channel_req.sender == paying_channel_req.sender
    assert _paying_channel_req.delegate == paying_channel_req.delegate
    assert _paying_channel_req.recipient == paying_channel_req.recipient
    assert _paying_channel_req.amount == paying_channel_req.amount
    assert _paying_channel_req.timeout == paying_channel_req.timeout
    assert _paying_channel_req.state == paying_channel_req.state
    assert _paying_channel_req.error_msg == paying_channel_req.error_msg
    assert _paying_channel_req.channel == paying_channel_req.channel


def test_paying_channel_req_roundtrip_perf(paying_channel_req, builder):
    obj = paying_channel_req.build(builder)
    builder.Finish(obj)
    data = builder.Output()
    scratch = {'value': 0}

    def loop():
        _paying_channel_req = PayingChannelRequest.cast(data)
        if True:
            assert _paying_channel_req.request == paying_channel_req.request
            assert _paying_channel_req.timestamp == paying_channel_req.timestamp
            assert _paying_channel_req.market == paying_channel_req.market
            assert _paying_channel_req.sender == paying_channel_req.sender
            assert _paying_channel_req.delegate == paying_channel_req.delegate
            assert _paying_channel_req.recipient == paying_channel_req.recipient
            assert _paying_channel_req.amount == paying_channel_req.amount
            assert _paying_channel_req.timeout == paying_channel_req.timeout
            assert _paying_channel_req.state == paying_channel_req.state
            assert _paying_channel_req.error_msg == paying_channel_req.error_msg
            assert _paying_channel_req.channel == paying_channel_req.channel

            scratch['value'] += int(_paying_channel_req.channel[0])
            scratch['value'] += int(_paying_channel_req.channel[7])
            scratch['value'] += int(_paying_channel_req.channel[15])

    N = 5
    M = 10000
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
    print(scratch['value'])
