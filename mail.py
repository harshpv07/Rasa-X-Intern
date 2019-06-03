def maill(proj_name,prog_use,proj_idea,proj_application,proj_budget,contact,senderemailadd,receiveremailaddr,senderemailpass):
    import smtplib 
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    s.starttls() 
    # a = str()
    # b = str(senderemailpass)
    # c = str()
    s.login(senderemailadd,senderemailpass) 
    #msg = "hello"
    msg = "CLIENT NEEDS" + "\n" + "Proposed Project Name | " + str(proj_name) + "\n" + "Program to be used | " + str(prog_use) + "\n" +  "Project Idea | " + str(proj_idea) + "\n" + "Project Application | " + str(proj_application) + "\n" + "Project Budget | " + str(proj_budget) + "\n" + "Client Contact Details | " + str(contact) + "\n" + "Do not Reply to this email"
    s.sendmail(senderemailadd,receiveremailaddr,msg)  
    print("Mail Sent")
    s.quit() 
if __name__ == '__main__':
    maill("hey","ho","kf","he",4523,988492123,"harsh.pv07@gmail.com","harsh.pv2017@vitstudent.ac.in","harsh@123")
    
