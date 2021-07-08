# -*- coding: utf-8 -*-

from odoo import models, fields, api


# class module_talgat(models.Model):
#     _name = 'module_talgat.module_talgat'
#     _description = 'module_talgat.module_talgat'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
class absence_views(models.Model):
    _description = 'absence_views'
    _name = 'absence_views'
    reason = fields.Text()
    name=fields.Char(string='Name',required=True)
    user = fields.Many2one('res.users', string='user')
    date_from = fields.Date()
    date_to = fields.Date()
    state=fields.Selection([
        ('draft', 'Draft'),
        ('submit','Submit'),
        ('rejected','Rejected'),

    ],readonly=True,string='Status',default='draft')

    def action_submit(self):
        for rec in self:
            rec.state='submit'




    def action_rejected(self):
         self.state='rejected'