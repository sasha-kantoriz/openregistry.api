# -*- coding: utf-8 -*-
from pyramid.interfaces import IRequest
from openregistry.api.interfaces import IContentConfigurator
from .models import IResource, DummyTestResource
from .adapters import DummyTestResourceConfigurator


def includeme(config):
    config.add_resourceType(DummyTestResource)
    config.registry.registerAdapter(DummyTestResourceConfigurator,
                                    (IResource, IRequest),
                                    IContentConfigurator)
