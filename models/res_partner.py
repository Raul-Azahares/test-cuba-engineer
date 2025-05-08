from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    facebook_url = fields.Char('Facebook URL')
    linkedin_url = fields.Char('LinkedIn URL')
    twitter_url = fields.Char('Twitter URL')
    is_profile_complete = fields.Boolean('Profile Complete', compute='_compute_profile_complete', store=True)

    @api.depends('facebook_url', 'linkedin_url', 'twitter_url')
    def _compute_profile_complete(self):
        for record in self:
            record.is_profile_complete = bool(record.facebook_url and record.linkedin_url and record.twitter_url)

    def action_send_profile_completion_email(self):
        incomplete_partners = self.search([('is_profile_complete', '=', False)])
        mailing = self.env['mailing.mailing'].create({
            'subject': 'Complete Your Social Profile',
            'mailing_model_id': self.env['ir.model']._get('res.partner').id,
            'mailing_domain': [('id', 'in', incomplete_partners.ids)],
            'body_html': '<p>Please complete your social media profiles to enhance your visibility!</p>',
        })
        mailing.action_send_mail()