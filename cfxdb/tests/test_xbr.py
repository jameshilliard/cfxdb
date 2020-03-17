##############################################################################
#
#                        Crossbar.io FX
#     Copyright (C) Crossbar.io Technologies GmbH. All rights reserved.
#
##############################################################################

import os
import uuid
import random
import timeit
import pytest

import numpy as np
import flatbuffers

import zlmdb

import txaio
txaio.use_twisted()  # noqa

from txaio import time_ns
from autobahn import util

from cfxdb.xbr import TokenApproval, TokenTransfer, Market, Member, Actor, \
    PaymentChannel, PayingChannelRequest, PaymentChannelBalance, Offer, Transaction

from cfxdb.tests._util import _gen_ipfs_hash

zlmdb.TABLES_BY_UUID = {}


@pytest.fixture(scope='function')
def builder():
    _builder = flatbuffers.Builder(0)
    return _builder


#
# Actor
#


def fill_actor(actor):
    actor.actor = os.urandom(20)
    actor.actor_type = random.randint(1, 2)
    actor.market = uuid.uuid4()
    actor.timestamp = np.datetime64(time_ns(), 'ns')
    actor.joined = random.randint(0, 2**256 - 1)
    actor.security = random.randint(0, 2**256 - 1)
    actor.meta = _gen_ipfs_hash()
    actor.tid = os.urandom(32)
    actor.signature = os.urandom(65)


@pytest.fixture(scope='function')
def actor():
    _actor = Actor()
    fill_actor(_actor)
    return _actor


def test_actor_roundtrip(actor, builder):
    # serialize to bytes (flatbuffers) from python object
    obj = actor.build(builder)
    builder.Finish(obj)
    data = builder.Output()
    assert len(data) == 368

    # create python object from bytes (flatbuffes)
    _actor = Actor.cast(data)

    assert _actor.actor == actor.actor
    assert _actor.actor_type == actor.actor_type
    assert _actor.market == actor.market
    assert _actor.timestamp == actor.timestamp
    assert _actor.joined == actor.joined
    assert _actor.security == actor.security
    assert _actor.meta == actor.meta
    assert _actor.tid == actor.tid
    assert _actor.signature == actor.signature


def test_actor_roundtrip_perf(actor, builder):
    obj = actor.build(builder)
    builder.Finish(obj)
    data = builder.Output()
    scratch = {'value': 0}

    def loop():
        _actor = Actor.cast(data)
        if True:
            assert _actor.actor == actor.actor
            assert _actor.actor_type == actor.actor_type
            assert _actor.market == actor.market
            assert _actor.timestamp == actor.timestamp
            assert _actor.joined == actor.joined
            assert _actor.security == actor.security
            assert _actor.meta == actor.meta
            assert _actor.tid == actor.tid
            assert _actor.signature == actor.signature

            scratch['value'] += _actor.actor_type

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


#
# Member
#


def fill_member(member):
    member.address = os.urandom(20)
    member.account_oid = uuid.uuid4()
    member.timestamp = np.datetime64(time_ns(), 'ns')
    member.registered = random.randint(0, 2**256 - 1)
    member.eula = _gen_ipfs_hash()
    member.profile = _gen_ipfs_hash()
    member.level = random.randint(1, 5)
    member.tid = os.urandom(32)
    member.signature = os.urandom(65)


@pytest.fixture(scope='function')
def member():
    _member = Member()
    fill_member(_member)
    return _member


def test_member_roundtrip(member, builder):
    # serialize to bytes (flatbuffers) from python object
    obj = member.build(builder)
    builder.Finish(obj)
    data = builder.Output()
    assert len(data) == 384

    # create python object from bytes (flatbuffes)
    _member = Member.cast(data)

    assert _member.address == member.address
    assert _member.account_oid == member.account_oid
    assert _member.timestamp == member.timestamp
    assert _member.registered == member.registered
    assert _member.eula == member.eula
    assert _member.profile == member.profile
    assert _member.level == member.level
    assert _member.tid == member.tid
    assert _member.signature == member.signature


def test_member_roundtrip_perf(member, builder):
    obj = member.build(builder)
    builder.Finish(obj)
    data = builder.Output()
    scratch = {'value': 0}

    def loop():
        _member = Member.cast(data)
        if True:
            assert _member.address == member.address
            assert _member.account_oid == member.account_oid
            assert _member.timestamp == member.timestamp
            assert _member.registered == member.registered
            assert _member.eula == member.eula
            assert _member.profile == member.profile
            assert _member.level == member.level
            assert _member.tid == member.tid
            assert _member.signature == member.signature

            scratch['value'] += _member.level

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


