from odoo.tests import common

class TestSocialAccounts(common.TransactionCase):
    def setUp(self):
        super().setUp()
        self.partner = self.env['res.partner'].create({
            'name': 'Test Customer',
            'is_company': True,
        })

    def test_profile_complete(self):
        # Test incomplete profile
        self.assertFalse(self.partner.is_profile_complete, "Profile should be incomplete by default")

        # Add partial social accounts
        self.partner.write({
            'facebook_url': 'https://facebook.com/test',
            'linkedin_url': 'https://linkedin.com/in/test',
        })
        self.assertFalse(self.partner.is_profile_complete, "Profile should still be incomplete")

        # Add all social accounts
        self.partner.write({
            'twitter_url': 'https://twitter.com/test',
        })
        self.assertTrue(self.partner.is_profile_complete, "Profile should be complete")

    def test_search_social_accounts(self):
        self.partner.write({
            'facebook_url': 'https://facebook.com/test',
            'linkedin_url': 'https://linkedin.com/in/test',
            'twitter_url': 'https://twitter.com/test',
        })
        partners = self.env['res.partner'].search([('facebook_url', 'ilike', 'test')])
        self.assertIn(self.partner, partners, "Partner should be found by Facebook URL")