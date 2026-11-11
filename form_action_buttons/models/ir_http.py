# Part of Odoo. See LICENSE file for full copyright and licensing details.
import re

from odoo import models

DEFAULT_COLORS = {
    'save_bg': '#714B67',
    'save_text': '#FFFFFF',
    'discard_bg': '#E9ECEF',
    'discard_text': '#212529',
}
_HEX = re.compile(r'^#(?:[0-9a-fA-F]{3}|[0-9a-fA-F]{6})$')


class IrHttp(models.AbstractModel):
    _inherit = 'ir.http'

    def _form_action_buttons_colors(self):
        """The colours of the Save / Discard buttons, always valid hex values."""
        params = self.env['ir.config_parameter'].sudo()
        colors = {}
        for key, default in DEFAULT_COLORS.items():
            value = (params.get_param('form_action_buttons.' + key) or '').strip()
            # only plain hex colours reach the browser, whatever is stored
            colors[key] = value if _HEX.match(value) else default
        return colors

    def session_info(self):
        result = super().session_info()
        if self.env.user._is_internal():
            result['form_action_buttons'] = self._form_action_buttons_colors()
        return result
