from app.models.models import Database

## create database
if __name__ == "__main__":
    with Database("contacts.sqlite3") as cursor:
        cursor.create_table("contacts", ["name", "email", "phone", "country", "gender", "hair_type", "hair_color",
                                        "loss_time", "treatment", "plan", "medicines", "diseases"])