#
# Market
#


def fill_market(market):
    market.market = uuid.uuid4()
    market.timestamp = np.datetime64(time_ns(), 'ns')
    market.seq = random.randint(1, 2**32 - 1)
    market.owner = os.urandom(20)
    market.coin = os.urandom(20)
    market.terms = _gen_ipfs_hash()
    market.meta = _gen_ipfs_hash()
    market.maker = os.urandom(20)
    market.provider_security = random.randint(0, 2**256 - 1)
    market.consumer_security = random.randint(0, 2**256 - 1)
    market.market_fee = random.randint(0, 2**256 - 1)
    market.tid = os.urandom(32)
    market.signature = os.urandom(65)


@pytest.fixture(scope='function')
def market():
    _market = Market()
    fill_market(_market)
    return _market


def test_market_roundtrip(market, builder):
    # serialize to bytes (flatbuffers) from python object
    obj = market.build(builder)
    builder.Finish(obj)
    data = builder.Output()
    assert len(data) == 544

    # create python object from bytes (flatbuffes)
    _market = Market.cast(data)

    assert _market.market == market.market
    assert _market.timestamp == market.timestamp
    assert _market.seq == market.seq
    assert _market.owner == market.owner
    assert _market.coin == market.coin
    assert _market.terms == market.terms
    assert _market.meta == market.meta
    assert _market.maker == market.maker
    assert _market.provider_security == market.provider_security
    assert _market.consumer_security == market.consumer_security
    assert _market.market_fee == market.market_fee
    assert _market.tid == market.tid
    assert _market.signature == market.signature


def test_market_roundtrip_perf(market, builder):
    obj = market.build(builder)
    builder.Finish(obj)
    data = builder.Output()
    scratch = {'value': 0}

    def loop():
        _market = Market.cast(data)
        if True:
            assert _market.market == market.market
            assert _market.timestamp == market.timestamp
            assert _market.seq == market.seq
            assert _market.owner == market.owner
            assert _market.coin == market.coin
            assert _market.terms == market.terms
            assert _market.meta == market.meta
            assert _market.maker == market.maker
            assert _market.provider_security == market.provider_security
            assert _market.consumer_security == market.consumer_security
            assert _market.market_fee == market.market_fee
            assert _market.tid == market.tid
            assert _market.signature == market.signature

            scratch['value'] += _market.seq

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


#
# TokenTransfer
#


def fill_token_transfer(token_transfer):
    token_transfer.tx_hash = os.urandom(32)
    token_transfer.block_hash = os.urandom(32)
    token_transfer.from_address = os.urandom(20)
    token_transfer.to_address = os.urandom(20)
    token_transfer.value = random.randint(1, 2**256 - 1)


@pytest.fixture(scope='function')
def token_transfer():
    _token_transfer = TokenTransfer()
    fill_token_transfer(_token_transfer)
    return _token_transfer


def test_token_transfer_roundtrip(token_transfer, builder):
    # serialize to bytes (flatbuffers) from python object
    obj = token_transfer.build(builder)
    builder.Finish(obj)
    data = builder.Output()
    assert len(data) == 220

    # create python object from bytes (flatbuffes)
    _token_transfer = TokenTransfer.cast(data)

    assert _token_transfer.tx_hash == token_transfer.tx_hash
    assert _token_transfer.block_hash == token_transfer.block_hash
    assert _token_transfer.from_address == token_transfer.from_address
    assert _token_transfer.to_address == token_transfer.to_address
    assert _token_transfer.value == token_transfer.value


def test_token_transfer_roundtrip_perf(token_transfer, builder):
    obj = token_transfer.build(builder)
    builder.Finish(obj)
    data = builder.Output()
    scratch = {'value': 0}

    def loop():
        _token_transfer = TokenTransfer.cast(data)
        if True:
            assert _token_transfer.tx_hash == token_transfer.tx_hash
            assert _token_transfer.block_hash == token_transfer.block_hash
            assert _token_transfer.from_address == token_transfer.from_address
            assert _token_transfer.to_address == token_transfer.to_address
            assert _token_transfer.value == token_transfer.value

            scratch['value'] += int(_token_transfer.tx_hash[0])
            scratch['value'] += int(_token_transfer.tx_hash[7])
            scratch['value'] += int(_token_transfer.tx_hash[19])

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


#
# TokenApproval
#


