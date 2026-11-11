/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { session } from "@web/session";
import { FormStatusIndicator } from "@web/views/form/form_status_indicator/form_status_indicator";

const DEFAULTS = {
    save_bg: "#714B67",
    save_text: "#FFFFFF",
    discard_bg: "#E9ECEF",
    discard_text: "#212529",
};

patch(FormStatusIndicator.prototype, {
    get fabColors() {
        return { ...DEFAULTS, ...(session.form_action_buttons || {}) };
    },
    get fabSaveStyle() {
        const c = this.fabColors;
        return `background-color: ${c.save_bg}; color: ${c.save_text}; border-color: ${c.save_bg};`;
    },
    get fabDiscardStyle() {
        const c = this.fabColors;
        return `background-color: ${c.discard_bg}; color: ${c.discard_text}; border-color: ${c.discard_bg};`;
    },
});
