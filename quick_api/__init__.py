# -*- coding: utf-8 -*-
"""
/***************************************************************************
 QuickApi
                                 A QGIS plugin
 This plugin queries Open Elevation API
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2020-06-17
        copyright            : (C) 2020 by Ciaran Evans
        email                : an-email@com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load QuickApi class from file QuickApi.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .quick_api import QuickApi
    return QuickApi(iface)
