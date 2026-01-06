from frappe import _


def get_data():
	"""Return desktop page configuration"""
	return [
		{
			"module_name": "Foundry ERP",
			"color": "#FF5733",
			"icon": "fa fa-industry",
			"type": "module",
			"label": _("Foundry ERP")
		}
	]
