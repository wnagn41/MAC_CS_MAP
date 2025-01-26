from bs4 import BeautifulSoup
import re

def extract_course_info(html_file_path, output_file_path):
    # Read the HTML file
    with open(html_file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Parse HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all course listings
    courses = soup.find_all('li', class_='course-listing__course')

    # Initialize list to store courses
    course_list = []
    
    # Open output file
    with open(output_file_path, 'w', encoding='utf-8') as outfile:
        for course in courses:
            try:
                # Extract course code and name
                title_button = course.find('button', class_='course-listing__course-title')
                spans = title_button.find_all('span')
                course_code = spans[0].get_text(strip=True)
                
                # Check if course code starts with "COMPSCI"
                if not course_code.startswith("COMPSCI"):
                    continue  # Skip this course if it doesn't start with "COMPSCI"
                
                course_name = spans[1].get_text(strip=True)

                # Extract description
                description_div = course.find('div', class_='course-listing__course-description')
                description = description_div.get_text(strip=True) if description_div else "No description available"

                # Extract prerequisites and antirequisites using regex
                prereq_match = re.search(r'Prerequisite\(s\):\s*([^A-Z]*[^.]*)', description)
                prerequisites = prereq_match.group(1).strip() if prereq_match else "None listed"


                # Clean up description by removing prerequisites and antirequisites
                main_description = description
                if prereq_match:
                    main_description = main_description.replace(prereq_match.group(0), '')

                main_description = main_description.strip()

                # Create course dictionary
                course_data = {
                    'code': course_code,
                    'name': course_name,
                    'prerequisites': prerequisites,
                }
                
                # Add to list
                course_list.append(course_data)

                # Write to file in structured format
                outfile.write(f"Course Code: {course_code}\n")
                # outfile.write(f"Course Name: {course_name}\n")
                outfile.write(f"Prerequisites: {prerequisites}\n")
                outfile.write("\n" + "="*80 + "\n\n")  # Separator between courses

            except Exception as e:
                print(f"Error processing course: {e}")
                continue

    print(f"Course information has been extracted and saved to {output_file_path}")
    return course_list  # Return the list of courses

# Usage example
if __name__ == "__main__":
    html_file_path = "Courses – Faculty of Engineering.html"
    output_file_path = "extracted_courses.txt"
    courses = extract_course_info(html_file_path, output_file_path)  # Capture the returned courses
    print(courses)