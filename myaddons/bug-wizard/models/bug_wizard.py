from odoo import models, fields, api

class bugWizard(models.TransientModel):
    _name='bug.wizard'
    bug_ids=fields.Many2many('bm.bug',string='Bug')
    new_is_closed=fields.Boolean('是否关闭')
    wizard_user_id=fields.Many2one('res.user',string='负责人')