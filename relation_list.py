from extract_cs_course import extract_course_info
from per_form_course import extract_courses_by_term
import re

def create_course_lists(html_file_path, output_file_path):
    # Get all CS courses
    all_courses = extract_course_info(html_file_path, output_file_path)
    # Get performed courses
    performed_courses = extract_courses_by_term('Permission Form.html')
    all_performed_codes = [course['code'] for term in performed_courses.values() for course in term]

    # Initialize lists
    courses_in_performed = []
    courses_not_in_performed = []
    
    # Sort courses into appropriate lists
    for course in all_courses:
        # Remove description and antirequisites
        course.pop('description', None)
        course.pop('antirequisites', None)
        
        # Extract and format prerequisites
        prereq_text = course.get('prerequisites', '')
        prereq_list = re.findall(r'\b\d[A-Z0-9]{3}\b', prereq_text)
        course['prerequisites'] = prereq_list  # Update prerequisites to be a list of codes
        
        if any(course['code'].strip() == performed_code.strip() for performed_code in all_performed_codes):
            courses_in_performed.append(course)
        else:
            courses_not_in_performed.append(course)
    
    print(all_courses)
    return courses_in_performed, courses_not_in_performed

# Usage example
if __name__ == "__main__":
    html_file_path = "Courses – Faculty of Engineering.html"
    output_file_path = "extracted_courses.txt"
    
    in_list, not_in_list = create_course_lists(html_file_path, output_file_path)

