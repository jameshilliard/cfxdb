##############################################################################
#
#                        Crossbar.io FX
#     Copyright (C) Crossbar.io Technologies GmbH. All rights reserved.
#
##############################################################################

import random
import timeit

import txaio
txaio.use_twisted()  # noqa

import flatbuffers
import pytest

from cfxdb.xbr import PaymentChannelBalance


def fill_payment_channel_bal(payment_channel_bal):
    payment_channel_bal.remaining = random.randint(0, 2**256 - 1)
    payment_channel_bal.inflight = random.randint(0, 2**256 - 1)
    payment_channel_bal.seq = random.randint(0, 2**32 - 1)


@pytest.fixture(scope='function')
def payment_channel_bal():
    _payment_channel_bal = PaymentChannelBalance()
    fill_payment_channel_bal(_payment_channel_bal)
    return _payment_channel_bal


@pytest.fixture(scope='function')
def builder():
    _builder = flatbuffers.Builder(0)
    return _builder


def test_payment_channel_bal_roundtrip(payment_channel_bal, builder):
    # serialize to bytes (flatbuffers) from python object
    obj = payment_channel_bal.build(builder)
    builder.Finish(obj)
    data = builder.Output()
    assert len(data) == 112

    # create python object from bytes (flatbuffes)
    _payment_channel_bal = PaymentChannelBalance.cast(data)

    assert _payment_channel_bal.remaining == payment_channel_bal.remaining
    assert _payment_channel_bal.inflight == payment_channel_bal.inflight
    assert _payment_channel_bal.seq == payment_channel_bal.seq


def test_payment_channel_bal_roundtrip_perf(payment_channel_bal, builder):
    obj = payment_channel_bal.build(builder)
    builder.Finish(obj)
    data = builder.Output()
    scratch = {'value': 0}

    def loop():
        _payment_channel_bal = PaymentChannelBalance.cast(data)
        if True:
            assert _payment_channel_bal.remaining == payment_channel_bal.remaining
            assert _payment_channel_bal.inflight == payment_channel_bal.inflight
            assert _payment_channel_bal.seq == payment_channel_bal.seq

            scratch['value'] += int(_payment_channel_bal.seq)

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
