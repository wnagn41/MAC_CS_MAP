from per_form_course import extract_courses_by_term
from temp import parse_courses

def get_available_courses():
    # Get courses from permission form
    term_courses = extract_courses_by_term('Permission Form.html')
    
    # Create a set of all available course codes
    available_codes = set()
    for term in ['summer', 'fall', 'winter']:
        available_codes.update(course['code'].replace(' ', '') for course in term_courses[term])
    
    # Get all course details from extracted_courses.txt
    all_courses = parse_courses('extracted_courses.txt')
    
    # Filter courses that are available in 2024-2025
    available_courses = []
    for course in all_courses:
        course_code = course[0].replace(' ', '')  # Remove space from course code
        if course_code in available_codes:
            available_courses.append(course)
    
    return available_courses, term_courses

if __name__ == "__main__":
    available_courses, term_courses = get_available_courses()
    
    print("Available Courses for 2024-2025:")
    print("=" * 80)
    print(f"\nTotal courses: {len(available_courses)}")
    print("-" * 80)
    
    print("\nSummer 2024:")
    print("-" * 40)
    for course in term_courses['summer']:
        print(f"{course['code']} - {course['professor']}")
    
    print("\nFall 2024:")
    print("-" * 40)
    for course in term_courses['fall']:
        print(f"{course['code']} - {course['professor']}")
    
    print("\nWinter 2025:")
    print("-" * 40)
    for course in term_courses['winter']:
        print(f"{course['code']} - {course['professor']}")
    
    print("\nDetailed Course Information:")
    print("=" * 80)
    for course in available_courses:
        print(f"\nCourse Code: {course[0]}")
        print(f"Course Name: {course[1]}")
        print(f"Prerequisites: {course[3]}")
        print(f"Prerequisite Codes: {course[4]}")
        print("-" * 40)
