from connection_orm import Base, engine, session
from User import User
from Post import Post

# Create tables
Base.metadata.create_all(engine)

def show_menu():
  print("Options Menu")
  print('1 - New User')
  print('2 - New Post')
  print('3 - Show posts and users')
  print('4 - Exit')

def new_user():
  name = input("Enter name: ")
  email = input("Enter email: ")
  user = User(name, email)
  session.add(user)
  session.commit()
  print('\nUser created successfully\n')

def new_post():
  title = input("Enter title: ")
  content = input("Enter content: ")
  author_id = input("Enter author ID: ")
  user = session.query(User).filter_by(id=author_id).first()
  
  if user:
    post = Post(title, content, author_id)
    session.add(post)
    session.commit()
    print('\nPost created successfully\n')
  else: 
    print('\nUser not found\n')
    
def show_posts_and_users():
  users = session.query(User).join(User.post).order_by(User.name).all()
  
  for user in users:
    print(f"\n{user.name} - {user.email}")
    for post in user.post:
      print(f"{post.title}")
      print(f"{post.content}")
    