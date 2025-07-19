import pymysql

# Connect to MySQL
def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="Abd@123",
        database="studentinfo"
    )

# Signup function
def signup():
    print("\n🔐 SIGN UP")
    name = input("👤 Enter name: ")
    age = int(input("🎂 Enter age: "))
    gender = input("⚧️ Enter gender (Male/Female): ")
    class_name = input("🏫 Enter class: ")
    email = input("📧 Enter email: ")
    address = input("🏠 Enter address: ")

    try:
        conn = get_connection()
        cursor = conn.cursor()
        insert_query = """
            INSERT INTO students (name, age, gender, class, email, address)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(insert_query, (name, age, gender, class_name, email, address))
        conn.commit()
        print("✅ Signup successful!")
    except Exception as e:
        print(f"❌ Signup error: {e}")
    finally:
        conn.close()

# Signin function
def signin():
    print("\n🔓 SIGN IN")
    email = input("📧 Enter your email: ")
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students WHERE email = %s", (email,))
        user = cursor.fetchone()
        if user:
            print(f"✅ Signin successful! Welcome, {user[1]} ❤️")
        else:
            print("❌ No user found with this email.")
    except Exception as e:
        print(f"❌ Signin error: {e}")
    finally:
        conn.close()

# Show students
def show_students():
    print("\n📋 ALL STUDENTS")
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()
        for student in students:
            print(f"ID: {student[0]}, Name: {student[1]}, Email: {student[5]}")
    except Exception as e:
        print(f"❌ Error fetching students: {e}")
    finally:
        conn.close()

# Delete student
def delete_student():
    print("\n🗑️ DELETE STUDENT")
    email = input("📧 Enter email of student to delete: ")
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM students WHERE email = %s", (email,))
        conn.commit()
        if cursor.rowcount > 0:
            print("✅ Student deleted successfully.")
        else:
            print("❌ No student found with this email.")
    except Exception as e:
        print(f"❌ Delete error: {e}")
    finally:
        conn.close()

# 🎯 Main Menu
def main():
    while True:
        print("\n============================")
        print("🎓 STUDENT MANAGEMENT SYSTEM")
        print("============================")
        print("1. Signup (New Student)")
        print("2. Signin (Check Existing)")
        print("3. Show All Students")
        print("4. Delete Student")
        print("5. Exit")
        choice = input("🧭 Choose option (1-5): ")

        if choice == '1':
            signup()
        elif choice == '2':
            signin()
        elif choice == '3':
            show_students()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            print("👋 Exiting... Bye love! 💖")
            break
        else:
            print("❌ Invalid choice, try again!")

# Run the app
if __name__ == "__main__":
    main()
