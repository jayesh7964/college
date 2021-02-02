from odoo import fields,api,models

class collegejob_position(models.Model):
    _name='college.job.position'
    _description='College Job Position'

    name = fields.Char(string='Job Name')    #help='name of branch',required='True',size=10)
    code = fields.Char(string='Job code')



