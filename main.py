import uvicorn
from fastapi import FastAPI, BackgroundTasks
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig



conf = ConnectionConfig(
    MAIL_USERNAME="kidcher1416@gmail.com",
    MAIL_PASSWORD="thonglovelan123",
    MAIL_FROM="kidcher1416@gmail.com",
    MAIL_PORT=587,
    MAIL_SERVER="smtp.gmail.com",
    MAIL_FROM_NAME="Hoang Le Anh Thong",
    MAIL_TLS=True,
    MAIL_SSL=False,
    TEMPLATE_FOLDER='templates/'
)

app = FastAPI(title='API SEND EMAIL')

def send_email_background(background_tasks: BackgroundTasks, subject: str, email_to: str, body: dict):
    message = MessageSchema(
        subject=subject,
        recipients=[email_to],
        template_body=body,
        subtype='html')
    fm = FastMail(conf)
    background_tasks.add_task(
        fm.send_message, message, template_name='email.html')

@app.get("/")
def about():
    return "API SEND EMAIL"
@app.get('/send-email/backgroundtasks')
def send_email_backgroundtasks(background_tasks: BackgroundTasks,email:str):
    name = email.split("@")[0]
    send_email_background(background_tasks, 'Thank You Flow!', email, {'title': 'THANK YOU!', 'name':name})
    return 'Đã gửi thành công'
if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)