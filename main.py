import os 
from Email import Email

# link='recruitment-task-backend-internship-main\emails\\'
# files_in_directory = os.listdir(link)
allmails=[]
# txt_format_files = filter(lambda x: x[-4:] == '.txt', files_in_directory)
# csv_format_files = filter(lambda x: x[-4:] == '.csv', files_in_directory)



task_email= Email()
allmails=task_email.incorrect_emails(allmails) #csv_format_files,allmails,txt_format_files
task_email.seach_in_emails('agustin',allmails)
task_email.list_domains(allmails)
task_email.not_logged_emails(allmails)