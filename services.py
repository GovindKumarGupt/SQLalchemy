from sqlalchemy import select
from db import SessionLocal
from models import User

# --- 1. CREATE (डेटा सम्मिलित करना) ---
def create_user(name: str, email: str):
    # 'with' स्टेटमेंट का उपयोग करने से काम पूरा होने पर सेशन अपने आप बंद हो जाता है
    with SessionLocal() as session:
        # यूजर ऑब्जेक्ट बनाना
        new_user = User(name=name, email=email)
        session.add(new_user)  # सेशन में जोड़ना
        session.commit()       # डेटाबेस में स्थायी रूप से सेव करना
        print(f"User {name} created successfully!")

# --- 2. READ SINGLE RECORD (एक यूजर ढूंढना) ---
def get_single_user(user_id: int):
    with SessionLocal() as session:
        # session.get() सीधे प्राइमरी की (ID) के आधार पर डेटा खोजता है
        user = session.get(User, user_id)
        return user

# --- 3. READ ALL RECORDS (सभी यूज़र्स की लिस्ट निकालना) ---
def get_all_users():
    with SessionLocal() as session:
        # SQL: SELECT * FROM users;
        statement = select(User)
        # session.scalars() हमें ऑब्जेक्ट्स की एक क्लीन लिस्ट देता है
        users = session.scalars(statement).all()
        return users

# --- 4. UPDATE (डेटा अपडेट करना) ---
def update_user_email(user_id: int, new_email: str):
    with SessionLocal() as session:
        # पहले उस यूजर को ढूंढें जिसे अपडेट करना है
        user = session.get(User, user_id)
        if user:
            user.email = new_email  # वैल्यू बदलना
            session.commit()         # बदलावों को सेव करना
            print(f"User ID {user_id} email updated!")
            return user
        print("User not found!")
        return None

# --- 5. DELETE (डेटा हटाना) ---
def delete_user(user_id: int):
    with SessionLocal() as session:
        user = session.get(User, user_id)
        if user:
            session.delete(user)    # डिलीट के लिए मार्क करना
            session.commit()        # डेटाबेस से हटाना
            print(f"User ID {user_id} deleted successfully!")
        else:
            print("User not found!")