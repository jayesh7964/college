from odoo import fields,api,models

class college_participant(models.Model):
    _name='college.event.participant'
    _description='College event participant'
    _sql_constraints = [
        ('check_number_of_participant', 'CHECK(number_of_participant >= 0 AND number_of_participant <= 65)',
         'The number_of_participant should be between 0 and 100.')
    ]

    event_id = fields.Many2one(comodel_name='college.event',string='Event name')
    number_of_participant = fields.Integer(string='Number of participants')
    event_regi_id = fields.Many2one(comodel_name='college.event.registration',string='Winner name')



