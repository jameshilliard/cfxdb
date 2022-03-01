##############################################################################
#
#                        Crossbar.io FX
#     Copyright (C) Crossbar.io Technologies GmbH. All rights reserved.
#
##############################################################################

import pytest

import txaio
txaio.use_twisted()

import zlmdb  # noqa

import txaio
txaio.use_twisted()
from cfxdb.globalschema import GlobalSchema
import zlmdb


@pytest.fixture(scope='module')
def db():
    db = zlmdb.Database(dbpath='test1')
    db.__enter__()
    return db


def test_stats(db):
    dbs = GlobalSchema.attach(db)

    # {'branch_pages': 0,
    # 'current_size': 10485760,
    # 'depth': 1,
    # 'entries': 14,
    # 'free': 0.999609375,
    # 'last_pgno': 7,
    # 'last_txnid': 14,
    # 'leaf_pages': 1,
    # 'map_addr': 0,
    # 'map_size': 10485760,
    # 'max_readers': 126,
    # 'max_size': 10485760,
    # 'num_readers': 1,
    # 'overflow_pages': 0,
    # 'pages': 1,
    # 'pages_size': 4096,
    # 'psize': 4096,
    # 'read_only': False,
    # 'sync_enabled': True,
    # 'zlmdb_slots': 14}
    stats = db.stats()

    # check default maximum size
    assert stats['max_size'] == 10485760

    # check current size, which is maxsize when writemap==True (which it is by default)
    assert stats['current_size'] == 10485760

    # however, the DB is empty ..
    assert stats['pages'] == 1
    assert stats['free'] > 0.99
