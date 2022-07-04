import pandas
import os 
class Email :
    # this function take csv_format_files and txt_format_files list they include name of files in emails folder
    # and allmails list to append correct email adress.
    #  in here I prefer to take allmails for future project it can be easy to adapt next project
    def incorrect_emails(self,allmails):
        link='recruitment-task-backend-internship-main\emails\\'
        files_in_directory = os.listdir(link)
        txt_format_files = filter(lambda x: x[-4:] == '.txt', files_in_directory)
        csv_format_files = filter(lambda x: x[-4:] == '.csv', files_in_directory)
        wrong_emails=[]
        #  this function can be outside  of incorrect_emails for future porjects 
        def chech_email(email):
            list=email.split('@')

            if len(list)==2 and len(list[0])>1 :
                domain=list[1]
                list2=domain.split('.')
                if len(list2)==2 and len(list2[0])>1 and len(list2[1])>1 and len(list2[1])<5 :
                    return True
                else:
                    return False
            else:
                return False
        # for csv files pandas read tezt and separete all to turn them same format as txt file
        for i in csv_format_files:
            link='recruitment-task-backend-internship-main\emails\\'
            data = pandas.read_csv(link+i, sep = ';' )
            for i in data['email']:
                if chech_email(i):
                    allmails.append(i) 
                else:
                    wrong_emails.append(i)
        # for txt files created different for loop because csv files has different text format
        for i in txt_format_files:
            with open (link+i) as file:
                context=file.read().split()
                for i in context:
                    if chech_email(i):
                        allmails.append(i) 
                    else:
                        wrong_emails.append(i)
        with open('task_1_myanswer.txt', 'w') as f:
            f.write(f"Invalid emails ({len(wrong_emails)})")
            f.write('\n')
            for mail in wrong_emails:
                f.write(f"    {mail}")
                f.write('\n')
        return allmails
    # this function take a string to search in allmails
    def seach_in_emails(self,string,allmails):
        results=[]
        for x in allmails: 
            if string in x:
                results.append(x)
        with open('task_2_myanswer.txt', 'w') as f:
                f.write(f"Found emails with '{string}' in email  ({len(results)})")
                f.write('\n')
                for mail in results:
                    f.write(f"    {mail}")
                    f.write('\n')
    # it categorize all emails according to domains
    def list_domains(self,allmails):
        domains=[]
        for i in allmails:
            splited=i.split('@')
            if splited[1] not in domains:
                domains.append(splited[1])
        domains.sort(reverse=False, key=str.lower)
        for j in domains:
            str_match = [s for s in allmails if s.__contains__(j)]
            str_match.sort()
            with open('task_3_myanswer.txt', 'a') as f:
                f.write(f"Domain {j} ({len(str_match)})")
                f.write('\n')
            
                for mail in str_match:
                    f.write(f"    {mail}")
                    f.write('\n')
    # this file compare allmails with email-send.logs file. it write mails not got mail in to task_4_myanswer.txt.
    def not_logged_emails(self,allmails):
        notsended=[]
        with open ('recruitment-task-backend-internship-main\email-sent.logs','r') as file:
            context=file.read() 
            for j in allmails:
                    if not context.__contains__(j):
                        notsended.append(j)
            with open('task_4_myanswer.txt', 'w') as f:
                f.write(f"Emails not sent ({len(notsended)})")
                f.write('\n')
                for mail in notsended:
                    f.write(f"    {mail}")
                    f.write('\n')