def fill_token_approval(token_approval):
    token_approval.tx_hash = os.urandom(32)
    token_approval.block_hash = os.urandom(32)
    token_approval.owner_address = os.urandom(20)
    token_approval.spender_address = os.urandom(20)
    token_approval.value = random.randint(1, 2**256 - 1)


@pytest.fixture(scope='function')
def token_approval():
    _token_approval = TokenApproval()
    fill_token_approval(_token_approval)
    return _token_approval


def test_token_approval_roundtrip(token_approval, builder):
    # serialize to bytes (flatbuffers) from python object
    obj = token_approval.build(builder)
    builder.Finish(obj)
    data = builder.Output()
    assert len(data) == 220

    # create python object from bytes (flatbuffes)
    _token_approval = TokenApproval.cast(data)

    assert _token_approval.tx_hash == token_approval.tx_hash
    assert _token_approval.block_hash == token_approval.block_hash
    assert _token_approval.owner_address == token_approval.owner_address
    assert _token_approval.spender_address == token_approval.spender_address
    assert _token_approval.value == token_approval.value


def test_token_approval_roundtrip_perf(token_approval, builder):
    obj = token_approval.build(builder)
    builder.Finish(obj)
    data = builder.Output()
    scratch = {'value': 0}

    def loop():
        _token_approval = TokenApproval.cast(data)
        if True:
            assert _token_approval.tx_hash == token_approval.tx_hash
            assert _token_approval.block_hash == token_approval.block_hash
            assert _token_approval.owner_address == token_approval.owner_address
            assert _token_approval.spender_address == token_approval.spender_address
            assert _token_approval.value == token_approval.value

            scratch['value'] += int(_token_approval.tx_hash[0])
            scratch['value'] += int(_token_approval.tx_hash[7])
            scratch['value'] += int(_token_approval.tx_hash[19])

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


#
# PaymentChannel
#


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


#
# PayingChannelRequest
#


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


#
# PaymentChannelBalance
#


def fill_payment_channel_bal(payment_channel_bal):
    payment_channel_bal.remaining = random.randint(0, 2**256 - 1)
    payment_channel_bal.inflight = random.randint(0, 2**256 - 1)
    payment_channel_bal.seq = random.randint(0, 2**32 - 1)


@pytest.fixture(scope='function')
def payment_channel_bal():
    _payment_channel_bal = PaymentChannelBalance()
    fill_payment_channel_bal(_payment_channel_bal)
    return _payment_channel_bal


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


#
# Offers
#


def fill_offer(offer):
    now = time_ns()
    offer.timestamp = np.datetime64(now, 'ns')
    offer.offer = uuid.uuid4()
    offer.seller = os.urandom(20)
    offer.seller_session_id = random.randint(0, 2**53)
    offer.seller_authid = util.generate_token(5, 4)
    offer.key = uuid.uuid4()
    offer.api = uuid.uuid4()
    offer.uri = 'com.example.something.add2'
    offer.valid_from = np.datetime64(now, 'ns')
    offer.signature = os.urandom(64)
    offer.price = random.randint(0, 2**256 - 1)
    offer.categories = {
        'xtile': '{:05}'.format(random.randint(0, 99999)),
        'ytile': '{:05}'.format(random.randint(0, 99999)),
    }
    offer.expires = np.datetime64(now + 60 * 60 * 10**9, 'ns')
    offer.copies = 1000
    offer.remaining = random.randint(0, 1000)


def fill_offer_empty(offer):
    offer.timestamp = None
    offer.offer = None
    offer.seller = None
    offer.seller_session_id = None
    offer.seller_authid = None
    offer.key = None
    offer.api = None
    offer.uri = None
    offer.valid_from = None
    offer.signature = None
    offer.price = None
    offer.categories = None
    offer.expires = None
    offer.copies = None
    offer.remaining = None


@pytest.fixture(scope='function')
def offer():
    _offer = Offer()
    fill_offer(_offer)
    return _offer


def test_offer_roundtrip(offer, builder):
    # serialize to bytes (flatbuffers) from python object
    obj = offer.build(builder)
    builder.Finish(obj)
    data = builder.Output()
    assert len(data) == 480

    # create python object from bytes (flatbuffes)
    _offer = Offer.cast(data)

    assert _offer.timestamp == offer.timestamp
    assert _offer.offer == offer.offer
    assert _offer.seller == offer.seller
    assert _offer.seller_session_id == offer.seller_session_id
    assert _offer.seller_authid == offer.seller_authid
    assert _offer.key == offer.key
    assert _offer.api == offer.api
    assert _offer.uri == offer.uri
    assert _offer.valid_from == offer.valid_from
    assert _offer.signature == offer.signature
    assert _offer.price == offer.price
    assert _offer.categories == offer.categories
    assert _offer.expires == offer.expires
    assert _offer.copies == offer.copies
    assert _offer.remaining == offer.remaining


