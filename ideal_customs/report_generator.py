import frappe
from erpnext.accounts.report.accounts_receivable.accounts_receivable import execute
from erpnext.accounts.report.accounts_receivable_summary.accounts_receivable_summary import execute as summary_execute


@frappe.whitelist(allow_guest=True)
def get_report(customer: str):
    company_list = frappe.db.get_list('Company')
    company = company_list[0].name
    filters = {
        "company":company,
        "party_type" : "Customer",
        "party": [customer],
        "range1": 30,
        "range2": 60,
        "range3": 90,
        "range4": 120,
        "show_remarks" : False
    }
    report = execute(filters)
    return report

@frappe.whitelist(allow_guest= True)
def get_receivable_summary(customer: str):
    company_list = frappe.db.get_list('Company')
    company = company_list[0].name
    filters = {
        "company": company,
        "party_type": "Customer",
        "party" : [customer],
        "range1": 30,
        "range2": 60,
        "range3": 90,
        "range4": 120,
        "range5": 360,
        "show_remarks" : False
    }
    ageing_report = execute(filters)
    return ageing_report