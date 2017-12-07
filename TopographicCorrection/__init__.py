# -*- coding: utf-8 -*-
"""
/***************************************************************************
 TopographicCorrection
                                 A QGIS plugin
 This plugin is using for topgraphic correction
                             -------------------
        begin                : 2017-10-31
        copyright            : (C) 2017 by forests2020
        email                : forests2020@gmail.com
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
    """Load TopographicCorrection class from file TopographicCorrection.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .topo_corr import TopographicCorrection
    return TopographicCorrection(iface)
