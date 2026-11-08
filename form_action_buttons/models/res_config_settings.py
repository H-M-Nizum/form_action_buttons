# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import fields, models

from .ir_http import DEFAULT_COLORS


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'


    fab_save_bg = fields.Char(
        string='Save Button Background', default=DEFAULT_COLORS['save_bg'],
        config_parameter='form_action_buttons.save_bg')
    fab_save_text = fields.Char(
        string='Save Button Text', default=DEFAULT_COLORS['save_text'],
        config_parameter='form_action_buttons.save_text')
    fab_discard_bg = fields.Char(
        string='Discard Button Background', default=DEFAULT_COLORS['discard_bg'],
        config_parameter='form_action_buttons.discard_bg')
    fab_discard_text = fields.Char(
        string='Discard Button Text', default=DEFAULT_COLORS['discard_text'],
        config_parameter='form_action_buttons.discard_text')
