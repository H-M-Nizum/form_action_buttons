# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo.tests import tagged
from odoo.tests.common import HttpCase, TransactionCase

from ..models.ir_http import DEFAULT_COLORS


@tagged('post_install', '-at_install', 'form_action_buttons')
class TestFormActionButtons(TransactionCase):

    def _colors(self):
        return self.env['ir.http']._form_action_buttons_colors()

    def test_defaults(self):
        self.assertEqual(self._colors(), DEFAULT_COLORS)

    def test_settings_are_used(self):
        settings = self.env['res.config.settings'].create({
            'fab_save_bg': '#16A34A', 'fab_save_text': '#FFFFFF',
            'fab_discard_bg': '#DC2626', 'fab_discard_text': '#FFF',
        })
        settings.execute()
        colors = self._colors()
        self.assertEqual(colors['save_bg'], '#16A34A')
        self.assertEqual(colors['discard_bg'], '#DC2626')
        self.assertEqual(colors['discard_text'], '#FFF')

    def test_invalid_value_falls_back(self):
        """Nothing but a plain hex colour may reach the browser style attribute."""
        params = self.env['ir.config_parameter'].sudo()
        params.set_param('form_action_buttons.save_bg', 'red;background:url(x)')
        params.set_param('form_action_buttons.save_text', '')
        colors = self._colors()
        self.assertEqual(colors['save_bg'], DEFAULT_COLORS['save_bg'])
        self.assertEqual(colors['save_text'], DEFAULT_COLORS['save_text'])


@tagged('post_install', '-at_install', 'form_action_buttons')
class TestFormActionButtonsUI(HttpCase):

    def test_buttons_rendered_with_colors(self):
        self.env['ir.config_parameter'].sudo().set_param('form_action_buttons.save_bg', '#16A34A')
        self.start_tour('/odoo/action-base.action_partner_form/new', 'form_action_buttons_tour', login='admin')
