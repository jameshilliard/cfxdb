##############################################################################
#
#                        Crossbar.io FX
#     Copyright (C) Crossbar.io Technologies GmbH. All rights reserved.
#
##############################################################################

import uuid

from zlmdb import table
from zlmdb import MapStringUuid, MapUuidCbor, MapSlotUuidUuid, MapUuidStringUuid, MapUuidUuidUuid
from zlmdb import MapUuidUuidCbor, MapUuidUuidUuidStringUuid

from cfxdb.mrealm import RouterCluster, WebCluster, WebService, WebClusterNodeMembership, RouterClusterNodeMembership, parse_webservice, RouterWorkerGroup, RouterWorkerGroupClusterPlacement
from cfxdb.mrealm import ApplicationRealm, Role, ApplicationRealmRoleAssociation
from cfxdb.log import MNodeLogs, MWorkerLogs

__all__ = ('MrealmSchema', )


#
# Application Realms
#
@table('7099565b-7b44-4891-a0c8-83c7dbb60883', marshal=ApplicationRealm.marshal, parse=ApplicationRealm.parse)
class ApplicationRealms(MapUuidCbor):
    """
    Table: arealm_oid -> arealm
    """


@table('89f3073a-32d5-497e-887d-7e930e9c26e6')
class IndexApplicationRealmByName(MapStringUuid):
    """
    Index: arealm_name -> arealm_oid
    """


#
# Roles
#
@table('341083bb-edeb-461c-a6d4-38dddcda6ec9', marshal=Role.marshal, parse=Role.parse)
class Roles(MapUuidCbor):
    """
    Table: role_oid -> role
    """


@table('71b990d1-4525-44cd-9ef8-3569de8b4c80')
class IndexRoleByName(MapStringUuid):
    """
    Index: role_name -> role_oid
    """


#
# Application Realm Role Associations
#
@table('5eabdb63-9c31-4c97-b514-7e8fbac7e143',
       marshal=ApplicationRealmRoleAssociation.marshal,
       parse=ApplicationRealmRoleAssociation.parse)
class ApplicationRealmRoleAssociations(MapUuidUuidCbor):
    """
    Table: (arealm_oid, role_oid) -> arealm_role_association
    """


#
# Router clusters
#
@table('b054a230-c370-4c29-b5de-7e0148321b0a', marshal=RouterCluster.marshal, parse=RouterCluster.parse)
class RouterClusters(MapUuidCbor):
    """
    Table: routercluster_oid -> routercluster
    """


@table('0c80c7a8-7536-4a74-8916-4922c0b72cb7')
class IndexRouterClusterByName(MapStringUuid):
    """
    Index: routercluster_name -> routercluster_oid
    """


#
# Router cluster node memberships
#
@table('a091bad6-f14c-437c-8e30-e9be84380658',
       marshal=RouterClusterNodeMembership.marshal,
       parse=RouterClusterNodeMembership.parse)
class RouterClusterNodeMemberships(MapUuidUuidCbor):
    """
    Table: (cluster_oid, node_oid) -> cluster_node_membership
    """


#
# Router worker groups
#
@table('c019457b-d499-454f-9bf2-4f7e85079d8f',
       marshal=RouterWorkerGroup.marshal,
       parse=RouterWorkerGroup.parse)
class RouterWorkerGroups(MapUuidCbor):
    """
    Table: workergroup_oid -> workergroup
    """


@table('4bb8ec14-4820-4061-8b2c-d1841e2686e1')
class IndexWorkerGroupByCluster(MapUuidStringUuid):
    """
    Index: cluster_oid, workergroup_name -> workergroup_oid
    """


#
# Router worker groups to cluster node placements
#
@table('e3d326d2-6140-47a9-adf9-8e93b832717b',
       marshal=RouterWorkerGroupClusterPlacement.marshal,
       parse=RouterWorkerGroupClusterPlacement.parse)
class RouterWorkerGroupClusterPlacements(MapUuidCbor):
    """
    Table: placement_oid -> placement
    """


