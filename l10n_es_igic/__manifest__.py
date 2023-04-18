##############################################################################
#
#    Sistemas de Datos, Open Source Management Solution
#    Copyright (C) 2004-2011 Pexego Sistemas Informáticos.
#    Copyright (C) 2014 Arturo Esparragón Goncalves (http://sdatos.com).
#    Copyright (C) 2016-2018 Rodrigo Colombo Vlaeminch (http://sdatos.com).
#    Copyright (C) 2019 Comunitea (https://comunitea.com).
#    Copyright (C) 2019 Héctor J. Ravelo (http://sdatos.com)
#    License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0
#
##############################################################################

{
    "name": "IGIC (Impuesto General Indirecto Canario",
    "version": "16.0.1.0.0",
    "author": "David Diz Martínez <daviddiz@gmail.com>,"
    "Atlantux Consultores - Enrique Zanardi,"
    "Sistemas de Datos,"
    "Comunitea,"
    "Odoo Community Association (OCA)",
    "category": "Accounting/Localizations/Account Charts",
    "website": "https://github.com/OCA/l10n-spain",
    "depends": ["l10n_es"],
    "license": "AGPL-3",
    "data": [
        "data/account_chart_template_data.xml",
        "data/account.account.template-common-canary.csv",
        "data/account.account.template-pymes-canary.csv",
        "data/account.account.template-assoc-canary.csv",
        "data/account.account.template-full-canary.csv",
        "data/account_data.xml",
        "data/account_tax_data.xml",
        "data/account_fiscal_position_template_canary_data.xml",
    ],
    "installable": True,
    "auto_install": False,
}
