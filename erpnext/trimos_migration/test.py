import frappe

def create_custom_field():
    doc = frappe.get_doc({
	"doctype": "Custom Field",
	"dt": "Quotation",
	"label": "Quotation Status",
        "fieldname": "quotation_status",
        "insert_after": "customer_section",
        "fieldtype": "Select",
        "options": "Active\nInactive\nOrder Lost\nOrder Won\nOrder Received",
        "permlevel": 0,
        "reqd": 1,
        "allow_on_submit": 1,
        "in_standard_filter": 1,
        "search_index": 1
    })
    doc.insert()

