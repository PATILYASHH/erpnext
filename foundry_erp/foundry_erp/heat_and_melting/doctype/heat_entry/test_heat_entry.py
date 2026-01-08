# Copyright (c) 2026, Custom and contributors
# For license information, please see license.txt

import unittest

import frappe
from frappe.tests import IntegrationTestCase


class TestHeatEntry(IntegrationTestCase):
	"""Test cases for Heat Entry DocType"""

	def test_yield_calculation_normal(self):
		"""Test yield calculation with normal values"""
		heat = frappe.new_doc("Heat Entry")
		heat.actual_melt_qty_kg = 1000
		heat.good_qty_kg = 900
		heat.calculate_yield()
		self.assertEqual(heat.yield_percent, 90.0)

	def test_yield_calculation_zero_actual_melt(self):
		"""Test yield calculation with zero actual melt qty (should not raise error)"""
		heat = frappe.new_doc("Heat Entry")
		heat.actual_melt_qty_kg = 0
		heat.good_qty_kg = 900
		heat.calculate_yield()
		self.assertEqual(heat.yield_percent, 0)

	def test_yield_calculation_no_good_qty(self):
		"""Test yield calculation with no good qty"""
		heat = frappe.new_doc("Heat Entry")
		heat.actual_melt_qty_kg = 1000
		heat.good_qty_kg = 0
		heat.calculate_yield()
		self.assertEqual(heat.yield_percent, 0)

	def test_yield_calculation_precision(self):
		"""Test that yield is rounded to 2 decimal places"""
		heat = frappe.new_doc("Heat Entry")
		heat.actual_melt_qty_kg = 1000
		heat.good_qty_kg = 333.33
		heat.calculate_yield()
		# 333.33 / 1000 * 100 = 33.333, rounded to 33.33
		self.assertEqual(heat.yield_percent, 33.33)

	def test_furnace_capacity_validation_missing_furnace(self):
		"""Test that missing furnace is handled gracefully"""
		heat = frappe.new_doc("Heat Entry")
		heat.furnace = "NONEXISTENT-FURNACE"
		heat.actual_melt_qty_kg = 1000
		
		with self.assertRaises(frappe.exceptions.ValidationError) as context:
			heat.validate_furnace_capacity()
		
		self.assertIn("not found in system", str(context.exception))

	def test_automatic_naming_series(self):
		"""Test that naming series works correctly"""
		heat = frappe.new_doc("Heat Entry")
		# Just verify that naming_series field exists and has options
		self.assertIn("naming_series", [f.fieldname for f in heat.meta.fields])
