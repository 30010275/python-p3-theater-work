from models.database import SessionLocal
from models.audition import Audition
from models.role import Role

session = SessionLocal()

def list_roles():
    roles = session.query(Role).all()
    for role in roles:
        print(f"🎭 Role: {role.character_name}")

def list_auditions():
    auditions = session.query(Audition).all()
    for audition in auditions:
        print(f"🎭 Actor: {audition.actor} | Location: {audition.location} | Hired: {audition.hired}")

def hire_actor(actor_name):
    audition = session.query(Audition).filter_by(actor=actor_name).first()
    if audition:
        audition.call_back()
        session.commit()
        print(f"✅ {actor_name} has been hired!")
    else:
        print("❌ Actor not found.")

def main():
    while True:
        print("\n Theater Audition System ")
        print("1️ List Roles")
        print("2️ List Auditions")
        print("3️ Hire an Actor")
        print("4️ Exit")

        choice = input("Select an option: ")

        if choice == "1":
            list_roles()
        elif choice == "2":
            list_auditions()
        elif choice == "3":
            actor_name = input("Enter actor name to hire: ")
            hire_actor(actor_name)
        elif choice == "4":
            print("👋 Exiting...")
            break
        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    main()
