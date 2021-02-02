from odoo import fields,api,models

class collegeevent_category(models.Model):
    _name='college.event.category'
    _description='College event category'

    _rec_name = "category"
    category = fields.Char(string='Event type')



