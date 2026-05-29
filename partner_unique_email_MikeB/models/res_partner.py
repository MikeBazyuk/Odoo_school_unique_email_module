import logging

from odoo import _, api, models
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)


class ResPartner(models.Model):

    _inherit = 'res.partner'

    @api.constrains('email')
    def _check_unique_email(self):

        for partner in self.filtered('email'):
            duplicate = self.search([
                ('email', '=ilike', partner.email),
                ('id', '!=', partner.id),
            ], limit=1)
            if duplicate:
                raise ValidationError(_(
                    'Партнер з e-mail адресою "%(email)s" вже існує у системі: %(name)s.',
                    email=partner.email,
                    name=duplicate.display_name,
                ))
