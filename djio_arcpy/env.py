#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. currentmodule:: djio_arcpy.env
.. moduleauthor:: Pat Daburu <pat@daburu.net>

Manage your arcpy environments at runtime.
"""
from typing import Any, Dict
import arcpy


class Environment(object):
    """
    This is a wrapper class for the `arcpy.env <https://bit.ly/2J90NLf>`_
    global.
    """
    __rwattrs__ = {
        'addOutputsToMap': bool,
        'autoCancelling': bool,
        'autoCommit': int,
        'baDataSource': str,
        'buildStatsAndRATForTempRaster': bool,
        'cartographicCoordinateSystem': str,
        'cartographicPartitions': str,
        'cellSize': str,
        'coincidentPoints': str,
        'compression': str,
        'configKeyword': str,
        'extent': str,
        'geographicTransformations': str,
        'maintainAttachments': bool,
        'maintainSpatialIndex': bool,
        'mask': str,
        'MDomain': str,
        'MResolution': float,
        'MTolerance': float,
        'nodata': str,
        'outputCoordinateSystem': str,
        'outputMFlag': str,
        'outputZFlag': str,
        'outputZValue': str,
        'overwriteOutput': bool,
        'parallelProcessingFactor': int,
        'processingServer': str,
        'processingServerPassword': str,
        'processingServerUser': str,
        'pyramid': str,
        'qualifiedFieldNames': bool,
        'randomGenerator': Any,
        'rasterStatistics': str,
        'referenceScale': float,
        'resamplingMethod': str,
        'scratchWorkspace': str,
        'snapRaster': str,
        'S100FeatureCatalogueFile': str,
        'terrainMemoryUsage': bool,
        'tileSize': str,
        'tinSaveVersion': str,
        'transferDomains': bool,
        'transferGDBAttributeProperties': bool,
        'workspace': str,
        'XYDomain': str,
        'XYResolution': str,
        'XYTolerance': str,
        'ZDomain': str,
        'ZResolution': str,
        'ZTolerance': str
    }  #: the arcpy environment variables that can be written an read

    __roattrs__ = {
        'isCancelled': bool,
        'packageWorkspace': str,
        'scratchFolder': str,
        'scratchGDB': str,
        'scriptWorkspace': str
    }  #: the arcpy environment variables that can only be read

    def __init__(self):
        self._outer: Dict[str, Any] = {

        }  #: the outer environment variables
        self.mark()

    def mark(self):
        """
        Store the current `arcpy.env` settings that will be restored when the
        :py:func:`restore` method is called.
        """
        for att in self.__rwattrs__:
            self._outer[att] = getattr(arcpy.env, att)

    def restore(self):
        """
        Overwrite the current `arcpy.env` settings with those that were stored
        when the :py:func:`mark` method was called (at construction or on
        entry using `with`).
        """
        for att in self.__rwattrs__:
            setattr(arcpy.env, att, self._outer[att])

    def __enter__(self):
        self.mark()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.restore()
