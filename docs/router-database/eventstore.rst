Event Store
===========

.. contents:: :local:

-------------


Session
-------

* :class:`cfxdb.eventstore.Session`
* :class:`cfxdb.schema.Sessions`

-------

.. autoclass:: cfxdb.eventstore.Session
    :members:
    :undoc-members:
        session,
        joined_at,
        left_at,
        realm,
        authid,
        authrole
    :member-order: bysource

.. autoclass:: cfxdb.schema.Sessions
    :members:
    :show-inheritance:


Publication
-----------

* :class:`cfxdb.eventstore.Publication`
* :class:`cfxdb.schema.Publications`

-------

.. autoclass:: cfxdb.eventstore.Publication
    :members:
    :undoc-members:
        timestamp,
        publication,
        publisher,
        topic,
        args,
        kwargs,
        payload,
        acknowledge,
        retain,
        exclude_me,
        exclude,
        exclude_authid,
        exclude_authrole,
        eligible,
        eligible_authid,
        eligible_authrole,
        enc_algo,
        enc_key,
        enc_serializer
    :member-order: bysource

.. autoclass:: cfxdb.schema.Publications
    :members:
    :show-inheritance:


Publication
-----------

* :class:`cfxdb.eventstore.Event`
* :class:`cfxdb.schema.Events`

-------

.. autoclass:: cfxdb.eventstore.Event
    :members:
    :undoc-members:
        timestamp,
        subscription,
        publication,
        receiver,
        retained,
        acknowledged_delivery
    :member-order: bysource

.. autoclass:: cfxdb.schema.Events
    :members:
    :show-inheritance:
