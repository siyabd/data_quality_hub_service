import re

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        return format_output("Email is valid.", "Pass")
    return format_output("Email validation failed.", "Fail")

def validate_gender(genderList,request):
    for x in genderList:
        print(x['code'])
        if(x['code'] == request.data):
            return format_output("Gender has been validated.", "pass")
    return format_output("Gender is not valid & does not exist.", "Fail")


def  default_message():
    return format_output("Validation not yet added.", "Not Valid")

def format_output(message, status):
    return {"message": message,  "status":status}







