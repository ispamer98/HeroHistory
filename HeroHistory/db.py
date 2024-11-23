#db.py


from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker, declarative_base

# Cambia estos valores con tus credenciales de Clever Cloud
DATABASE_USER = "uo4wvrncygvs6aq1"
DATABASE_PASSWORD = "2kBFDMWBcocBqIvGmOoH"
DATABASE_HOST = "bd7z4fvndjni59wutymm-mysql.services.clever-cloud.com"
DATABASE_PORT = "3306"  # generalmente 3306 para MySQL
DATABASE_NAME = "bd7z4fvndjni59wutymm"

# Crear la cadena de conexión
connection_string = f"mysql+pymysql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"

# Configurar el engine y la sesión
engine = create_engine(connection_string, pool_pre_ping=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
db_session = Session()

#Esto no conecta inmediatamente con la db, hay que hacerlo aparte

#Creamos la sesion, que es la que nos permite realizar transacciones en la base de datos

#Creamos una función para la primera vez que se inicie la app
def first_start():
    from .models import User  # Importamos los modelos aquí para evitar conflictos

    # Crear todas las tablas si aún no existen
    Base.metadata.create_all(engine)

    try:
        # Hacer una consulta para verificar si existen usuarios
        users = db_session.query(User).all()

        # Si no existen usuarios, creamos uno de muestra
        if not users:
            user = User(username="user1", pasw="user1", email="user1@user.com", birthday="30/01/2000", verify=True, avatar="/avatar3.png")
            user2 = User(username="user2", pasw="user2", email="user2@user.com", birthday="30/01/2000", verify=True,admin=True)
            user3 = User(username="user3", pasw="user3", email="user3@user.com", birthday="30/01/2000", verify=True)
            user4 = User(username="user4", pasw="user4", email="user4@user.com", birthday="30/01/2000", verify=True)
            users=[user, user2, user3, user4]
            for user in users:
                db_session.add(user)
                db_session.commit()
            print("Usuarios de muestra creado correctamente.")
        else:
            print("La base de datos ya tiene usuarios.")

    except SQLAlchemyError as e:
        db_session.rollback()
        print(f"Error en la transacción: {e}")
    finally:
        # Cerrar la sesión siempre, incluso en caso de excepción
        db_session.close()


