# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Nicolas Bessi
#    Copyright 2011-2012 Camptocamp SA
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp import fields, api

from openerp.addons.base_geoengine import geo_model
from openerp.addons.base_geoengine import fields as geo_fields


class NPA(geo_model.GeoModel):

    """GEO OSV SAMPLE"""

    _name = "dummy.zip"
    _inherit = ['mail.thread']
    _description = "Nouveau secteur"

    priority = fields.Integer('Priorité', default=100)
    name = fields.Char('Secteur', size=64, index=True, required=True, track_visibility='onchange')
    city = fields.Char('Ville', size=64, index=True, required=True, track_visibility='onchange')
    the_geom = geo_fields.GeoMultiPolygon('NPA Shape')
    total_sales = fields.Float('CA estimatif générale (en Ar)')
    affichage_list = fields.One2many('geoengine.demo.automatic.retailing.machine', 'secteur')

    def name_get(self, cursor, uid, ids, context=None):
        res = []
        for r in self.browse(cursor, uid, ids):
            res.append((r.id, u"%s %s" % (r.name, r.city)))
        return res
