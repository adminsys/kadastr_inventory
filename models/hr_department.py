# -*- coding: utf-8 -*-

#
#  (c) 2024 Adminsys
#  Auteur: Eric Arys
#  Tous droits réservés.
#
#  Ce fichier fait partie du module Kadastr développé pour Odoo.
#
#  Il est interdit de copier, distribuer ou modifier ce code sans
#  l'autorisation expresse de Adminsys.
#
#  Site Web: http://www.admnsys.be
#  Produit: Kadastr Inventory
#  Contact: eric.arys@adminsys.be
#

from odoo import fields, models, api


class ModelName(models.Model):
    _inherit = "hr.department"
    kadastr_inventory_set_ids = fields.One2many(comodel_name='kadastr.inventory.set', inverse_name='department_id',string='Computer set')
