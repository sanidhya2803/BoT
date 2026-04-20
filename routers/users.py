from fastapi import APIRouter, Depends, UploadFile, File
from model import schemas
from dependencies import dependency
from llm import response
from groq import Groq 
from openai import Client
import os
from dotenv import load_dotenv
load_dotenv()
GROQ_API_KEY = os.getenv("groq_api_key")
client = Groq(api_key=GROQ_API_KEY)

router = APIRouter()

#---------------------------------------------------------------------Register User-----------------------------------------------------------------------------#
@router.post("/register_user")
def register_user(user:schemas.Register_User, db = Depends(dependency.connections)):
    try:
        query = "select email from users where email = %s"
        db.execute(query,(user.email,))
        result = db.fetchone()

        if result:
            return {"Message":"Email already Registered!!"}

        query = """
    insert into users(email,name,age,password)
    values(%s,%s,%s,%s)
    """

        db.execute(query,(user.email,user.name,user.age,user.password))
        db.connection.commit()

        return {"message":"Account Created!!"}

    except Exception as e:
        return {"Error":str(e)}
    
#---------------------------------------------------------------------Login User-----------------------------------------------------------------------------#
@router.post("/login_user")
def login_user(user:schemas.Login_User,db=Depends(dependency.connections)):

    query = "select name,password from users where email = %s"

    db.execute(query,(user.email,))
    
    result = db.fetchone()
    
    if result:
        if user.password == result["password"]:
            return {"user":result["name"]}
        else:
            return {"error":"Invalid Password!!"}
        
    else:
        return {"error":"Email not registered!!"}

#---------------------------------------------------------------------User Info-----------------------------------------------------------------------------#

@router.get("/user_info")
def user_info(email:str,db = Depends(dependency.connect)):

    query = "select email, name, age from users where email = %s"

    db.execute(query,(email,))
    result = db.fetchone()
    if result:
        return {"message":{"email":result["email"],
                           "name":result["name"],
                           "age":result["age"]}}
    
#---------------------------------------------------------------------Single Query Chat Bot-----------------------------------------------------------------------------#
@router.post("/chat")
def user_input(chat:schemas.UserChat):

    result = response.llm_response(chat.message)

    return {"message":result}

#---------------------------------------------------------------------Chat History ChatBot-----------------------------------------------------------------------------#
@router.post("/history_chat")
def history_chat(chat:schemas.ChatRequest):
    try:
        messages = chat.messages

        chat_history = []
        for msg in messages:
            chat_history.append({
                "role":msg.role,
                "content":msg.content
            })

        response = client.chat.completions.create(
            model = "llama-3.3-70b-versatile",
            messages = chat_history
        )

        reply = response.choices[0].message.content

        return {"response":reply}
    
    except Exception as e:
        return {"error":str(e)}
    
#---------------------------------------------------------------------File Upload-----------------------------------------------------------------------------#
@router.post("/file_upload")
async def file_upload(file: UploadFile = File(...)):

    content = await file.read()

    return{
        "filename": file.filename,
        "type": file.content_type,
        "content": len(content)
    }


        
