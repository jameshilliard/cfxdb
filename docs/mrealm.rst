Management Realm
================

Each management realm controller running on the master node stores its configuration and run-time
information in an embedded database.

.. note::

    Each management realm has its own dedicated management realm controller database. This database
    is separate for each management realm and not accessed by any other management realm controller.

---------

.. toctree::
    :maxdepth: 3

    mrealm-arealm
    mrealm-routercluster
    mrealm-webcluster


Database Schema
---------------

.. autoclass:: cfxdb.mrealmschema.MrealmSchema
    :members:
        attach,
        roles,
        idx_roles_by_name,
        permissions,
        idx_permissions_by_uri,
        arealms,
        idx_arealms_by_name,
        idx_arealm_by_webcluster,
        arealm_role_associations,
        principals,
        idx_principals_by_name,
        credentials,
        idx_credentials_by_auth,
        idx_credentials_by_principal,
        routerclusters,
        idx_routerclusters_by_name,
        routercluster_node_memberships,
        router_workergroups,
        idx_workergroup_by_cluster,
        router_workergroup_placements,
        idx_clusterplacement_by_workername,
        webclusters,
        idx_webclusters_by_name,
        webcluster_node_memberships,
        webservices,
        idx_webservices_by_path,
        mnode_logs,
        mworker_logs

Node and Worker Log Tables
--------------------------

mnode_logs
..........

.. autoclass:: cfxdb.log.mnode_log.MNodeLog

.. autoclass:: cfxdb.log.mnode_logs.MNodeLogs

mworker_logs
............

.. autoclass:: cfxdb.log.mworker_log.MWorkerLog

.. autoclass:: cfxdb.log.mworker_logs.MWorkerLogs

Cluster Tables
--------------

.. autoclass:: cfxdb.mrealm.Cluster

.. autoclass:: cfxdb.mrealm.ClusterNodeMembership
