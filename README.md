# CRM Social Accounts

Odoo module to extend CRM functionality by adding social media account management for customers.

## Features
- Add Facebook, LinkedIn, and Twitter URLs to customer profiles.
- Display social accounts in a dedicated tab with icons.
- Show "Profile Complete" checkmark when all social accounts are filled.
- Filter for customers with incomplete profiles.
- Public website page to promote customers with search by name or social accounts.
- Unit tests and test coverage reporting.
- Continuous integration with GitHub Actions.

## Installation
1. Copy the module to your Odoo addons directory.
2. Update the module list in Odoo.
3. Install the module from the Apps menu.

## Requirements
- Odoo 17
- Dependencies: `crm`, `website`

## Development
- Run tests: `coverage run ./odoo-bin --addons-path=addons,crm_social_accounts --db-filter=odoo --test-enable --log-level=test`
- Generate coverage report: `coverage html`