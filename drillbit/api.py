# import requests
# import frappe

# def check_plagiarism(content):
#     api_key = frappe.db.get_single_value('Plagiarism Settings', 'drillbit_api_key')
#     url = "https://www.drillbitplagiarism.com/openapi"  # Example endpoint; adjust based on actual API docs.
#     headers = {
#         "Authorization": f"Bearer {api_key}",
#         "Content-Type": "application/json"
#     }
#     data = {
#         "content": content,
#         "language": "en"  # Adjust as per API requirements
#     }
    
#     response = requests.post(url, headers=headers, json=data)
#     if response.status_code == 200:
#         return response.json()  # Process and return the result
#     else:
#         frappe.throw(f"Failed to check plagiarism: {response.content.decode('utf-8')}")



# import frappe
# import difflib
# from werkzeug.utils import secure_filename

# @frappe.whitelist(allow_guest=True)
# def check_plagiarism(content=None, file_url=None):
#     # Check if content is provided or a file is uploaded
#     if content and file_url:
#         return {"status": "error", "message": "Please provide either content or a file, not both"}

#     if not content and not file_url:
#         return {"status": "error", "message": "No content or file provided"}

#     if file_url:
#         # Handle file upload
#         file_doc = frappe.get_doc("File", {"file_url": file_url})
#         with open(file_doc.get_full_path(), 'r') as f:
#             content = f.read()

#     # Example: Simple comparison with a predefined set of documents
#     reference_texts = [
#         "This is a reference document.",
#         "Another example document for comparison."
#     ]

#     matches = []
#     for reference in reference_texts:
#         match_ratio = difflib.SequenceMatcher(None, content, reference).ratio()
#         if match_ratio > 0.6:  # Arbitrary threshold
#             matches.append({"reference": reference, "similarity": match_ratio})

#     return {
#         "status": "success",
#         "matches": matches if matches else "No significant matches found."
#     }

import hashlib
from difflib import SequenceMatcher

def check_plagiarism(text, comparison_texts):
    for comparison in comparison_texts:
        ratio = SequenceMatcher(None, text, comparison).ratio()
        if ratio > 0.8:  # Threshold for plagiarism
            return True, ratio
    return False, None

def check_plagiarism_in_file(file_path, comparison_texts):
    with open(file_path, 'r') as file:
        text = file.read()
    return check_plagiarism(text, comparison_texts)

def hash_text(text):
    return hashlib.md5(text.encode()).hexdigest()
