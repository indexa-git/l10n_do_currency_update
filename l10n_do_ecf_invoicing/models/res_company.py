from odoo import models, fields


class ResCompany(models.Model):
    _inherit = "res.company"

    l10n_do_ecf_service_env = fields.Selection(
        [("TesteCF", "Test"), ("CerteCF", "Certification"), ("eCF", "Production")],
        string="ECF Service Environment",
        required=True,
        default="TesteCF",
    )