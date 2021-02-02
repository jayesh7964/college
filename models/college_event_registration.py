from odoo import fields,api,models

class collegeevent_registration(models.Model):
    _name='college.event.registration'
    _description='College event registration'

    name = fields.Many2one(comodel_name='college.student',string='Student name')    #help='name of branch',required='True',size=10)
    semester = fields.Many2one(comodel_name='college.semester',related='name.semester_id',string='Semester')
    branch = fields.Many2one(comodel_name='college.branch',related='name.branch_id',string='Branch')



    # event_reg_id = fields.Many2one(comodel_name='college.event')




