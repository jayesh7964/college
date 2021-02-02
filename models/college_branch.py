from odoo import fields,api,models

class collegebranch(models.Model):
    _name='college.branch'
    _description='College Branch'
    _sql_constraints = [
        ('col-branch', 'unique (name)', 'The name of the branch must be unique!')

    ]

    name = fields.Char(string='Branch name')    #help='name of branch',required='True',size=10)
    code = fields.Char(string='Branch code')
    contact_person = fields.Char(string='Contact person')
    contact = fields.Char(string='Contact number')  #copy=False

    staff_count = fields.Integer(string='staff member', compute='get_staff_count')

    def btn_staff(self):
        return {
            'name': 'branch of staff',
            'type': 'ir.actions.act_window',
            'res_model': 'college.staff',
            'view_mode': 'tree,form',
            'domain':[('branch_id','=',self.id)],
        }

    def get_staff_count(self):
        count = self.env['college.staff'].search_count([('branch_id', '=', self.id)])
        self.staff_count = count


    # ============================== ORM name_get ======================================
    # def name_get(self):
    #     print("=================================name_get==========================")
    #     result = []
    #     for i in self:
    #         a = i.name+" : "+i.code
    #         result.append((i.id,a))
    #     return result

    # ============================== ORM name_search ======================================
    # @api.model
    # def name_search(self, name='', args=None, operator='ilike', limit=100):
    #     print("============================= name_search ============================")
    #     # domain = ['|',('name',operator,name),('code',operator,name)]
    #     # args += domain
    #     args = ['|',('name',operator,name),('contact_person',operator,name)]
    #     a = self.search(args,limit=limit)
    #     return a.name_get()


