def my_map(f,lst):
    if lst == []:
        return []
    else:
        return [f(lst[0])] + my_map(f, lst[1:])

def myzip(lst1,lst2):
    if lst1 ==[] or lst2 == []:
        return []
    else:
        return [(lst1[0],lst2[0])] + myzip(lst1[1:],lst2[1:])

def student(sid,fname,lname, crses):
    """Constructor for student"""
    courses = []
    while crses != []:
        courses += [(crses[0],crses[1])]
        crses = crses[2:]
    return [sid,[fname,lname],courses]

def get_id(std):
    """Returns students ID"""
    return std[0]

def get_name(std):
    """Returns students Name"""
    return std[1]

def get_courses(std):
    """Returns a list of tuples of course codes and grade"""
    return std[2]

def get_fname(name):
    """Returns first name"""
    return name[0]

def get_lname(name):
    """Returns last name"""
    return name[1]

def get_ccode(course_det):
    """Returns course code part of the tuple"""
    return course_det[0]

def get_grade(course_det):
    """Returns grade part of the tuple"""
    return course_det[1]

       
st1=student('620000101',"Jane","Doe",["COMP1126",80,"COMP1127",60,"COMP1210",50,"COMP1161",60,"COCR2003",85,"COMP2140",80])
     
credit_list={'COMP1126':3,'COMP1127':3,'COMP1161':3,'COMP1210':3,'COMP1220':3,'COMP2140':3,'COMP2111':3,'COCR2003':1}

qp_list = {"A+":4.3,"A":4.0,"A-":3.7,"B+":3.3,"B":3.0,"B-":2.7,"C+":2.3,\
      "C":2.0,"F1":1.7,"F2":1.3,"F3": 0.0}

def  computeLetterGrade(grade):
    if grade > 89:
        return "A+"
    elif 80 <= grade <= 89:
        return "A"
    elif 75 <= grade <= 79:
        return "A-"
    elif 70 <= grade <= 74:
        return "B+"
    elif 65 <= grade <= 69:
        return "B"
    elif 60 <= grade <= 64:
        return "B-"
    elif 55 <= grade <= 59:
        return "C+"
    elif 50 <= grade <= 54:
        return "C"
    elif 45 <= grade <= 49:
        return "F1"
    elif 40 <= grade <= 44:
        return "F2"
    elif 0 <= grade <= 39:
        return "F3"
    
def calcLetterGrade(std):
    # Write your code here
    courses = get_courses(std)
    #print(courses)
    codes = my_map(get_ccode,courses)
    #print(codes)
    grades = my_map(get_grade,courses)
    #print(grades)
    grade_lst = []
    for i in range(len(grades)):
        grade_lst += [computeLetterGrade(grades[i])]
    #print(grade_lst)
    return myzip(codes,grade_lst)
    
def convertToWtqp(c_pair):
    return (credit_list[get_ccode(c_pair)],qp_list[get_grade(c_pair)])

def calcGPA(std):
    # Write your code here
    #print(calcLetterGrade(std))
    conv_lst = []
    for i in calcLetterGrade(std):
        conv_lst += [convertToWtqp(i)]
    #print(conv_lst)
    return (sum([i[0]*i[1] for i in conv_lst]))/(sum([i[0] for i in conv_lst]))
    
        
        
    

## For this function to work you first need to write calc_gpa()
def print_students_gpa(std):
    """Prints the students details and GPA"""
    print ("Student Id:", get_id(std))
    print ("Student name:", get_fname(get_name(std)), get_lname(get_name(std)))
    print ("GPA: %.2f" %(calcGPA(std)))
          