@table('1a18739f-7224-4459-a446-6f1fedd760a7')
class IndexClusterPlacementByWorkerName(MapUuidUuidUuidStringUuid):
    """
    Index: (workergroup_oid, cluster_oid, node_oid, worker_name) -> placement_oid
    """


#
# Web clusters
#
@table('719d029f-e9d5-4b25-98e0-cf04d5a2648b', marshal=WebCluster.marshal, parse=WebCluster.parse)
class WebClusters(MapUuidCbor):
    """
    Table: webcluster_oid -> webcluster
    """


@table('296c7d17-4769-4e40-8cb7-e6c394b93335')
class IndexWebClusterByName(MapStringUuid):
    """
    Index: webcluster_name -> webcluster_oid
    """


#
# Web cluster node memberships
#
@table('e9801077-a629-470b-a4c9-4292a1f00d43',
       marshal=WebClusterNodeMembership.marshal,
       parse=WebClusterNodeMembership.parse)
class WebClusterNodeMemberships(MapUuidUuidCbor):
    """
    Table: (webcluster_oid, node_oid) -> webcluster_node_membership
    """


#
# Web cluster services
#
@table('a8803ca3-09a0-4d72-8728-2469de8d50ac', marshal=WebService.marshal, parse=parse_webservice)
class WebServices(MapUuidCbor):
    """
    Table: webservice_oid -> webservice
    """


@table('d23d4dbb-5d5c-4ccc-b72a-0ff18363169f')
class IndexWebClusterWebServices(MapUuidUuidUuid):
    """
    Index: (webcluster_oid, webservice_oid) -> webservice_oid
    """


@table('f0b05bcf-f682-49bb-929e-ac252e9867fa')
class IndexWebServiceByPath(MapUuidStringUuid):
    """
    Index: (webcluster_oid, webservice_name) -> webservice_oid
    """


@table('62d0841c-602e-473e-a6d5-3d8ce01e9e06')
class IndexWebClusterPathToWebService(MapUuidStringUuid):
    """
    Index: (webcluster_oid, path) -> webservice_oid
    """


#
# Docs metadata
#
@table('e11680d5-e20c-40b1-97d9-380b5ace1cb3', marshal=(lambda x: x), parse=(lambda x: x))
class Docs(MapUuidCbor):
    """
    Table: doc_oid -> doc
    """


@table('d1de0b8c-3b6d-488b-8778-5bac8528ab4b')
class IndexObjectToDoc(MapSlotUuidUuid):
    """
    Index: (object_slot, object_oid) -> doc_oid
    """


