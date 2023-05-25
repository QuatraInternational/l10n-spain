from odoo import SUPERUSER_ID, api


def migrate(cr, version):
    """Reassign the conventional module category for localizations in Odoo 13.

    The previously assigned categories from Odoo 16 break the Odoo migration process.

    ```
    odoo.upgrade.util.exceptions.MigrationError:
    Can't rename base.module_category_localization_account_charts to
    base.module_category_accounting_localizations_account_charts as it already exists.
    ```
    """
    with api.Environment.manage():
        env = api.Environment(cr, SUPERUSER_ID, {})
        module = env["ir.module.module"].search([("name", "=", "l10n_es_igic")])
        module.category_id = env.ref("base.module_category_localization")
        env.ref("base.module_category_accounting_localizations_account_charts").unlink()
        env.ref("base.module_category_accounting_localizations").unlink()
