import { registry } from "@web/core/registry";

registry.category("web_tour.tours").add("form_action_buttons_tour", {
    steps: () => [
        {
            content: "Type a name so the form becomes dirty",
            trigger: ".o_form_view .o_input[id^=name]",
            run: "edit Button Test",
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
            run: "click",
        },
        {
            content: "The record is saved: it is no longer new",
            trigger: ".o_form_status_indicator:not(.o_form_status_indicator_new_record)",
        },
    ],
});