class MrealmSchema(object):
    """
    Management realm database schema.
    """
    def __init__(self, db):
        self.db = db

    # arealms: ApplicationRealm
    arealms = None
    """
    """

    # roles: Role
    roles = None
    """
    """

    # idx_roles_by_name: IndexRolesByName
    idx_roles_by_name = None

    # idx_arealms_by_name: IndexApplicationRealmByName
    idx_arealms_by_name = None
    """
    """

    # arealm_role_associations: ApplicationRealmRoleAssociation
    arealm_role_associations = None
    """
    """

    # routerclusters: RouterClusters
    routerclusters = None
    """
    """

    # idx_routerclusters_by_name: IndexRouterClusterByName
    idx_routerclusters_by_name = None
    """
    """

    # routercluster_node_memberships: RouterClusterNodeMemberships
    routercluster_node_memberships = None
    """
    """

    # router_workergroups: RouterWorkerGroups
    router_workergroups = None
    """
    """

    # idx_workergroup_by_cluster: IndexWorkerGroupByCluster
    idx_workergroup_by_cluster = None
    """
    """

    # router_workergroup_placements: RouterWorkerGroupClusterPlacements
    router_workergroup_placements = None
    """
    """

    # idx_clusterplacement_by_workername: IndexClusterPlacementByWorkerName
    idx_clusterplacement_by_workername = None
    """
    """

    # webclusters: WebClusters
    webclusters = None
    """
    """

    # idx_webclusters_by_name: IndexWebClusterByName
    idx_webclusters_by_name = None
    """
    """

    # webcluster_node_memberships: WebClusterNodeMemberships
    webcluster_node_memberships = None
    """
    """

    # webservices: WebServices
    webservices = None
    """
    """

    # idx_webservices_by_path: IndexWebServiceByPath
    idx_webservices_by_path = None
    """
    """

    # idx_webcluster_path_to_service: IndexWebClusterPathToWebService
    idx_webcluster_path_to_service = None
    """
    """

    # idx_node_to_webclusters: IndexNodeToWebClusters
    idx_node_to_webclusters = None
    """
    """

    # idx_webcluster_to_nodes: IndexWebClusterToNodes
    idx_webcluster_to_nodes = None
    """
    """

    # docs: Docs
    docs = None
    """
    """

    # idx_object_to_doc: IndexObjectToDoc
    idx_object_to_doc = None
    """
    """

    # mnode_logs: MNodeLogs
    mnode_logs = None
    """
    Managed node log records.
    """

    # mworker_logs: MWorkerLogs
    mworker_logs = None
    """
    Managed node worker log records.
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
        schema = MrealmSchema(db)

        # application realms
        schema.arealms = db.attach_table(ApplicationRealms)
        schema.idx_arealms_by_name = db.attach_table(IndexApplicationRealmByName)

        schema.roles = db.attach_table(Roles)
        schema.idx_roles_by_name = db.attach_table(IndexRoleByName)

        schema.arealm_role_associations = db.attach_table(ApplicationRealmRoleAssociations)

        # router clusters
        schema.routerclusters = db.attach_table(RouterClusters)

        schema.idx_routerclusters_by_name = db.attach_table(IndexRouterClusterByName)
        schema.routerclusters.attach_index('idx1', schema.idx_routerclusters_by_name,
                                           lambda routercluster: routercluster.name)

        schema.routercluster_node_memberships = db.attach_table(RouterClusterNodeMemberships)

        # router worker groups
        schema.router_workergroups = db.attach_table(RouterWorkerGroups)

        schema.idx_workergroup_by_cluster = db.attach_table(IndexWorkerGroupByCluster)
        schema.router_workergroups.attach_index('idx1', schema.idx_workergroup_by_cluster, lambda wg:
                                                (wg.cluster_oid, wg.name))

        schema.idx_clusterplacement_by_workername = db.attach_table(IndexClusterPlacementByWorkerName)
        schema.router_workergroups.attach_index(
            'idx2', schema.idx_clusterplacement_by_workername, lambda wg:
            (wg.oid, wg.cluster_oid, uuid.UUID(bytes=b'\x00' * 16), ''))

        schema.router_workergroup_placements = db.attach_table(RouterWorkerGroupClusterPlacements)

        # web clusters
        schema.webclusters = db.attach_table(WebClusters)

        schema.idx_webclusters_by_name = db.attach_table(IndexWebClusterByName)
        schema.webclusters.attach_index('idx1', schema.idx_webclusters_by_name,
                                        lambda webcluster: webcluster.name)

        schema.webcluster_node_memberships = db.attach_table(WebClusterNodeMemberships)

        # web services
        schema.webservices = db.attach_table(WebServices)

        schema.idx_webservices_by_path = db.attach_table(IndexWebServiceByPath)
        schema.webservices.attach_index('idx1', schema.idx_webservices_by_path, lambda webservice:
                                        (webservice.webcluster_oid, webservice.path))

        schema.idx_webcluster_webservices = db.attach_table(IndexWebClusterWebServices)
        schema.webservices.attach_index('idx2', schema.idx_webcluster_webservices, lambda webservice:
                                        (webservice.webcluster_oid, webservice.oid))

        schema.mnode_logs = db.attach_table(MNodeLogs)
        schema.mworker_logs = db.attach_table(MWorkerLogs)

        return schema
