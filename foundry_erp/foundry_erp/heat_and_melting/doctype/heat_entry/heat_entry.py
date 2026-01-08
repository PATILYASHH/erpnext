# Copyright (c) 2026, Custom and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class HeatEntry(Document):
	def validate(self):
		"""Validate heat entry before saving"""
		self.validate_furnace_capacity()
		self.calculate_yield()

	def validate_furnace_capacity(self):
		"""Validate that actual melt qty does not exceed furnace capacity"""
		if self.actual_melt_qty_kg and self.furnace:
			try:
				furnace = frappe.get_doc("Furnace Master", self.furnace)
				if furnace.capacity_kg and self.actual_melt_qty_kg > furnace.capacity_kg:
					frappe.throw(
						f"Actual Melt Qty ({self.actual_melt_qty_kg} kg) exceeds furnace capacity ({furnace.capacity_kg} kg)"
					)
			except frappe.DoesNotExistError:
				frappe.throw(f"Furnace {self.furnace} not found in system")
			except Exception as e:
				frappe.throw(f"Error validating furnace capacity: {str(e)}")

	def calculate_yield(self):
		"""Auto calculate yield percentage"""
		if self.actual_melt_qty_kg and self.actual_melt_qty_kg > 0 and self.good_qty_kg:
			self.yield_percent = round((self.good_qty_kg / self.actual_melt_qty_kg) * 100, 2)
		else:
			self.yield_percent = 0
