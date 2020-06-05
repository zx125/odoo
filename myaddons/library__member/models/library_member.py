from odoo import fields, models


class Member(models.Model):
    _name = 'library.member'
    _description = 'Library Member'
    card_number = fields.Char()
    _inherit = ['mail.thread', 'mail.activity.mixin']
    partner_id = fields.Many2one(
        'res.partner',
        delegate=True,
        ondelete='cascade',
        required=True)