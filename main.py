from models import create_tables
from services import (
    create_user, 
    get_single_user, 
    get_all_users, 
    update_user_email, 
    delete_user
)

if __name__ == "__main__":
    # स्टेप 1: टेबल बनाएं (यदि पहले से नहीं बनी है)
    create_tables()
    
    # स्टेप 2: नया यूजर जोड़ें (Create)
    # create_user(name="Sonam", email="sonam@example.com")
    # create_user(name="Raj", email="raj@example.com")
    
    # स्टेप 3: सिंगल यूजर का डेटा देखें (Read Single)
    # user = get_single_user(user_id=1)
    # print("Single User Data:", user)
    
    # स्टेप 4: सभी यूज़र्स की लिस्ट देखें (Read All)
    # all_users = get_all_users()
    # print("All Users List:", all_users)
    
    # स्टेप 5: यूजर का ईमेल अपडेट करें (Update)
    # update_user_email(user_id=1, new_email="sonam.new@domain.com")
    
    # स्टेप 6: यूजर को डिलीट करें (Delete)
    # delete_user(user_id=2)