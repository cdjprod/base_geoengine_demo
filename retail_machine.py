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
import base64
import urllib
import os
import logging
from openerp import api, fields, models, exceptions, _
from openerp import tools
from openerp.addons.base_geoengine import geo_model
from openerp.addons.base_geoengine import fields as geo_fields

_logger = logging.getLogger(__name__)


class RetailMachine(geo_model.GeoModel):
    """GEO OSV SAMPLE"""

    _name = "geoengine.demo.automatic.retailing.machine"
    _inherit = ['mail.thread']
    _description = "Nouveau site"

    the_point = geo_fields.GeoPoint('Coordinate')
    the_line = geo_fields.GeoLine('Power supply line', index=True)
    total_sales = fields.Float('Total sale', index=False)
    money_level = fields.Char('Money level', size=32, index=True)
    state = fields.Selection([('hs', 'HS'),
                              ('ok', 'OK')],
                             'State',
                             index=True)
    name = fields.Char('Serial number', size=64, required=False)

###########       ##############      ##############################

    segment = fields.Char(string='Segment', required=False)
    description = fields.Char(string='Description', required=True, track_visibility='onchange')
    format_1 = fields.Char(string='Format', required=False)
    domaine = fields.Char(String='Domaine Activité')
    societe = fields.Char(string='Société', required=True)
    ville = fields.Char(string='Ville', required=True)
    secteur = fields.Many2one('dummy.zip', string='Secteur', required=False)
    localisation = fields.Char(string='Localisation', required=False)
    regisseur = fields.Char(string='Regisseur', required=False)
    type_1 = fields.Selection([('Point de vente', 'Point de vente'), ('Panneaux','Panneaux'), 
        ('Abri-bus', 'Abri-bus'), ('Roof-top', 'Roof-top'), ('Mur', 'Mur')],string='Type', index=True, required=True)


    date_refresh = fields.Date(string = 'Date de prochain rafraîchissement', required=False, index=True)
    date_suivie_debut = fields.Date(string="Date debut", default=fields.Date.today)
    date_suivie_fin = fields.Date(string="Date fin")
    active = fields.Boolean(string='Active', default=True)


    etat_visuel = fields.Selection([('bon', 'Bon'),('delave', 'Délavé'), ('dechire', 'Déchirée')], 
                string="Etat visuel", index=True, required=True, track_visibility='onchange')
    etat_support = fields.Selection([('bon', 'Bon'),('pied', 'Pied tordue'), ('panneaux', 'Panneaux tordue')], 
                string="Etat support", index=True, required=True, track_visibility='onchange')
    etat_production = fields.Selection([('fini', 'Fini'),('bc', 'BC en attente'), ('visuel', 'Visuel HD en attente')], 
                string="Etat de production", index=True, required=True, track_visibility='onchange')
    
    prix_loc = fields.Float('Valeur en location (en Ar)') 
    prix_taxe = fields.Float('Valeur taxe communale (en Ar)')
    prix_prod = fields.Float('Valeur production (en Ar)')


    image_visuel = fields.Binary(string="Visuel")
    image_pre = fields.Binary()
    image_loin = fields.Binary()
    ancien_visuel = fields.One2many('ancien.visuel.photo', 'ancien')
    color = fields.Char()
    icon = fields.Char('icon')

    @api.multi          
    def name_get(self):
        res = []
        for rec in self:
            res.append((rec.id, u"%s %s %s" % (rec.type_1, rec.description, rec.localisation)))
        return res