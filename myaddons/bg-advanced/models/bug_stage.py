# -*- coding: utf-8 -*-

from odoo import models, fields, api

class bugStage(models.Model):
    _name = 'bm.bug.stage'
    _description = 'bug阶段'
    _order = 'sequence,name'

    name =fields.Char('名称')
    desc_detail=fields.Text('描述')
    status=fields.Selection([('waiting','未开始'),('doing','进行中'),('closed','关闭'),('rework','重测未通过')],'状态')
    document=fields.Html('文档')
    percent_pro=fields.Float('进度',(3,2))
    deadline=fields.Date('最晚解决日期')
    create_on=fields.Datetime('创建时间',default=lambda self:fields.Datetime.now())
    delay=fields.Boolean('是否延迟')
    image=fields.Binary('图片')
    sequence =fields.Integer('Sequence')

    bugs_ids=fields.One2many('bm.bug','stage_id',string='bug')