def test_offer_empty(builder):
    offer = Offer()
    fill_offer_empty(offer)

    # serialize to bytes (flatbuffers) from python object
    obj = offer.build(builder)
    builder.Finish(obj)
    data = builder.Output()
    assert len(data) == 12

    # create python object from bytes (flatbuffes)
    _offer = Offer.cast(data)

    unix_zero = np.datetime64(0, 'ns')

    assert _offer.timestamp == unix_zero
    assert _offer.offer is None
    assert _offer.seller is None
    assert _offer.seller_session_id == 0
    assert _offer.seller_authid is None
    assert _offer.key is None
    assert _offer.api is None
    assert _offer.uri is None
    assert _offer.valid_from == unix_zero
    assert _offer.signature is None
    assert _offer.price == 0
    assert _offer.categories is None
    assert _offer.expires == unix_zero
    assert _offer.copies == 0
    assert _offer.remaining == 0


def test_offer_roundtrip_perf(offer, builder):
    obj = offer.build(builder)
    builder.Finish(obj)
    data = builder.Output()
    scratch = {'value': 0}

    def loop():
        _offer = Offer.cast(data)
        if True:
            assert _offer.timestamp == offer.timestamp
            assert _offer.offer == offer.offer
            assert _offer.seller == offer.seller
            assert _offer.seller_session_id == offer.seller_session_id
            assert _offer.seller_authid == offer.seller_authid
            assert _offer.key == offer.key
            assert _offer.api == offer.api
            assert _offer.uri == offer.uri
            assert _offer.valid_from == offer.valid_from
            assert _offer.signature == offer.signature
            assert _offer.price == offer.price
            assert _offer.categories == offer.categories
            assert _offer.expires == offer.expires
            assert _offer.copies == offer.copies
            assert _offer.remaining == offer.remaining

            scratch['value'] += _offer.price

    N = 7
    M = 20000
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


#
# Transactions
#


def fill_transaction(transaction):
    now = time_ns()
    transaction.tid = uuid.uuid4()
    transaction.created = np.datetime64(now, 'ns')
    transaction.created_payment_channel_seq = random.randint(0, 1000)
    transaction.created_paying_channel_seq = random.randint(0, 1000)
    transaction.offer = uuid.uuid4()
    transaction.amount = random.randint(0, 2**256 - 1)
    transaction.payment_channel = os.urandom(20)
    transaction.paying_channel = os.urandom(20)
    transaction.state = random.randint(1, 3)
    transaction.completed = np.datetime64(now, 'ns')
    transaction.completed_payment_channel_seq = random.randint(0, 1000)
    transaction.completed_paying_channel_seq = random.randint(0, 1000)

    # transaction.key = uuid.uuid4()
    # transaction.buyer_pubkey = os.urandom(32)
    # transaction.payment_channel_after = random.randint(0, 2**256 - 1)
    # transaction.paying_channel_after = random.randint(0, 2**256 - 1)
    # transaction.payment_mm_sig = os.urandom(65)
    # transaction.payment_del_sig = os.urandom(65)
    # transaction.paying_mm_sig = os.urandom(65)
    # transaction.paying_del_sig = os.urandom(65)


def fill_transaction_empty(transaction):
    transaction.tid = None
    transaction.created = None
    transaction.created_payment_channel_seq = None
    transaction.created_paying_channel_seq = None
    transaction.offer = None
    transaction.amount = None
    transaction.payment_channel = None
    transaction.paying_channel = None
    transaction.state = None
    transaction.completed = None
    transaction.completed_payment_channel_seq = None
    transaction.completed_paying_channel_seq = None

    # transaction.key = None
    # transaction.buyer_pubkey = None
    # transaction.payment_channel_after = None
    # transaction.paying_channel_after = None
    # transaction.payment_mm_sig = None
    # transaction.payment_del_sig = None
    # transaction.paying_mm_sig = None
    # transaction.paying_del_sig = None


@pytest.fixture(scope='function')
def transaction():
    _transaction = Transaction()
    fill_transaction(_transaction)
    return _transaction


