from odoo import http
from odoo.http import request

class CustomerPromotion(http.Controller):
    @http.route('/customers', type='http', auth='public', website=True)
    def customer_promotion(self, **kwargs):
        search_query = kwargs.get('search', '')
        domain = [('is_company', '=', True)]
        if search_query:
            domain += ['|', '|', '|',
                       ('name', 'ilike', search_query),
                       ('facebook_url', 'ilike', search_query),
                       ('linkedin_url', 'ilike', search_query),
                       ('twitter_url', 'ilike', search_query)]
        partners = request.env['res.partner'].sudo().search(domain)
        return request.render('crm_social_accounts.customer_promotion_template', {
            'partners': partners,
            'search_query': search_query,
        })