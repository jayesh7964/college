from odoo import fields,api,models
from odoo.exceptions import ValidationError
# import datetime
class collegeprofessor(models.Model):
    _name='college.staff'
    _description = 'College Staff'


    name = fields.Char(string='Name')
    contact = fields.Char(string='Contact number')
    birthdate = fields.Date(string='D.O.B')
    email=fields.Char(string="Email")
    age=fields.Integer(string="Age")
    gender=fields.Selection([
        ('male','Male'),
        ('female','Female'),
    ],string='Gender')
    image=fields.Binary(string='image', attachment=False)
    adress=fields.Text(string='Adress')
    state = fields.Many2one('res.country.state', string='State')
    country = fields.Many2one('res.country', string='Country')
    position_id=fields.Many2one(comodel_name='college.job.position',string='Position')
    branch_id=fields.Many2one(comodel_name='college.branch',string='Branch')
    joining_date=fields.Date(string='Joining Date')     #,default=datetime.date.today()

    @api.constrains('age')
    def _check_age(self):
        for rec in self:
            if rec.age <23:
                raise ValidationError('you are not eligible')



