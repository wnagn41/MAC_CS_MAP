from bs4 import BeautifulSoup
import re

def extract_courses_by_term(html_file):
    with open(html_file, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')
    
    # Find all select elements
    selects = soup.find_all('select', {'name': 'course[]'})
    
    term_courses = {
        'summer': [],
        'fall': [],
        'winter': []
    }
    
    for select in selects:
        # Get the term from the first option
        term_option = select.find('option').text
        
        # Determine which term this select is for
        term = None
        if 'Spg/Sum' in term_option:
            term = 'summer'
        elif 'Fall' in term_option:
            term = 'fall'
        elif 'Winter' in term_option:
            term = 'winter'
            
        if term:
            # Get all course options (skip the first one as it's the term header)
            course_options = select.find_all('option')[1:]
            for option in course_options:
                # Extract course code using regex
                match = re.search(r'(COMPSCI)\s+\d[A-Z0-9]{3}', option.text)
                if match:
                    course_code = match.group(0)
                    # Extract professor name if available
                    prof_match = re.search(r'--\s*(.+)$', option.text)
                    professor = prof_match.group(1).strip() if prof_match else "TBA"
                    term_courses[term].append({
                        'code': course_code,
                        'professor': professor
                    })
    
    return term_courses

def save_courses_to_file(courses, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        for term, course_list in courses.items():
            file.write(f"{term.capitalize()} 2024 Courses:\n")
            file.write("-" * 50 + "\n")
            for course in course_list:
                file.write(f"{course['code']} - {course['professor']}\n")
            file.write("\n")

if __name__ == "__main__":
    courses = extract_courses_by_term('Permission Form.html')
    save_courses_to_file(courses, 'per_form_compsci.txt')
    
    print("Summer 2024 Courses:")
    print("-" * 50)
    for course in courses['summer']:
        print(f"{course['code']} - {course['professor']}")
    
    print("\nFall 2024 Courses:")
    print("-" * 50)
    for course in courses['fall']:
        print(f"{course['code']} - {course['professor']}")
    
    print("\nWinter 2025 Courses:")
    print("-" * 50)
    for course in courses['winter']:
        print(f"{course['code']} - {course['professor']}")
