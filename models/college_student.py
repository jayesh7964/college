from odoo import fields,api,models

class collegestudent(models.Model):
    _name='college.student'
    _description = 'College Student'

    name = fields.Char(string='Student name')
    student_code = fields.Integer(string='Student code')
    birthdate = fields.Date(string='D.O.B')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
    ], string='Gender',default='male')
    contact = fields.Char(string='Contact number')
    email=fields.Char(string="Email")
    image = fields.Binary(string='image')
    adress=fields.Text(string='Adress')
    state=fields.Many2one('res.country.state',string='State')
    country=fields.Many2one('res.country',string='Country')
    semester_id=fields.Many2one(comodel_name='college.semester', string='Semester')
    branch_id = fields.Many2one(comodel_name='college.branch', string='Branch')

    #============================Recordset==================================

    # ==========================self=============================
    # def btn_self(self):
    #     print("===============self=============",self)
    #     print("===============self.env=============",self.env)
    #     print("===============self.env.context=============",self.env.context)
    #     print("===============self.env.context.get('uid')=============",self.env.context.get('uid'))

    # ========================== Search in RS =============================
    # def btn_self(self):
        # print("======================= creating blank RS ====================")
        # record = self.env['college.student']
        # print("======================= blank RS print ====================",record)

        # record = self.env['college.student'].search([])
        # print("======================= RS print with search method ====================",record)

        # record = self.env['college.student'].search([('contact','=','9409075044')])
        # for rec in record:
        #     print(rec.name)
        # print("======================= RS print with search method ====================",record)

    # ========================== Browse in RS =============================
    # def btn_self(self):
    #     record = self.env['college.student'].browse([1,3])
    #     for rec in record:
    #         print(rec.name,rec.contact)
    #     print("======================= RS print with browse method ====================",record)

    # ========================== Mapped in RS =============================
    def btn_mapped(self):
            record = self.env['college.student'].search([]).mapped('branch_id.name')
            print("======================= RS print with mapped method ====================", record)

    # ========================== Filtered in RS =============================
    def btn_filter(self):
        record = self.env['college.student'].search([]).filtered(lambda a:a.name=='akki')
        # for rec in record:
        #     print(rec.contact,rec.branch_id.name)
        print("======================= RS print with filtered method ====================", record)

    # ========================== Sorted in RS =============================
    def btn_sorted(self):
        record = sorted(self.env['college.student'].search([]).filtered(lambda a:a.branch_id.name=='IT').mapped('name'))
        # record = self.env['college.student'].search([]).sorted('name')
        print("======================= RS print with sorted method ====================", record)

    #===================================================================================================

    #=============================ORM Method======================================================

    #==================================== default_get method ===========================================
    @api.model
    def default_get(self, fields_list):
        print("======================= default get called ====================")
        print("======================= field_list ====================",fields_list)
        res = super(collegestudent,self).default_get(fields_list)
        print("======================= after super call res ====================")
        print("======================= res ====================",res)
        return res

    # ==================================== search method ===========================================
    # @api.model
    # def search(self, args, offset=0, limit=None, order=None, count=False):
    #     args = [('name','=','jayesh')]
    #     print("======================= search args ====================",args)
    #     res = super(collegestudent,self).search(args=args,offset=offset, limit=2, order='name desc', count=False)
    #     print("======================= after super call res ====================")
    #     print("======================= res ====================",res)
    #     return res

    # ========================== Search_count in RS =============================
    # def btn_self(self):
        # print("======================= creating blank RS ====================")
        # record = self.env['college.student']
        # print("======================= blank RS print ====================",record)

        # record = self.env['college.student'].search_count([])
        # print("======================= RS print with search_count method ====================",record)

        # record = self.env['college.student'].search_count([('name','=','viren')])
        # print("======================= RS print with search method ====================",record)

    # ==================================== search_read method ===========================================
    # @api.model
    # def search_read(self, domain=None, fields=None, offset=0, limit=None, order=None):
    #     print("======================= search read called ====================")
    #     print("======================= field ====================",fields)
    #     res = super(collegestudent,self).search_read(domain=[('name','=','jayesh')],fields=['name','gender'],offset=offset, limit=2, order='name desc')
    #     # res = super(collegestudent,self).search_read(domain=[('name','=','jayesh')],fields=fields,offset=offset, limit=2, order='name desc')
    #     # res = super(collegestudent,self).search_read(domain=None,fields=['name','gender'],offset=offset, limit=2, order='name desc')
    #     print("======================= after super call res ====================")
    #     print("======================= res ====================",res)
    #     return res

    # ==================================== create method ===========================================
    # @api.model
    # def create(self, vals):
    #     print("======================= create called ====================")
    #     print("======================= vals_list ====================",vals)
    #     vals['student_code']=50
    #     res = super(collegestudent,self).create(vals_list=vals)
    #     print("======================= after super call res ====================")
    #     print("======================= res ====================",res)
    #     return res

    # ==================================== unlink method ===========================================
    # def unlink(self):
    #     print("======================= unlink called ====================")
    #     res = super(collegestudent,self).unlink()
    #     print("======================= res ====================",res)
    #     return res

    # ==================================== write method ===========================================
    # def write(self, vals1):
    #     print("======================= write called ====================")
    #     print("======================= vals ====================",vals1)
    #     # for rec in self:
    #     #     if rec.name=='jayesh':
    #     #         vals1['student_code']=55
    #     # print("======================= vals ====================", vals1)
    #     # vals1.update({'name':'viren'})
    #     res = super(collegestudent,self).write(vals=vals1)
    #     print("======================= res ====================",res)
    #     return res

    # ==================================== copy method ===========================================
    # def copy(self, default=None):
    #     print("======================= copy called ====================")
    #     # default1 = {}
    #     # default1['name']='Jinkal'
    #     # res = super(collegestudent,self).copy(default=default1)
    #     res = super(collegestudent,self).copy(default=None)
    #     print("======================= res ====================",res)
    #     return res

    # ==================================== read_group method ===========================================
    # @api.model
    # def read_group(self, domain, fields, groupby, offset=0, limit=None, orderby=False, lazy=True):
    #     print("===========================read group called=========================")
    #     print("===========================read group called=========================",fields)
    #     # res = super(collegestudent,self).read_group(domain=[('name','=','nishant')],fields=['contact'],offset=offset,groupby=groupby, limit=limit, orderby=orderby,lazy=True)
    #     res = super(collegestudent,self).read_group(domain=domain,fields=fields,offset=offset,groupby=groupby, limit=limit, orderby=orderby,lazy=lazy)
    #     print("==================================== res =============================",res)
    #     for i in res:
    #         print(i)
    #     return res

    # ==================================== fields_view_get method ===========================================
    # @api.model
    # def fields_view_get(self, view_id='view_college_student_tree', view_type='tree', toolbar=False, submenu=False):
    #     print("======================= fields_view_get called ====================")
    #     res = super(collegestudent,self).fields_view_get(view_id=view_id,view_type=view_type,toolbar=False, submenu=False)
    #
    #     res['fields']['name']['sortable']=False
    #     print("======================= res ====================",res)
    #     return res
