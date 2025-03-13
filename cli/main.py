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

def add_role(role_name):
    new_role = Role(character_name=role_name)
    session.add(new_role)
    session.commit()
    print(f"✅ Role '{role_name}' added!")

def fetch_lead(role_name):
    role = session.query(Role).filter_by(character_name=role_name).first()
    if role:
        return role.lead()
    return "❌ Role not found."

def fetch_understudy(role_name):
    role = session.query(Role).filter_by(character_name=role_name).first()
    if role:
        return role.understudy()
    return "❌ Role not found."

def add_audition(actor, location, phone):
    new_audition = Audition(actor=actor, location=location, phone=int(phone))
    session.add(new_audition)
    session.commit()
    print(f"✅ Audition for '{actor}' added!")

def main():
    print("Welcome to the Theater Audition System!")
    while True:
        print("\n Theater Audition System ")
        print("1️ List Roles")
        print("2️ List Auditions")
        print("3️ Hire an Actor")
        print("4️ Add Role")
        print("5️ Add Audition (actor, location, phone)")
        print("6️ Fetch Lead for Role")
        print("7️ Fetch Understudy for Role")
        print("8️ Exit")

        choice = input("Select an option: ")

        if choice == "1":
            list_roles()
        elif choice == "2":
            list_auditions()
        elif choice == "3":
            actor_name = input("Enter actor name to hire: ")
            hire_actor(actor_name)
        elif choice == "4":
            role_name = input("Enter role name: ")
            add_role(role_name)
        elif choice == "5":
            audition_details = input("Enter audition details (actor, location, phone): ").split(", ")
            if len(audition_details) == 3:
                actor, location, phone = audition_details
                add_audition(actor, location, phone)
            else:
                print("❌ Invalid input. Please provide all details.")
        elif choice == "6":
            role_name = input("Enter role name to fetch lead: ")
            lead = fetch_lead(role_name)
            print(lead)
        elif choice == "7":
            role_name = input("Enter role name to fetch understudy: ")
            understudy = fetch_understudy(role_name)
            print(understudy)
        elif choice == "8":
            print("👋 Exiting...")
            break
        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    main()
