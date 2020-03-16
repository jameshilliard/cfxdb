##############################################################################
#
#                        Crossbar.io FX
#     Copyright (C) Crossbar.io Technologies GmbH. All rights reserved.
#
##############################################################################

from cfxdb.meta import Attributes
from cfxdb.xbr import Blocks, TokenApprovals, TokenTransfers, Members, Markets, IndexMarketsByOwner, \
    IndexMarketsByActor, Actors
from .account import Account, Accounts, IndexAccountsByUsername, IndexAccountsByEmail, IndexAccountsByWallet
from .userkey import UserKey, UserKeys, IndexUserKeyByAccount
from .vaction import VerifiedAction, VerifiedActions

from cfxdb.gen.xbrnetwork.AccountLevel import AccountLevel
from cfxdb.gen.xbrnetwork.WalletType import WalletType
from cfxdb.gen.xbrnetwork.VerificationType import VerificationType
from cfxdb.gen.xbrnetwork.VerificationStatus import VerificationStatus

__all__ = (
    # database schema
    'Schema',

    # enum types
    'AccountLevel',
    'WalletType',
    'VerificationType',
    'VerificationStatus',

    # database tables
    'Account',
    'Accounts',
    'IndexAccountsByUsername',
    'IndexAccountsByEmail',
    'IndexAccountsByWallet',
    'UserKey',
    'UserKeys',
    'IndexUserKeyByAccount',
    'VerifiedAction',
    'VerifiedActions',
)


class Schema(object):
    """
    XBR Network backend database schema.
    """

    attributes: Attributes
    """
    Generic meta-data attributes that can be stored on objects in tables. Primary key of this table is ``(table_oid, object_oid, attribute)``.
    """

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
    Index on XBR markets.
    """

    idx_markets_by_actor: IndexMarketsByActor
    """
    Index on XBR markets.
    """

    actors: Actors
    """
    XBR market actors.
    """

    accounts: Accounts
    """
    Member accounts database table :class:`xbrnetwork.Accounts`.
    """

    idx_accounts_by_username: IndexAccountsByUsername
    """
    Index "by username" of member accounts :class:`xbrnetwork.IndexAccountsByUsername`.
    """

    idx_accounts_by_email: IndexAccountsByEmail
    """
    Index "by email" of member accounts :class:`xbrnetwork.IndexAccountsByEmail`.
    """

    idx_accounts_by_wallet: IndexAccountsByWallet
    """
    Index "by wallet" of member accounts :class:`xbrnetwork.IndexAccountsByWallet`.
    """

    verified_actions: VerifiedActions
    """
    Verified actions database table :class:`xbrnetwork.VerifiedActions`.
    """

    user_keys: UserKeys
    """
    User client keys database table :class:`xbrnetwork.UserKeys`.
    """

    idx_user_key_by_account: IndexUserKeyByAccount
    """
    Index "by pubkey" of user keys :class:`xbrnetwork.IndexUserKeyByAccount`.
    """
    def __init__(self, db):
        self.db = db

    @staticmethod
    def attach(db):
        """
        Attach database schema to database instance.

        :param db: Database to attach schema to.
        :type db: :class:`zlmdb.Database`
        """
        schema = Schema(db)

        schema.attributes = db.attach_table(Attributes)

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

        schema.accounts = db.attach_table(Accounts)

        schema.idx_accounts_by_username = db.attach_table(IndexAccountsByUsername)
        schema.accounts.attach_index('idx1', schema.idx_accounts_by_username,
                                     lambda account: account.username)

        schema.idx_accounts_by_email = db.attach_table(IndexAccountsByEmail)
        schema.accounts.attach_index('idx2', schema.idx_accounts_by_email, lambda account: account.email)

        schema.idx_accounts_by_wallet = db.attach_table(IndexAccountsByWallet)
        schema.accounts.attach_index('idx3', schema.idx_accounts_by_wallet,
                                     lambda account: account.wallet_address)

        schema.verified_actions = db.attach_table(VerifiedActions)

        schema.user_keys = db.attach_table(UserKeys)

        schema.idx_user_key_by_account = db.attach_table(IndexUserKeyByAccount)
        schema.user_keys.attach_index('idx1', schema.idx_user_key_by_account, lambda user_key:
                                      (user_key.owner, user_key.created))

        return schema
