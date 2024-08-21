// Copyright (c) 2024, Amrinder Singh and contributors
// For license information, please see license.txt

// frappe.ui.form.on("DrillBitAPI", {
// 	refresh(frm) {

// 	},
// });


// plagiarism_checker/plagiarism_checker/doctype/plagiarism_check/plagiarism_check.js

frappe.ui.form.on('DrillBitAPI', {
    refresh: function(frm) {
        frm.add_custom_button(__('Verify'), function() {
            frappe.call({
                method: "drillbit.drillbit.doctype.drillbitapi.drillbitapi.verify_plagiarism",
                args: {
                    docname: frm.doc.name
                },
                callback: function(response) {
                    frappe.msgprint(response.message);
                }
            });
        });
    }
});


// frappe.ui.form.on('DrillbitAPI', {
//     refresh: function(frm) {
//         frm.add_custom_button(__('Verify'), function() {
//             frappe.call({
//                 method: "drillbit.drillbitapi.verify_plagiarism",
//                 args: {
//                     docname: frm.doc.name
//                 },
//                 callback: function(response) {
//                     frappe.msgprint(response.message);
//                 }
//             });
//         });
//     }
// });


// frappe.ui.form.on('DrillBitAPI', {
//     refresh: function(frm) {
//         // Add a custom button "Check Plagiarism"
//         frm.add_custom_button(__('Verify'), function() {
//             frappe.call({
//                 method: 'drillbit.drillbit.check_plagiarism_in_frappe',
//                 args: {
//                     drillbit_api: frm.doc.name
//                 },
//                 callback: function(r) {
//                     if(r.message) {
//                         // Display the results to the user
//                         frappe.msgprint({
//                             title: __('Plagiarism Check Result'),
//                             message: `Plagiarism Score: ${r.message.plagiarism_score}%<br>Matched Document: ${r.message.matched_document}`,
//                             indicator: 'blue'
//                         });
//                     }
//                 }
//             });
//         }).addClass('btn-primary');
//     }
// });

