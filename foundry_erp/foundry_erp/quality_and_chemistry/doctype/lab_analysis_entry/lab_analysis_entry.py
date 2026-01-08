# Copyright (c) 2026, Custom and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class LabAnalysisEntry(Document):
	def validate(self):
		"""Validate chemistry results against limits"""
		self.validate_chemistry_limits()

	def validate_chemistry_limits(self):
		"""Validate each element against chemistry limits and mark within_limit"""
		if not self.grade or not self.results:
			return

		# Get chemistry limits for the grade
		chemistry_limits = frappe.get_all(
			"Chemistry Limits Master", filters={"grade": self.grade}, fields=["name"]
		)

		if not chemistry_limits:
			return

		# Get element limits
		limits_doc = frappe.get_doc("Chemistry Limits Master", chemistry_limits[0].name)
		limits_map = {}
		for limit in limits_doc.element_limits:
			limits_map[limit.element] = {"min": limit.min_value, "max": limit.max_value}

		# Validate each result
		any_out_of_range = False
		for result in self.results:
			if result.element in limits_map:
				result.min_limit = limits_map[result.element]["min"]
				result.max_limit = limits_map[result.element]["max"]

				# Check if within limits
				min_val = result.min_limit or 0
				max_val = result.max_limit or float("inf")

				if min_val <= result.actual_value <= max_val:
					result.within_limit = 1
				else:
					result.within_limit = 0
					any_out_of_range = True

		# Set status based on validation results
		if any_out_of_range:
			self.status = "Out of Specification"
			frappe.msgprint(
				"Warning: One or more chemistry elements are out of specified limits",
				indicator="orange",
				alert=True
			)
		else:
			self.status = "Within Specification"
