# User Manual - Form Save & Discard Buttons

## 1. What the module does
In Odoo 17 a form shows only a small cloud icon (save) and an undo arrow (discard) in the top-left
corner when something has changed. This module shows two clear buttons instead:
**Save** and **Discard**. It works on every form of every application.

## 2. Installation
1. Copy the `form_action_buttons` folder into your Odoo addons path.
2. Restart Odoo, open **Apps**, click **Update Apps List**.
3. Search "Form Save & Discard Buttons" and click **Install**.

The buttons appear immediately; no other setup is needed.

## 3. Using the buttons
* Open or create any record. As soon as something is changed (or the record is new) the
  **Save** and **Discard** buttons appear at the top left.
* **Save** stores the record. Keyboard shortcut: `Alt+S`.
* **Discard** drops all unsaved changes. Keyboard shortcut: `Alt+J`.
* If the record is not valid (a required field is empty) Save is disabled until it is fixed.
* When the record is saved the buttons disappear, exactly like the original icons.

## 4. Changing the colours
Only administrators can do this.
1. Open **Settings** and click **Form Buttons** in the left menu.
2. Click a colour circle and choose a colour:
   * Save Button Background / Save Button Text
   * Discard Button Background / Discard Button Text
3. Click **Save** (top left) and reload the browser page.

All users now see the new colours. Only plain hex colours are accepted; any other stored
value is ignored and the default colour is used.

Defaults: Save = purple background, white text; Discard = light grey background, dark text.

## 5. Uninstalling
Uninstall the module from **Apps**. The original icons return.

## 6. Support
https://github.com/H-M-Nizum/form_action_buttons/issues
