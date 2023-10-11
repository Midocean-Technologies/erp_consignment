# Copyright (c) 2023, Midocean  and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class ConsignmentDelivery(Document):
    # pass
	
	def on_submit(self):
      
		doc = frappe.new_doc("Stock Entry")
		doc.stock_entry_type = "Material Transfer"
		for i in self.items:
			doc.append("items",{
				"item_code":i.item_code,
				"qty":i.qty,
				"s_warehouse":i.warehouse,
				"t_warehouse":self.consignment_warehouse
			})
		doc.consignment_delivery = self.name
		doc.customer = self.customer
		doc.save()
		doc.submit()
		self.db_set("stock_entry", doc.name)
  
	def on_cancel(self):
		if self.stock_entry:
			stock_entry = frappe.get_doc("Stock Entry",self.stock_entry)
			stock_entry.cancel()
			stock_entry.db_set("consignment_delivery","")
			self.db_set("stock_entry","")


			