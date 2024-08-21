# Copyright (c) 2024, Amrinder Singh and contributors
# For license information, please see license.txt

# import frappe
from frappe.website.website_generator import WebsiteGenerator



import frappe
from frappe import _
from frappe.model.document import Document
from drillbit.api import check_plagiarism, check_plagiarism_in_file

class DrillBitAPI(Document):
    def get_all_documents(self):
        return [d.description for d in frappe.get_all('DrillbitAPI', fields=['description'])]

    def check_plagiarism(self, text, comparison_texts):
        for comparison_text in comparison_texts:
            similarity = self.calculate_similarity(text, comparison_text)
            if similarity > 0.8:  
                return True, similarity
        return False, 0

    def check_plagiarism_in_file(self, file_path, comparison_texts):
        with open(file_path, 'r') as file:
            file_content = file.read()
            return self.check_plagiarism(file_content, comparison_texts)

    def calculate_similarity(self, text1, text2):
        return 0.0  # Implement your similarity calculation logic here

@frappe.whitelist()
def verify_plagiarism(docname):
    frappe.logger().info(f"Received docname: {docname}")
    doc = frappe.get_doc('DrillbitAPI', docname)
    drillbit_api = DrillBitAPI()

    comparison_texts = drillbit_api.get_all_documents()

    if doc.upload_file:
        file_path = frappe.get_site_path('private', 'files', doc.upload_file)
        is_plagiarized, similarity = drillbit_api.check_plagiarism_in_file(file_path, comparison_texts)
    else:
        is_plagiarized, similarity = drillbit_api.check_plagiarism(doc.description, comparison_texts)

    if is_plagiarized:
        return _("Plagiarism detected with a similarity of {0:.2f}%").format(similarity * 100)
    else:
        return _("No plagiarism detected")
