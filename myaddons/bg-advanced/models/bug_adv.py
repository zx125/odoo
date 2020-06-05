# -*- coding: utf-8 -*-

from odoo import models, fields, api

class bugAdvanced(models.Model):
    _inherit = 'bm.bug'
    need_time=fields.Integer('所需时间(小时)')
    name=fields.Char(help='简要描述发现的bug')
    stage_id=fields.Many2one('bm.bug.stage','阶段')
    tag_ids=fields.Many2many('bm.bug.tag',string='标示')

    @api.onchange('user_id')
    def user_follower_ref(self):
        if not self.user_id:
            self.follower_id = None
        return {
            'warning':{
                'title':'无负责人',
                'message':'关注者也被清空'
            }
        }