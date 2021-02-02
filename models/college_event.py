from odoo import fields,api,models

class collegeevent(models.Model):
    _name='college.event'
    _description='College Event'


    name = fields.Char(string='Event Name')
    category_id=fields.Many2one(comodel_name='college.event.category',string='Category')
    manager = fields.Many2one(comodel_name='college.staff',string='Event manager')
    date = fields.Date(string='Date')
    duration = fields.Float(string='Duration')
    venue = fields.Text(string='Venue')
    entry_fees = fields.Float(string='Entry Fee')
    discount = fields.Integer(string='Discount(%)',default=10)
    actual_fees = fields.Float(string='Actual fees',compute='calc_actual_fees')
    # number_of_participant = fields.Integer(string='Number of participants')
    # event_regi_id = fields.Many2one(comodel_name='college.event.registration',string='Winner name')
    discription= fields.Text(string='Event discription')
    state = fields.Selection([
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
    ], string='state', default="pending")

    # event_regi_ids = fields.One2many(comodel_name='college.event.registration',inverse_name='event_reg_id',string='Participant Detail')

    def btn_confirm(self):
        self.state="confirmed"


    # def btn_pending(self):
    #     self.state="confirmed"

    def btn_cancel(self):
        self.state="pending"


    def calc_actual_fees(self):
        for rec in self:
            rec.actual_fees=rec.entry_fees -(rec.entry_fees*rec.discount)/100