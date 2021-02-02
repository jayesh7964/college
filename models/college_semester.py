from odoo import fields,api,models

class collegesemester(models.Model):
    _name='college.semester'
    _description='College Semester'

    name = fields.Char(string='Semester')
    code = fields.Char(string='Semester code')



