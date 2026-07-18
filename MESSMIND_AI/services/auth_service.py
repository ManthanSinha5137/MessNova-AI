from database import db
from core.security import hash_password, verify_password
from datetime import datetime, timedelta
from services.session_service import session
from services.remember_me_service import remember_me


class AuthService:

    # -------------------------
    # Register User
    # -------------------------

    def register_user(
        self,
        full_name,
        email,
        phone,
        password,
        role="Student"
    ):

        existing = db.fetchone(
            "SELECT id FROM users WHERE email=?",
            (email,)
        )

        if existing:
            return False, "Email already exists."

        hashed = hash_password(password)

        db.execute(
            """
            INSERT INTO users
            (
                full_name,
                email,
                phone,
                password_hash,
                role
            )
            VALUES (?,?,?,?,?)
            """,
            (
                full_name,
                email,
                phone,
                hashed,
                role
            )
        )

        return True, "User registered successfully."

    # -------------------------
    # Login
    # -------------------------

    def login_user(self, email, password, remember=False):

        user = db.fetchone(
            """
            SELECT
                id,
                full_name,
                email,
                password_hash,
                role,
                failed_attempts,
                locked_until,
                is_active
            FROM users
            WHERE email=?
            """,
            (email,)
        )

        if not user:
            return False, "User not found."

        (
            user_id,
            name,
            email,
            password_hash,
            role,
            failed_attempts,
            locked_until,
            is_active
        ) = user

        if not is_active:
            return False, "Account is disabled."

        if locked_until:

            locked_time = datetime.fromisoformat(locked_until)

            if datetime.now() < locked_time:

                remaining = locked_time - datetime.now()

                minutes = int(remaining.total_seconds() // 60) + 1

                return False, f"Account locked. Try again in {minutes} minute(s)."

            db.execute(
                """
                UPDATE users
                SET
                    locked_until = NULL,
                    failed_attempts = 0
                WHERE id = ?
                """,
                (user_id,)
            )

        if verify_password(password, password_hash):

            db.execute(
                """
                UPDATE users
                SET failed_attempts=0,
                    last_login=CURRENT_TIMESTAMP
                WHERE id=?
                """,
                (user_id,)
            )

            user_data = {
                "id": user_id,
                "name": name,
                "email": email,
                "role": role
            }

            session.create_session(user_data)

            if remember:
               remember_me.save_user(user_data)

            return True, user_data

        failed_attempts += 1

        db.execute(
            """
            UPDATE users
            SET failed_attempts=?
            WHERE id=?
            """,
            (failed_attempts, user_id)
        )

        if failed_attempts >= 5:

            lock_until = datetime.now() + timedelta(minutes=30)

            db.execute(
                """
                UPDATE users
                SET
                    failed_attempts = 0,
                    locked_until = ?
                WHERE id = ?
                """,
                (
                    lock_until.isoformat(),
                    user_id
                )
            )

            return False, "Too many failed attempts. Account locked for 30 minutes."

        return False, f"Incorrect password. Attempts left: {5 - failed_attempts}"

    # -------------------------
    # Create Default Super Admin
    # -------------------------

    def create_default_super_admin(self):

        admin = db.fetchone(
            """
            SELECT id
            FROM users
            WHERE role = ?
            """,
            ("Super Admin",)
        )

        if admin:
            return

        hashed = hash_password("Admin@123")

        db.execute(
            """
            INSERT INTO users
            (
                full_name,
                email,
                phone,
                password_hash,
                role
            )
            VALUES (?,?,?,?,?)
            """,
            (
                "Manthan Sinha",
                "kanhaasinha9@gmail.com",
                "",
                hashed,
                "Super Admin"
            )
        )

        print("✅ Default Super Admin Created")


auth = AuthService()