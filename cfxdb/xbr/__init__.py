##############################################################################
#
#                        Crossbar.io FX
#     Copyright (C) Crossbar.io Technologies GmbH. All rights reserved.
#
##############################################################################

from .actor import Actor, Actors
from .block import Block, Blocks
from .channel import PaymentChannel, PaymentChannels, IndexPaymentChannelByDelegate, PaymentChannelBalance, PaymentChannelBalances, \
    PayingChannelRequest, PayingChannelRequests, PayingChannels, IndexPayingChannelByDelegate, IndexPayingChannelByRecipient, \
    PayingChannelBalances, IndexPayingChannelRequestByRecipient
from .market import Market, Markets, IndexMarketsByOwner, IndexMarketsByActor
from .member import Member, Members
from .offer import Offer, Offers, IndexOfferByKey
from .token import TokenApproval, TokenApprovals, TokenTransfer, TokenTransfers
from .transaction import Transaction, Transactions

from cfxdb.gen.xbr.MemberLevel import MemberLevel
from cfxdb.gen.xbr.ActorType import ActorType
from cfxdb.gen.xbr.PayingChannelRequestState import PayingChannelRequestState
from cfxdb.gen.xbr.PaymentChannelType import PaymentChannelType
from cfxdb.gen.xbr.PaymentChannelState import PaymentChannelState
from cfxdb.gen.xbr.TransactionState import TransactionState

__all__ = (
    # database schema
    'Schema',

    # enum types
    'MemberLevel',
    'ActorType',
    'PayingChannelRequestState',
    'PaymentChannelType',
    'PaymentChannelState',
    'TransactionState',

    # table/index types
    'Actor',
    'Actors',
    'Block',
    'Blocks',
    'PaymentChannel',
    'PaymentChannels',
    'IndexPaymentChannelByDelegate',
    'PaymentChannelBalance',
    'PaymentChannelBalances',
    'PayingChannelRequest',
    'PayingChannelRequests',
    'PayingChannels',
    'IndexPayingChannelByDelegate',
    'IndexPayingChannelByRecipient',
    'PayingChannelBalances',
    'IndexPayingChannelRequestByRecipient',
    'Market',
    'Markets',
    'IndexMarketsByOwner',
    'IndexMarketsByActor',
    'Member',
    'Members',
    'Offer',
    'Offers',
    'IndexOfferByKey',
    'TokenApproval',
    'TokenApprovals',
    'TokenTransfer',
    'TokenTransfers',
    'Transaction',
    'Transactions',
)


class Schema(object):
    """
    CFC edge database schema for ZLMDB.
    """
    def __init__(self, db):
        self.db = db

    blocks: Blocks
    """
    Ethereum blocks basic information.
    """

    token_approvals: TokenApprovals
    """
    Token approvals archive.
    """

    token_transfers: TokenTransfers
    """
    Token transfers archive.
    """

    members: Members
    """
    XBR network members.
    """

    markets: Markets
    """
    XBR markets.
    """

    idx_markets_by_owner: IndexMarketsByOwner
    """
    Index ``(owner_adr, created) -> market_oid``.
    """

    idx_markets_by_actor: IndexMarketsByActor
    """
    Index ``(actor_adr, joined) -> market_oid``.
    """

    actors: Actors
    """
    XBR market actors.
    """

    payment_channels: PaymentChannels
    """
    Payment channels for XBR consumer delegates.
    """

    idx_payment_channel_by_delegate: IndexPaymentChannelByDelegate
    """
    Maps from XBR consumer delegate address to the currently active payment
    channel address for the given consumer delegate.
    """

    payment_balances: PaymentChannelBalances
    """
    Current off-chain balances within payment channels.
    """

    paying_channel_requests: PayingChannelRequests
    """
    Requests for openng paying channels.
    """

    paying_channels: PayingChannels
    """
    Paying channels for XBR provider delegates.
    """

    idx_paying_channel_by_delegate: IndexPayingChannelByDelegate
    """
    Maps from XBR provider delegate address to the currently active paying
    channel address for the given provider delegate.
    """

    idx_paying_channel_requests_by_recipient: IndexPayingChannelByRecipient
    """
    """

    paying_balances: PayingChannelBalances
    """
    Current off-chain balances within paying channels.
    """

    key_offers: Offer
    """
    Data encryption key offers.
    """

    idx_offer_by_key: IndexOfferByKey
    """
    Index of key offers by key ID (rather than offer ID, as the object table
    is indexed by).
    """

    transaction: Transactions
    """
    """

    @staticmethod
    def attach(db):
        """
        Factory to create a schema from attaching to a database. The schema tables
        will be automatically mapped as persistant maps and attached to the
        database slots.

        :param db: zlmdb.Database
        :return: object of Schema
        """
        schema = Schema(db)

        schema.blocks = db.attach_table(Blocks)

        schema.token_approvals = db.attach_table(TokenApprovals)

        schema.token_transfers = db.attach_table(TokenTransfers)

        schema.members = db.attach_table(Members)

        schema.markets = db.attach_table(Markets)

        schema.idx_markets_by_owner = db.attach_table(IndexMarketsByOwner)

        schema.markets.attach_index('idx1', schema.idx_markets_by_owner, lambda market:
                                    (market.owner, market.timestamp))

        schema.actors = db.attach_table(Actors)
        schema.idx_markets_by_actor = db.attach_table(IndexMarketsByActor)

        # schema.actors.attach_index('idx1', schema.idx_markets_by_actor, lambda actor:
        #                            (actor.actor, actor.timestamp))

        schema.payment_channels = db.attach_table(PaymentChannels)

        schema.idx_payment_channel_by_delegate = db.attach_table(IndexPaymentChannelByDelegate)
        # schema.payment_channels.attach_index('idx1',
        #                                      schema.idx_payment_channel_by_delegate,
        #                                      lambda payment_channel: (bytes(payment_channel.delegate), np.datetime64(time_ns(), 'ns')))

        schema.payment_balances = db.attach_table(PaymentChannelBalances)

        schema.paying_channel_requests = db.attach_table(PayingChannelRequests)

        schema.idx_paying_channel_requests_by_recipient = db.attach_table(
            IndexPayingChannelRequestByRecipient)
        schema.paying_channel_requests.attach_index(
            'idx1', schema.idx_paying_channel_requests_by_recipient,
            lambda paying_channel_request: bytes(paying_channel_request.recipient))

        schema.paying_channels = db.attach_table(PayingChannels)

        schema.idx_paying_channel_by_delegate = db.attach_table(IndexPayingChannelByDelegate)
        # schema.paying_channels.attach_index('idx1',
        #                                      schema.idx_paying_channel_by_delegate,
        #                                      lambda paying_channel: (bytes(paying_channel.delegate), np.datetime64(time_ns(), 'ns')))

        # schema.idx_paying_channel_by_recipient = db.attach_table(IndexPayingChannelByRecipient)
        # schema.paying_channels.attach_index('idx2',
        #                                      schema.idx_paying_channel_by_recipient,
        #                                      lambda paying_channel: (bytes(paying_channel.recipient), np.datetime64(time_ns(), 'ns')))

        schema.paying_balances = db.attach_table(PayingChannelBalances)

        schema.offers = db.attach_table(Offers)
        schema.idx_offer_by_key = db.attach_table(IndexOfferByKey)
        schema.offers.attach_index('idx1', schema.idx_offer_by_key, lambda offer: offer.key)

        schema.transactions = db.attach_table(Transactions)

        return schema
