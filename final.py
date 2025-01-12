list = [{'code': 'COMPSCI 1DM3', 'name': 'Discrete Mathematics for Computer Science', 'prerequisites': []}, 
        {'code': 'COMPSCI 1JC3', 'name': 'Introduction to Computational Thinking', 'prerequisites': []}, 
        {'code': 'COMPSCI 1MD3', 'name': 'Introduction to Programming', 'prerequisites': []}, 
        {'code': 'COMPSCI 1XC3', 'name': 'Computer Science Practice and Experience: Development Basics', 'prerequisites': ['1MD3']}, 
        {'code': 'COMPSCI 1XD3', 'name': 'Computer Science Practice and Experience: Introduction to  Software Design Using Web Programming', 'prerequisites': ['1JC3']}, 
        {'code': 'COMPSCI 2AC3', 'name': 'Automata and Computability', 'prerequisites': ['2LC3', '2C03']}, 
        {'code': 'COMPSCI 2C03', 'name': 'Data Structures and Algorithms', 'prerequisites': ['1DM3', '1XC3', '1XD3', '1MD3']}, 
        {'code': 'COMPSCI 2DB3', 'name': 'Databases', 'prerequisites': ['2LC3', '2DM3']}, 
        {'code': 'COMPSCI 2GA3', 'name': 'Computer Architecture', 'prerequisites': ['1MD3']}, 
        {'code': 'COMPSCI 2LC3', 'name': 'Logical Reasoning for Computer Science', 'prerequisites': ['1DM3', '1MD3', '1XC3', '1XD3']}, 
        {'code': 'COMPSCI 2ME3', 'name': 'Introduction to Software Development', 'prerequisites': ['1XC3', '1XD3']}, 
        {'code': 'COMPSCI 2SD3', 'name': 'Concurrent Systems', 'prerequisites': ['2C03', '2LC3', '2ME3']}, 
        {'code': 'COMPSCI 2XC3', 'name': 'Computer Science Practice and Experience: Algorithms and Software Design', 'prerequisites': ['1XC3', '1XD3', '2C03', '2ME3']}, 
        {'code': 'COMPSCI 3AC3', 'name': 'Algorithms and Complexity', 'prerequisites': ['2C03', '2AC3']}, 
        {'code': 'COMPSCI 3DM3', 'name': 'Introduction to Data Mining', 'prerequisites': ['2DB3','2C03','2ME3']}, 
        {'code': 'COMPSCI 3DP3', 'name': 'Data Privacy', 'prerequisites': ['2C03', '2D03']}, 
        {'code': 'COMPSCI 3EA3', 'name': 'Software Specifications and Correctness', 'prerequisites': ['2LC3', '2AC3', '2ME3', '2SD3']}, 
        {'code': 'COMPSCI 3GC3', 'name': 'Computer Graphics', 'prerequisites': ['1B03', '2C03']}, 
        {'code': 'COMPSCI 3MI3', 'name': 'Principles Of Programming Languages', 'prerequisites': ['2C03', '2LC3', '2AC3', '2ME3']}, 
        {'code': 'COMPSCI 3N03', 'name': 'Computer Networks and Security', 'prerequisites': ['3SH3']}, 
        {'code': 'COMPSCI 3RA3', 'name': 'Software Requirements and Security Considerations', 'prerequisites': ['2AC3', '2ME3']}, 
        {'code': 'COMPSCI 3TB3', 'name': 'Syntax-Based Tools and Compilers', 'prerequisites': ['2C03', '2C03', '2GA3', '2GA3', '2AC3','3MI3']}, 
        {'code': 'COMPSCI 3SH3', 'name': 'Computer Science Practice and Experience: Operating Systems', 'prerequisites': ['2SD3', '2C03', '2GA3']}, 
        {'code': 'COMPSCI 4E03', 'name': 'Performance Analysis of Computer Systems', 'prerequisites': ['2D03', '2C03']}, 
        {'code': 'COMPSCI 4EN3', 'name': 'Software Entrepreneurship', 'prerequisites': []}, 
        {'code': 'COMPSCI 4HC3', 'name': 'Human Computer Interfaces', 'prerequisites': ['2C03']}, 
        {'code': 'COMPSCI 4ML3', 'name': 'Introduction to Machine Learning', 'prerequisites': ['2C03', '2C03', '4O03']}, 
        {'code': 'COMPSCI 4O03', 'name': 'Linear Optimization Algorithms', 'prerequisites': ['2C03']}, 
        {'code': 'COMPSCI 4X03', 'name': 'Scientific Computation', 'prerequisites': ['1AA3', '1B03']}, 
        {'code': 'COMPSCI 4Z03', 'name': 'Directed Readings', 'prerequisites': []}, 
        {'code': 'COMPSCI 4ZP6A/B', 'name': 'Computer Science Capstone Project', 'prerequisites': []}, 
        {'code': 'COMPSCI 3VA3', 'name': 'Information Visualization and Visual Analytics', 'prerequisites': ['1XD3', '2C03', '2DB3']},
        {'code': 'COMPSCI 4AL3', 'name': 'Applications of Machine Learning', 'prerequisites': ['2C03', '2ME3', '2D03']}, 
        {'code': 'COMPSCI 4CR3', 'name': 'Applied Cryptography', 'prerequisites': ['1B03','1DM3', '2C03']}, 
        {'code': 'COMPSCI 4SD3', 'name': 'Data-Driven Algorithms for Sequential Decision Making', 'prerequisites': ['2C03','2D03']}, 
        {'code': 'COMPSCI 4NL3', 'name': 'Natural Language Processing', 'prerequisites': ['2C03','1B03','2D03']}]
