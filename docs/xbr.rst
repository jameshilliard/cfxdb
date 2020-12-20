.. _XBRDB:

XBR Market Maker
================

`schema.PaymentChannels`
------------------------

.. autoclass:: cfxdb.xbrmm.PaymentChannels

.. autoclass:: cfxdb.xbrmm.IndexPaymentChannelByDelegate

.. autoclass:: cfxdb.xbrmm.PaymentChannel
    :members:
    :undoc-members:
        channel,
        market,
        sender,
        delegate,
        recipient,
        amount,
        timeout,
        state,
        open_at,
        closing_at,
        closed_at
    :member-order: bysource


`schema.PaymentChannelBalances`
-------------------------------

.. autoclass:: cfxdb.xbrmm.PaymentChannelBalances

.. autoclass:: cfxdb.xbrmm.PaymentChannelBalance
    :members:
    :undoc-members:
        remaining,
        inflight
    :member-order: bysource


`schema.Offers`
---------------

.. autoclass:: cfxdb.xbrmm.Offers

.. autoclass:: cfxdb.xbrmm.IndexOfferByKey

.. autoclass:: cfxdb.xbrmm.Offer
    :members:
    :undoc-members:
        timestamp,
        offer,
        seller,
        seller_session_id,
        seller_authid,
        key,
        api,
        uri,
        valid_from,
        signature,
        price,
        categories,
        expires,
        copies,
        remaining
    :member-order: bysource
