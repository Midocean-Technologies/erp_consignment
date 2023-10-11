import frappe
from frappe import _
from frappe.custom.doctype.custom_field.custom_field import create_custom_field
from frappe.custom.doctype.property_setter.property_setter import make_property_setter

@frappe.whitelist()
def after_install():
    custom_field_add()
#     create_make_property_setter()

# def create_make_property_setter():
#     make_property_setter(
#         "Lead",
#         "company_name",
#         "reqd",
#         1,
#         "Check",
#     )
    

def custom_field_add():
    # pass
    create_custom_field(
        "Customer",
        {
            "label": _("Consignment Warehouse"),
            "fieldname": "consignment_warehouse",
            "fieldtype": "Link",
            "options": "Warehouse",
            "insert_after": "customer_code",
        },
    )
    create_custom_field(
        "Stock Entry",
        {
            "label": _("Consignment Delivery"),
            "fieldname": "consignment_delivery",
            "fieldtype": "Data",
            # "options": "Consignment Delivery",
            "insert_after": "inspection_required",
        },
    )
    create_custom_field(
        "Stock Entry",
        {
            "label": _("Customer"),
            "fieldname": "customer",
            "fieldtype": "Link",
            "options": "Customer",
            "insert_after": "consignment_delivery",
        },
    )
    