print(len(list))

for i in list:
    i['prerequisites'] = ["COMPSCI " + j for j in i['prerequisites']]
    # print(i['prerequisites'])
# for course in list:
    # print("    ,", course)


list2 = [{'code': 'COMPSCI 1DM3', 'name': 'Discrete Mathematics for Computer Science', 'prerequisites': []}
    , {'code': 'COMPSCI 1JC3', 'name': 'Introduction to Computational Thinking', 'prerequisites': []}
    , {'code': 'COMPSCI 1MD3', 'name': 'Introduction to Programming', 'prerequisites': []}
    , {'code': 'COMPSCI 1XC3', 'name': 'Computer Science Practice and Experience: Development Basics', 'prerequisites': ['COMPSCI 1MD3']}
    , {'code': 'COMPSCI 1XD3', 'name': 'Computer Science Practice and Experience: Introduction to  Software Design Using Web Programming', 'prerequisites': ['COMPSCI 1JC3','COMPSCI 1MD3']}
    , {'code': 'COMPSCI 2AC3', 'name': 'Automata and Computability', 'prerequisites': ['COMPSCI 2LC3', 'COMPSCI 2C03']}
    , {'code': 'COMPSCI 2C03', 'name': 'Data Structures and Algorithms', 'prerequisites': ['COMPSCI 1DM3', 'COMPSCI 1XC3', 'orCOMPSCI 1XD3', 'orCOMPSCI 1MD3']}
    , {'code': 'COMPSCI 2DB3', 'name': 'Databases', 'prerequisites': ['COMPSCI 2LC3', 'COMPSCI 2DM3']}
    , {'code': 'COMPSCI 2GA3', 'name': 'Computer Architecture', 'prerequisites': ['COMPSCI 1MD3']}
    , {'code': 'COMPSCI 2LC3', 'name': 'Logical Reasoning for Computer Science', 'prerequisites': ['COMPSCI 1DM3', 'COMPSCI 1MD3', 'orCOMPSCI 1XC3', 'orCOMPSCI 1XD3']}        
    , {'code': 'COMPSCI 2ME3', 'name': 'Introduction to Software Development', 'prerequisites': ['COMPSCI 1XC3', 'COMPSCI 1XD3']}
    , {'code': 'COMPSCI 2SD3', 'name': 'Concurrent Systems', 'prerequisites': ['COMPSCI 2C03', 'COMPSCI 2LC3', 'COMPSCI 2ME3']}
    , {'code': 'COMPSCI 2XC3', 'name': 'Computer Science Practice and Experience: Algorithms and Software Design', 'prerequisites': ['COMPSCI 1XC3', 'COMPSCI 1XD3', 'COMPSCI 2C03', 'COMPSCI 2ME3']}
    , {'code': 'COMPSCI 3AC3', 'name': 'Algorithms and Complexity', 'prerequisites': ['COMPSCI 2C03', 'COMPSCI 2AC3']}
    , {'code': 'COMPSCI 3DM3', 'name': 'Introduction to Data Mining', 'prerequisites': ['COMPSCI 2DB3', 'COMPSCI 2C03', 'COMPSCI 2ME3', 'STATS 2D03']}
    , {'code': 'COMPSCI 3DP3', 'name': 'Data Privacy', 'prerequisites': ['COMPSCI 2C03', 'STATS 2D03', 'MATH 1B03']}
    , {'code': 'COMPSCI 3EA3', 'name': 'Software Specifications and Correctness', 'prerequisites': ['COMPSCI 2LC3', 'COMPSCI 2AC3', 'COMPSCI 2ME3', 'COMPSCI 2SD3']}       
    , {'code': 'COMPSCI 3GC3', 'name': 'Computer Graphics', 'prerequisites': ['MATH 1B03', 'COMPSCI 2C03']}
    , {'code': 'COMPSCI 3MI3', 'name': 'Principles Of Programming Languages', 'prerequisites': ['COMPSCI 2C03', 'COMPSCI 2LC3', 'COMPSCI 2AC3', 'COMPSCI 2ME3']}
    , {'code': 'COMPSCI 3N03', 'name': 'Computer Networks and Security', 'prerequisites': ['COMPSCI 3SH3']}
    , {'code': 'COMPSCI 3RA3', 'name': 'Software Requirements and Security Considerations', 'prerequisites': ['COMPSCI 2AC3', 'COMPSCI 2ME3']}
    , {'code': 'COMPSCI 3TB3', 'name': 'Syntax-Based Tools and Compilers', 'prerequisites': ['COMPSCI 2C03', 'COMPSCI 2AC3', 'COMPSCI 2GA3', 'COMPSCI 3MI3']}
    , {'code': 'COMPSCI 3SH3', 'name': 'Computer Science Practice and Experience: Operating Systems', 'prerequisites': ['COMPSCI 2SD3', 'COMPSCI 2C03', 'COMPSCI 2GA3']}   
    , {'code': 'COMPSCI 4E03', 'name': 'Performance Analysis of Computer Systems', 'prerequisites': ['STATS 2D03']}
    , {'code': 'COMPSCI 4EN3', 'name': 'Software Entrepreneurship', 'prerequisites': []}
    , {'code': 'COMPSCI 4HC3', 'name': 'Human Computer Interfaces', 'prerequisites': ['COMPSCI 2C03']}
    , {'code': 'COMPSCI 4ML3', 'name': 'Introduction to Machine Learning', 'prerequisites': ['COMPSCI 2C03', 'STATS 2D03', 'COMPSCI 4O03']}
    , {'code': 'COMPSCI 4O03', 'name': 'Linear Optimization Algorithms', 'prerequisites': ['COMPSCI 2C03']}
    , {'code': 'COMPSCI 4X03', 'name': 'Scientific Computation', 'prerequisites': ['MATH 1AA3', 'MATH 1B03']}
    , {'code': 'COMPSCI 4Z03', 'name': 'Directed Readings', 'prerequisites': []}
    , {'code': 'COMPSCI 4ZP6A/B', 'name': 'Computer Science Capstone Project', 'prerequisites': []}
    , {'code': 'COMPSCI 3VA3', 'name': 'Information Visualization and Visual Analytics', 'prerequisites': ['COMPSCI 1XD3', 'COMPSCI 2C03','COMPSCI 2DB3', 'COMPSCI 2DB3']}
    , {'code': 'COMPSCI 4AL3', 'name': 'Applications of Machine Learning', 'prerequisites': ['COMPSCI 2C03', 'COMPSCI 2ME3', 'STATS 2D03']}
    , {'code': 'COMPSCI 4CR3', 'name': 'Applied Cryptography', 'prerequisites': ['MATH 1B03', 'COMPSCI 1DM3', 'COMPSCI 2C03']}
    , {'code': 'COMPSCI 4SD3', 'name': 'Data-Driven Algorithms for Sequential Decision Making', 'prerequisites': ['COMPSCI 2C03', 'STATS 2D03']}
    , {'code': 'COMPSCI 4NL3', 'name': 'Natural Language Processing', 'prerequisites': ['COMPSCI 2C03', 'MATH 1B03', 'STATS 2D03']}]

for i in list2:
    print("  ")
    print(i['code'])
    print('prerequisites')
    for j in i['prerequisites']:
        if j in [course['code'] for course in list2]:
            print(j)
