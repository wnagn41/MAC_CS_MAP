import re

def parse_courses(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    course_pattern = re.compile(
        r'Course Code: (.*?)\nCourse Name: (.*?)\nDescription: (.*?)\nPrerequisites: (.*?)\nAntirequisites:', re.DOTALL)
    courses = course_pattern.findall(content)

    course_list = []
    for course in courses:
        course_code = course[0].strip()
        course_name = course[1].strip()
        course_description = course[2].strip()
        course_prerequisites = course[3].strip()
        
        # Extract prerequisite course codes
        prereq_list = []
        # Match pattern like: XXXX 1XX3 where X can be letter or number
        prereq_codes = re.findall(r'[A-Z]+\s*\d[A-Z0-9]{3}', course_prerequisites)
        if prereq_codes:
            prereq_list = [code.replace(' ', '') for code in prereq_codes]
            
        course_list.append([
            course_code, 
            course_name, 
            course_description, 
            course_prerequisites,
            prereq_list
        ])

    return course_list

if __name__ == "__main__":
    file_path = 'extracted_courses.txt'
    courses = parse_courses(file_path)
    for course in courses:
        print(course[0],course[-1])
    # print(courses[-1])

