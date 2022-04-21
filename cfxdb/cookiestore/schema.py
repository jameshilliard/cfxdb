##############################################################################
#
#                        Crossbar.io Database
#     Copyright (c) Crossbar.io Technologies GmbH. Licensed under MIT.
#
##############################################################################

import zlmdb
from cfxdb.cookiestore.cookie import Cookies


class Schema(object):
    """
    """
    def __init__(self, db):
        self.db = db

    cookies: Cookies
    """
    """

    @staticmethod
    def attach(db: zlmdb.Database) -> 'Schema':
        """
        Factory to create a schema from attaching to a database. The schema tables
        will be automatically mapped as persistent maps and attached to the
        database slots.
        """
        schema = Schema(db)

        schema.cookies = db.attach_table(Cookies)

        return schema
