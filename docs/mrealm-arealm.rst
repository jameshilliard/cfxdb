Application Realm
=================

.. contents:: :local:

--------------


Application Realm Tables
------------------------

arealms
.......

.. autoclass:: cfxdb.mrealm.ApplicationRealm

.. autoclass:: cfxdb.mrealmschema.ApplicationRealms

idx_arealms_by_name
...................

.. autoclass:: cfxdb.mrealmschema.IndexApplicationRealmByName

idx_arealm_by_webcluster
........................

.. autoclass:: cfxdb.mrealmschema.IndexApplicationRealmByWebCluster

arealm_role_associations
........................

.. autoclass:: cfxdb.mrealm.ApplicationRealmRoleAssociation

.. autoclass:: cfxdb.mrealmschema.ApplicationRealmRoleAssociations


Principal Tables
----------------

principals
..........

.. autoclass:: cfxdb.mrealmschema.Principal

.. autoclass:: cfxdb.mrealmschema.Principals

idx_principals_by_name
......................

.. autoclass:: cfxdb.mrealmschema.IndexPrincipalByName


Credentials Tables
------------------

credentials
...........

.. autoclass:: cfxdb.mrealmschema.Credential

.. autoclass:: cfxdb.mrealmschema.Credentials

idx_credentials_by_auth
.......................

.. autoclass:: cfxdb.mrealmschema.IndexCredentialsByAuth

idx_credentials_by_principal
............................

.. autoclass:: cfxdb.mrealmschema.IndexCredentialsByPrincipal


Role Tables
-----------

roles
.....

.. autoclass:: cfxdb.mrealm.Role

.. autoclass:: cfxdb.mrealmschema.Roles

idx_roles_by_name
.................

.. autoclass:: cfxdb.mrealmschema.IndexRoleByName


Permissions Table
-----------------

permissions
...........

.. autoclass:: cfxdb.mrealm.Permission

.. autoclass:: cfxdb.mrealmschema.Permissions

idx_permissions_by_uri
......................

.. autoclass:: cfxdb.mrealmschema.IndexPermissionByUri
