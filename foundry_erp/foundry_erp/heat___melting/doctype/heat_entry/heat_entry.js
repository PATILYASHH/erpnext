// Copyright (c) 2026, Custom and contributors
// For license information, please see license.txt

frappe.ui.form.on('Heat Entry', {
	// Calculate yield percentage when good_qty_kg or actual_melt_qty_kg changes
	actual_melt_qty_kg: function(frm) {
		calculate_yield(frm);
	},
	
	good_qty_kg: function(frm) {
		calculate_yield(frm);
	},
	
	rejection_qty_kg: function(frm) {
		// Auto calculate good qty if rejection is entered
		if (frm.doc.actual_melt_qty_kg && frm.doc.rejection_qty_kg) {
			let good_qty = frm.doc.actual_melt_qty_kg - frm.doc.rejection_qty_kg;
			frm.set_value('good_qty_kg', good_qty);
		}
	}
});

function calculate_yield(frm) {
	if (frm.doc.actual_melt_qty_kg && frm.doc.good_qty_kg) {
		let yield_percent = (frm.doc.good_qty_kg / frm.doc.actual_melt_qty_kg) * 100;
		frm.set_value('yield_percent', yield_percent);
	} else {
		frm.set_value('yield_percent', 0);
	}
}
