from django.shortcuts import render
from django.core.mail import send_mail

def employee_form(request):

    if request.method == "POST":

        name = request.POST.get('name')
        number = request.POST.get('number')
        email = request.POST.get('email')
        designation = request.POST.get('designation')

        subject = "New Employee Details"

        message = f"""
        Name : {name}
        Mobile Number : {number}
        Email : {email}
        Designation : {designation}
        """

        send_mail(
            subject,
            message,
            'towersecuritycompany@gmail.com',
            ['towersecuritycompany@gmail.com'],
            fail_silently=False
        )

        return render(request,'success.html')

    return render(request,'index.html')