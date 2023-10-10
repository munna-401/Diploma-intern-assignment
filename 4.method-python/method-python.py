#Python Method Calling
def my_name_is():
    print("My name is  munna")


def i_have_enrolled_course(course_name):
    print(f"I have enrolled in a course named {course_name}")


def i_have_learning(backend, frontend):
    return f"Learning {backend}, {frontend}"

course_and_learn=[
     
            { "course":"Python & Web",
                "learn": "Python, HTML, CSS, Bootstrap"
            },
         
            {
                "course": "Java Spring Boot",
                "learn": "Java, HTML, CSS, Hibernet"
            },
           
               
            { 
                  "course": "C# & ASP.NET Core",
                "learn": "C#, Entity Framework, Razor"
            },
           
             {
                   "course": "MERN Development",
               "learn": "Node, React, HTML, CSS"
             },
             {
                  "course": "PHP & Laravel",
                "learn": "PHP, Blade, Eloquent"
             }
         ]


for x in course_and_learn:
        my_name_is()
        i_have_enrolled_course("Python & Web")
        result = i_have_learning("Python", "HTML, CSS, JavaScript")
        print(result)
print(x["course"],x["learn"])