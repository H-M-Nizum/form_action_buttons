# Form Save & Discard Buttons

Odoo 17 shows two tiny icons (a cloud and an undo arrow) in the top-left corner of every form
when a record has unsaved changes. This module replaces them with two real buttons,
**Save** and **Discard**, and lets an administrator choose their background and text colours.

* Works on every form view of every app, nothing to configure per model.
* Same behaviour as the original icons: the buttons appear only when there is something to save,
  keep the `S` (save) and `J` (discard) shortcuts, and Save is disabled while the record is invalid.
* Four colours: Save background, Save text, Discard background, Discard text.
* Free, no extra Python dependencies, LGPL-3.

## Configuration

Settings > **Form Buttons**. Pick the colours with the colour pickers and click Save.
The colours apply to all users the next time they load the page.

Only plain hex colours (`#RGB` or `#RRGGBB`) are accepted; anything else falls back to the default.

## Technical notes

* `ir.http.session_info` hands the colours to the web client (internal users only).
* `FormStatusIndicator` is patched and its template extended; no core file is changed.
* Colours are stored as system parameters `form_action_buttons.save_bg`, `.save_text`,
  `.discard_bg`, `.discard_text`. Uninstalling the module restores the original icons.

## Author

H.M.Nizum - https://github.com/H-M-Nizum/form_action_buttons
