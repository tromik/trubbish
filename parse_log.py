import smtplib
from email.mime.text import MIMEText
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders

# log file vars
filename = 'p_DataMart_to_GP_Write_Barbados_Live_2016-10-27_00-00.log'
process = 'p_DataMart_to_GP_Write'
exec_end_str = 'Project Execution End'

def read_log(filename):
    fnd_end = False
    with open(filename, 'r') as f:
        for line in f:
            if process and exec_end_str in line:
                # Found process execution end line
                fnd_end = True
                if not 'successfully' in line:
                    # Process completed but did so with errors
                    return False
        # Process did not complete; exited before end
        return fnd_end



if not read_log(filename):
    sender = 'integration@gadventures.com'
    recipients = ['tomr@gadventures.com', 'tomr@gadventures.com']

    msg = MIMEMultipart()

    msg['Subject'] = 'Error in log' # % textfile
    msg['From'] = sender
    msg['To'] =  ", ".join(recipients)

    body = 'Process ' + process + ' did not complete successfully!'

    msg.attach(MIMEText(body, 'plain'))

    attachment = open(filename, "rb")

    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    msg.attach(part)

    s = smtplib.SMTP('10.11.0.26')
    s.sendmail(sender, recipients, msg.as_string())
    s.quit()
    attachment.close()