def test_transaction_roundtrip(transaction, builder):
    # serialize to bytes (flatbuffers) from python object
    obj = transaction.build(builder)
    builder.Finish(obj)
    data = builder.Output()
    assert len(data) in [240, 248]

    # create python object from bytes (flatbuffes)
    _transaction = Transaction.cast(data)

    assert _transaction.tid == transaction.tid
    assert _transaction.created == transaction.created
    assert _transaction.created_payment_channel_seq == transaction.created_payment_channel_seq
    assert _transaction.created_paying_channel_seq == transaction.created_paying_channel_seq
    assert _transaction.offer == transaction.offer
    assert _transaction.amount == transaction.amount
    assert _transaction.payment_channel == transaction.payment_channel
    assert _transaction.paying_channel == transaction.paying_channel
    assert _transaction.state == transaction.state
    assert _transaction.completed == transaction.completed
    assert _transaction.completed_payment_channel_seq == transaction.completed_payment_channel_seq
    assert _transaction.completed_paying_channel_seq == transaction.completed_paying_channel_seq

    # assert _transaction.key == transaction.key
    # assert _transaction.buyer_pubkey == transaction.buyer_pubkey
    # assert _transaction.payment_channel_after == transaction.payment_channel_after
    # assert _transaction.paying_channel_after == transaction.paying_channel_after
    # assert _transaction.payment_mm_sig == transaction.payment_mm_sig
    # assert _transaction.payment_del_sig == transaction.payment_del_sig
    # assert _transaction.paying_mm_sig == transaction.paying_mm_sig
    # assert _transaction.paying_del_sig == transaction.paying_del_sig


def test_transaction_empty(builder):
    transaction1 = Transaction()
    fill_transaction_empty(transaction1)

    # serialize to bytes (flatbuffers) from python object
    obj = transaction1.build(builder)
    builder.Finish(obj)
    data = builder.Output()
    assert len(data) == 12

    # create python object from bytes (flatbuffes)
    transaction2 = Transaction.cast(data)

    unix_zero = np.datetime64(0, 'ns')

    assert transaction2.tid is None
    assert transaction2.created == unix_zero
    assert transaction2.created_payment_channel_seq == 0
    assert transaction2.created_paying_channel_seq == 0
    assert transaction2.offer is None
    assert transaction2.amount == 0
    assert transaction2.payment_channel is None
    assert transaction2.paying_channel is None
    assert transaction2.state == 0
    assert transaction2.completed == unix_zero
    assert transaction2.completed_payment_channel_seq == 0
    assert transaction2.completed_paying_channel_seq == 0

    # assert transaction2.key is None
    # assert transaction2.buyer_pubkey is None
    # assert transaction2.payment_channel_after == 0
    # assert transaction2.paying_channel_after == 0
    # assert transaction2.payment_mm_sig is None
    # assert transaction2.payment_del_sig is None
    # assert transaction2.paying_mm_sig is None
    # assert transaction2.paying_del_sig is None


def test_transaction_roundtrip_perf(transaction, builder):
    obj = transaction.build(builder)
    builder.Finish(obj)
    data = builder.Output()
    scratch = {'value': 0}

    def loop():
        _transaction = Transaction.cast(data)
        if True:
            assert _transaction.tid == transaction.tid
            assert _transaction.created == transaction.created
            assert _transaction.created_payment_channel_seq == transaction.created_payment_channel_seq
            assert _transaction.created_paying_channel_seq == transaction.created_paying_channel_seq
            assert _transaction.offer == transaction.offer
            assert _transaction.amount == transaction.amount
            assert _transaction.payment_channel == transaction.payment_channel
            assert _transaction.paying_channel == transaction.paying_channel
            assert _transaction.state == transaction.state
            assert _transaction.completed == transaction.completed
            assert _transaction.completed_payment_channel_seq == transaction.completed_payment_channel_seq
            assert _transaction.completed_paying_channel_seq == transaction.completed_paying_channel_seq

            # assert _transaction.key == transaction.key
            # assert _transaction.buyer_pubkey == transaction.buyer_pubkey
            # assert _transaction.payment_channel_after == transaction.payment_channel_after
            # assert _transaction.paying_channel_after == transaction.paying_channel_after
            # assert _transaction.payment_mm_sig == transaction.payment_mm_sig
            # assert _transaction.payment_del_sig == transaction.payment_del_sig
            # assert _transaction.paying_mm_sig == transaction.paying_mm_sig
            # assert _transaction.paying_del_sig == transaction.paying_del_sig

            scratch['value'] += _transaction.amount

    N = 7
    M = 20000
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
