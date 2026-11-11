/** @odoo-module **/

import { registry } from "@web/core/registry";

registry.category("web_tour.tours").add("form_action_buttons_tour", {
    steps: () => [
        {
            content: "Create a new contact",
            trigger: ".o-kanban-button-new",
            run: "click",
        },
        {
            content: "Type a name so the form becomes dirty",
            trigger: ".o_form_view .o_input[id^=name]",
            run() {
                const input = document.querySelector(".o_form_view .o_input[id^=name]");
                input.focus();
                input.value = "Button Test";
                input.dispatchEvent(new Event("input", { bubbles: true }));
                input.dispatchEvent(new Event("change", { bubbles: true }));
            },
        },
        {
            content: "Save button is a real, coloured button with a label",
            trigger: ".o_form_button_save.o_fab_button:contains(Save)",
            run() {
                const color = getComputedStyle(document.querySelector(".o_form_button_save")).backgroundColor;
                if (color !== "rgb(22, 163, 74)") {
                    throw new Error("Unexpected Save background: " + color);
                }
            },
        },
        {
            content: "Discard button is a real button with a label",
            trigger: ".o_form_button_cancel.o_fab_button:contains(Discard)",
        },
        {
            content: "Click Save",
            trigger: ".o_form_button_save",
            run() {
                document.querySelector(".o_form_button_save").click();
            },
        },
        {
            content: "The page is still usable after the click",
            trigger: ".o_control_panel",
        },
    ],
});
