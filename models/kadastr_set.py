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
    _name = 'kadastr.inventory.set'
    _description = 'Set of computer objects'

    name = fields.Char()
    activate = fields.Boolean(default=True)
    department_id = fields.Many2one(comodel_name='hr.department', string='Department')
    owner_id = fields.Many2one(comodel_name='hr.employee', string='Employee')
