from database import db
from core.security import hash_password


def create_user(full_name, email, phone, password, role):

    hashed_password = hash_password(password)

    query = """
    INSERT INTO users
    (
        full_name,
        email,
        phone,
        password_hash,
        role
    )

    VALUES(?,?,?,?,?)
    """

    db.execute(
        query,
        (
            full_name,
            email,
            phone,
            hashed_password,
            role
        )
    )

    return True