from odoo import models, fields, api


class HrApplicant(models.Model):
    _inherit = 'hr.applicant'
    sex = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('unknown', 'Unknown'),

    ], readonly=True, string='Sex')

    nationality = fields.Char(string='Nationality')

    bdate = fields.Date(string='Birthday')

    citizenship = fields.Char(string='Citizenship')

    marital_status = fields.Char(string='Marital status')

    work_place = fields.Char(string='Work place')

    position = fields.Text(string='Job positon')

    term_work = fields.Char(string='Term of work')

    desc = fields.Text(string='Description ')



    education_uni = fields.Char(string='Education')

    specialty = fields.Char(string='Specialty')

    receipt_date = fields.Date(string='Receipt date')

    end_date = fields.Date(string='End date')

    responsible = fields.Many2one('hr.employee', string='Responsible')



    interviewer = fields.Char(string='Interviewer')
    @api.onchange('stage_id')
    def _get_hide(self):
        if int(self.stage_id) < 3:
            self.interviewer = self.responsible.name
        if int(self.stage_id) >= 3:
            self.interviewer = self.department_id.manager_id.name



# manager=fields.Many2one('hr.employee', string='Manager')
    # def action_offer(self):
    #     self.state = 'offer'
    #
    # def action_offerdelayed(self):
    #     self.state = 'offerdelayed'


from odoo import models, fields, api
#
# class MaintenanceView(models.Model):
#     _inherit = 'maintenance.request'
#     maintenance_type = fields.Selection([('corrective', 'Corrective'), ('preventive', 'Preventive')],
#                                         string='Maintenance Type', default="corrective")
