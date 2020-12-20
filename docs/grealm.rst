Global Domain
=============

The domain controller running on the master node stores its configuration and run-time
information in an embedded database

.. contents:: :local:

.. note::

    There exists only one domain controller database per master node. This database is separate
    from all managament realm controller databases, and only used to book keep users, Management
    realms and paired nodes. All configuration and management within a given management realm is
    then stored in the management realm controller database dedicated to the respective realm.

-------


Database Schema
---------------

.. autoclass:: cfxdb.globalschema.GlobalSchema
    :members:
        attach,
        nodes,
        idx_nodes_by_pubkey,
        idx_nodes_by_authid,
        organizations,
        idx_organizations_by_name,
        idx_users_by_pubkey,
        idx_users_by_email,
        activation_tokens,
        idx_act_tokens_by_authid_pubkey,
        mrealms,
        idx_mrealms_by_name,
        users,
        users_mrealm_roles,
        usage


Metadata Tables
---------------

.. autoclass:: cfxdb.common.ConfigurationElement



User Tables
-----------

.. autoclass:: cfxdb.user.User

.. autoclass:: cfxdb.globalschema.Users

.. autoclass:: cfxdb.globalschema.IndexUsersByName

.. autoclass:: cfxdb.globalschema.IndexUsersByPubkey

.. autoclass:: cfxdb.globalschema.IndexUsersByEmail

.. autoclass:: cfxdb.user.UserMrealmRole

.. autoclass:: cfxdb.globalschema.UserMrealmRoles

.. autoclass:: cfxdb.user.ActivationToken

.. autoclass:: cfxdb.globalschema.ActivationTokens

.. autoclass:: cfxdb.globalschema.IndexActivationTokensByAuthidPubkey


Organization Tables
-------------------

.. autoclass:: cfxdb.user.Organization

.. autoclass:: cfxdb.globalschema.Organizations

.. autoclass:: cfxdb.globalschema.IndexOrganizationsByName


Management Realm Tables
-----------------------

.. autoclass:: cfxdb.mrealm.ManagementRealm

.. autoclass:: cfxdb.globalschema.ManagementRealms

.. autoclass:: cfxdb.globalschema.IndexManagementRealmByName


Node Tables
-----------

.. autoclass:: cfxdb.mrealm.Node

.. autoclass:: cfxdb.globalschema.Nodes

.. autoclass:: cfxdb.globalschema.IndexNodesByPubkey

.. autoclass:: cfxdb.globalschema.IndexNodesByAuthid

.. autoclass:: cfxdb.usage.MasterNodeUsage
    :members:

.. autoclass:: cfxdb.globalschema.UsageRecords


