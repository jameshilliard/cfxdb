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

from cfxdb.xbr import PaymentChannel


def fill_payment_channel(payment_channel):
    payment_channel.type = random.randint(1, 2)
    payment_channel.channel = os.urandom(16)
    payment_channel.market = os.urandom(16)
    payment_channel.sender = os.urandom(20)
    payment_channel.delegate = os.urandom(20)
    payment_channel.recipient = os.urandom(20)
    payment_channel.amount = random.randint(0, 2**256 - 1)
    payment_channel.timeout = random.randint(0, 2**32 - 1)
    payment_channel.state = random.randint(1, 3)
    payment_channel.open_at = random.randint(0, 2**256 - 1)
    payment_channel.closing_at = random.randint(0, 2**256 - 1)
    payment_channel.closed_at = random.randint(0, 2**256 - 1)
    payment_channel.close_mm_sig = os.urandom(65)
    payment_channel.close_del_sig = os.urandom(65)
    payment_channel.close_channel_seq = random.randint(0, 2**32 - 1)
    payment_channel.close_is_final = random.choice([True, False])
    payment_channel.close_balance = random.randint(0, 2**256 - 1)
    payment_channel.closed_tx = os.urandom(32)


@pytest.fixture(scope='function')
def payment_channel():
    _payment_channel = PaymentChannel()
    fill_payment_channel(_payment_channel)
    return _payment_channel


@pytest.fixture(scope='function')
def builder():
    _builder = flatbuffers.Builder(0)
    return _builder


def test_payment_channel_roundtrip(payment_channel, builder):
    # serialize to bytes (flatbuffers) from python object
    obj = payment_channel.build(builder)
    builder.Finish(obj)
    data = builder.Output()
    assert len(data) in [632, 636]

    # create python object from bytes (flatbuffes)
    _payment_channel = PaymentChannel.cast(data)

    assert _payment_channel.type == payment_channel.type
    assert _payment_channel.channel == payment_channel.channel
    assert _payment_channel.market == payment_channel.market
    assert _payment_channel.sender == payment_channel.sender
    assert _payment_channel.delegate == payment_channel.delegate
    assert _payment_channel.recipient == payment_channel.recipient
    assert _payment_channel.amount == payment_channel.amount
    assert _payment_channel.timeout == payment_channel.timeout
    assert _payment_channel.state == payment_channel.state
    assert _payment_channel.open_at == payment_channel.open_at
    assert _payment_channel.closing_at == payment_channel.closing_at
    assert _payment_channel.closed_at == payment_channel.closed_at
    assert _payment_channel.close_mm_sig == payment_channel.close_mm_sig
    assert _payment_channel.close_del_sig == payment_channel.close_del_sig
    assert _payment_channel.close_channel_seq == payment_channel.close_channel_seq
    assert _payment_channel.close_is_final == payment_channel.close_is_final
    assert _payment_channel.close_balance == payment_channel.close_balance
    assert _payment_channel.closed_tx == payment_channel.closed_tx


def test_payment_channel_roundtrip_perf(payment_channel, builder):
    obj = payment_channel.build(builder)
    builder.Finish(obj)
    data = builder.Output()
    scratch = {'value': 0}

    def loop():
        _payment_channel = PaymentChannel.cast(data)
        if True:
            assert _payment_channel.type == payment_channel.type
            assert _payment_channel.channel == payment_channel.channel
            assert _payment_channel.market == payment_channel.market
            assert _payment_channel.sender == payment_channel.sender
            assert _payment_channel.delegate == payment_channel.delegate
            assert _payment_channel.recipient == payment_channel.recipient
            assert _payment_channel.amount == payment_channel.amount
            assert _payment_channel.timeout == payment_channel.timeout
            assert _payment_channel.state == payment_channel.state
            assert _payment_channel.open_at == payment_channel.open_at
            assert _payment_channel.closing_at == payment_channel.closing_at
            assert _payment_channel.closed_at == payment_channel.closed_at

            assert _payment_channel.close_mm_sig == payment_channel.close_mm_sig
            assert _payment_channel.close_del_sig == payment_channel.close_del_sig
            assert _payment_channel.close_channel_seq == payment_channel.close_channel_seq
            assert _payment_channel.close_is_final == payment_channel.close_is_final
            assert _payment_channel.close_balance == payment_channel.close_balance
            assert _payment_channel.closed_tx == payment_channel.closed_tx

            scratch['value'] += int(_payment_channel.channel[0])
            scratch['value'] += int(_payment_channel.channel[7])
            scratch['value'] += int(_payment_channel.channel[15])

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
