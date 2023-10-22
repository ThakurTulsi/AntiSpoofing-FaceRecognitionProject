import tkinter as tk
from tkinter import messagebox
import re
import uuid
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class App:
    
    def __init__(self) -> None:
        self.main_window = tk.Tk()
        self.main_window.geometry('1200x520')
        
        self.main_window_register_button = tk.Button(
                        self.main_window,
                        text="register",
                        activebackground="black",  # bg color of btn when clicked or activated
                        activeforeground="white",   # color of btn text when clicked
                        fg='white',                      # foreground color , color of btn text
                        bg='red',
                        command=self.register_action,            #what happens when btn clicked
                        height=2,
                        width=20,
                        font=('Helvetica bold', 20)
                    )
        self.main_window_login_button = tk.Button(
                        self.main_window,
                        text="login",
                        activebackground="black",  # bg color of btn when clicked or activated
                        activeforeground="white",   # color of btn text when clicked
                        fg='white',                      # foreground color , color of btn text
                        bg='green',
                        command=self.login_action,            #what happens when btn clicked
                        height=2,
                        width=20,
                        font=('Helvetica bold', 20)
                    )
        self.main_window_register_button.place(x=800,y=100)
        self.main_window_login_button.place(x=800,y=300)

        self.user_dir = './Users'
        if not os.path.exists(self.user_dir):
            os.makedirs(self.user_dir)
    

    
    def register_action(self):
        self.register_window = tk.Toplevel(self.main_window)
        self.register_window.geometry('1200x520+130+130')
        
        self.name_label = tk.Label(self.register_window,text="name")
        self.name_label.config(font=("sans-serif", 13), justify="left")
        self.name_label.place(x=800,y=50)
        self.name_entry_text = tk.Text(self.register_window,height=1,width=20, font=("Arial", 12))
        self.name_entry_text.place(x=860,y=50)
        
        
        self.email_label = tk.Label(self.register_window,text="email")
        self.email_label.config(font=("sans-serif", 13), justify="left")
        self.email_label.place(x=800,y=80)
        self.email_entry_text = tk.Text(self.register_window,height=1,width=20, font=("Arial", 12))
        self.email_entry_text.place(x=860,y=80)
        
        self.accept_btn = tk.Button(self.register_window,text='Accept new user',background='red',fg='white',height=2,command=self.accept_action)
        self.accept_btn.place(x=800,y=180)
        
    def login_action(self):
        pass
    
    def accept_action(self):
        name = self.name_entry_text.get(1.0,"end-1c")
        email = self.email_entry_text.get(1.0,"end-1c")
        
        isNameValid = self.validate_name(name)
        isEmailVAlid = self.validate_email(email)
        # print(name,email)
        
        if isNameValid and isEmailVAlid:
            #aage ka code 
            print("valid")
            
            self.generate_id(name,email)
            
    
    
    
    def user_email_registration(self,user_id,name,email):
        # print(f"email:{email}, name:{name},uid:{user_id}")
        sender_email = "rutupri123@gmail.com"
        receiver_email =  email
        subject = "Registration Successfull!"
        message = f"Dear {name} Congratulations! You have registered successfully, your unique user-id is:{user_id}.Thank you!!"

        
        # Create a multipart message object
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = receiver_email
        msg["Subject"] = subject
        
        # Attach the message to the email
        msg.attach(MIMEText(message, "plain"))
        
        # SMTP configuration
        smtp_host = "smtp.gmail.com"  # Replace with your SMTP host
        smtp_port = 587  # Replace with your SMTP port
        smtp_username = "admin_test"  # Replace with your SMTP username
        smtp_password = "vvgpsblurcmqfarh"  # Replace with your SMTP password
        
    
        try:
        # Create a SMTP session
            with smtplib.SMTP(smtp_host, smtp_port) as server:
                server.starttls()
            
                # Login to the SMTP server
                server.login("rutupri123@gmail.com", smtp_password)
            
                # Send the email
                server.sendmail(sender_email, receiver_email, msg.as_string())
        
            print("Registration email sent successfully!")
            
        except smtplib.SMTPException as e:
            print("Error sending registration email:", str(e))

# Example usage

       
    
    def validate_name(self,name):
        if name=='':
            messagebox.showerror("Invalid Name", "Please enter a valid name")
            self.register_window.destroy()
            return False
        
        return True
    
    def validate_email(self,email):
         # Check if email contains '@' symbol
        if '@' not in email:
            tk.messagebox.showerror("Invalid Email", "Email must contain '@' symbol.")
            self.register_window.destroy()
            return False

        # Check if email contains special characters
        if not re.match(r'^[a-zA-Z0-9_]+$', email.split('@')[0]):
            tk.messagebox.showerror("Invalid Email", "Email should not contain special characters.")
            self.register_window.destroy()
            return False

        # If all validations pass
        return True
        

        
        
    
    def start(self):
        self.main_window.mainloop()
    
    
if __name__=='__main__':    
    app = App()
    app.start()