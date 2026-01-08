from frappe import _


def get_data():
	"""Return desktop page configuration"""
	return [
		{
			"module_name": "Foundry ERP",
			"color": "#FF5733",
			"icon": "fa fa-industry",
			"type": "module",
			"label": _("Foundry ERP"),
		},
		# Quick Access - Heat & Melting
		{
			"module_name": "Heat Entry",
			"color": "#FF5733",
			"icon": "fa fa-fire",
			"type": "link",
			"link": "List/Heat Entry",
			"label": _("Heat Entry"),
			"_doctype": "Heat Entry",
		},
		{
			"module_name": "Charge Mix",
			"color": "#795548",
			"icon": "fa fa-cubes",
			"type": "link",
			"link": "List/Charge Mix",
			"label": _("Charge Mix"),
			"_doctype": "Charge Mix",
		},
		{
			"module_name": "Alloy Addition",
			"color": "#9C27B0",
			"icon": "fa fa-flask",
			"type": "link",
			"link": "List/Alloy Addition",
			"label": _("Alloy Addition"),
			"_doctype": "Alloy Addition",
		},
		# Quick Access - Quality
		{
			"module_name": "Lab Analysis Entry",
			"color": "#2196F3",
			"icon": "fa fa-microscope",
			"type": "link",
			"link": "List/Lab Analysis Entry",
			"label": _("Lab Analysis"),
			"_doctype": "Lab Analysis Entry",
		},
		# Quick Access - Production Planning
		{
			"module_name": "Daily Production Plan",
			"color": "#4CAF50",
			"icon": "fa fa-calendar-check",
			"type": "link",
			"link": "List/Daily Production Plan",
			"label": _("Daily Plan"),
			"_doctype": "Daily Production Plan",
		},
		{
			"module_name": "Monthly Production Plan",
			"color": "#8BC34A",
			"icon": "fa fa-calendar-alt",
			"type": "link",
			"link": "List/Monthly Production Plan",
			"label": _("Monthly Plan"),
			"_doctype": "Monthly Production Plan",
		},
		# Quick Access - Masters
		{
			"module_name": "Furnace Master",
			"color": "#FF9800",
			"icon": "fa fa-industry",
			"type": "link",
			"link": "List/Furnace Master",
			"label": _("Furnaces"),
			"_doctype": "Furnace Master",
		},
		{
			"module_name": "Grade Master",
			"color": "#607D8B",
			"icon": "fa fa-certificate",
			"type": "link",
			"link": "List/Grade Master",
			"label": _("Grades"),
			"_doctype": "Grade Master",
		},
		# Quick Access - Pattern Management
		{
			"module_name": "Pattern Issue",
			"color": "#00BCD4",
			"icon": "fa fa-share",
			"type": "link",
			"link": "List/Pattern Issue",
			"label": _("Pattern Issue"),
			"_doctype": "Pattern Issue",
		},
		# Quick Access - Costing
		{
			"module_name": "Heat Costing",
			"color": "#E91E63",
			"icon": "fa fa-dollar-sign",
			"type": "link",
			"link": "List/Heat Costing",
			"label": _("Heat Costing"),
			"_doctype": "Heat Costing",
		},
	]
