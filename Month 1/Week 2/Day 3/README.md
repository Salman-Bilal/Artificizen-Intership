# Day 03 – Database Integration with SQLAlchemy & CRUD Operations 🗄️

## Overview 📝
This folder contains my solutions and practice exercises completed during Day 03 of Week 02 of the internship training plan. The focus of this day was setting up relational databases in FastAPI using SQLAlchemy, establishing relationships, managing sessions using dependency injection (`yield`), performing standard CRUD operations, and enforcing the clean architecture pattern of separating Database Models from Pydantic Schemas.

---

## Topics Covered 📚

### SQLAlchemy Setup & Configuration
* Installing required database drivers and toolkits
* Configuring the Database URL string format
* Creating the database factory components: `create_engine()`, `SessionLocal`, and defining the `Base = declarative_base()` model catalog

### SQLAlchemy Database Models
* Constructing data schemas inheriting from `Base`
* Defining column parameters: `Column`, `Integer`, `String`, `Boolean`, and `ForeignKey`
* Establishing table linkages using `relationship()` for one-to-many and many-to-one mapping

### Dependency Injection (`get_db`)
* Managing stateful connection sessions cleanly using a generator function with `yield`
* Protecting database transactions and closing sessions safely post-execution via `Depends(get_db)`

### CRUD Operations
* **Create:** Persisting records using `db.add()`, `db.commit()`, and updating instances with `db.refresh()`
* **Read:** Fetching datasets using `db.query().filter()`, `.first()`, and `.all()`
* **Update/Delete:** Modifying existing rows or removing items cleanly from the session tree

### Architectural Cleanliness
* Strict boundaries: Never exposing SQLAlchemy ORM models directly to the consumer
* Transforming data safely by mapping database attributes into validated Pydantic schemas before output

### Alembic Basics (Theory)
* Initializing database migration environments with `alembic init`
* Tracking structural state changes using `alembic revision --autogenerate`
* Moving schema states forward using `alembic upgrade head`

---

## Practice Questions Implemented 🛠️

### 1. SQLAlchemy SQLite Setup & Table Initialization
Configured SQLAlchemy to work locally with an SQLite database instance (`app.db`). Built a `User` model complete with `id`, `name`, `email`, and an `is_active` boolean status flag. Triggered structural initialization using `Base.metadata.create_all()`.

* **Concepts Used:** `create_engine`, `declarative_base`, `Column`, `Base.metadata.create_all`
* **File:** `1_Create_User_Model.py`

### 2. Dependency Injection & POST User Endpoints
Developed a reusable `get_db()` session generator context. Attached this database yield engine directly into a `POST /users` endpoint to safely handle incoming validation models and persist new records to the user database table.

* **Concepts Used:** Generator Function, `yield`, `Depends`, `db.add()`, `db.commit()`
* **File:** `2_Get_DB_Using_Yeild.py`

### 3. GET Single User Entry By ID
Constructed a parameterized route handler path `GET /users/{user_id}` designed to pull precise records matching a specific index key. Built conditional checks to trigger standard `HTTP 404 Not Found` payload errors if the search index fails to exist.

* **Concepts Used:** Query Filtering, `filter().first()`, `HTTPException`, 404 Status Handling
* **File:** `3_Fetch_Usres_From_DB.py`

### 4. Paginated User Lists (Skip & Limit Contexts)
Created a comprehensive search endpoint `GET /users` capable of managing large datasets gracefully through offset parameters (`skip`) and capacity ceilings (`limit`).

* **Concepts Used:** Database Pagination, `.offset()`, `.limit()`, Query parameters
* **File:** `4_Get_User_using_Skip_Limit.py`

### 5. Document Removal Routing (DELETE Operations)
Wrote an operation path `DELETE /users/{user_id}` engineered to find targeting record IDs, safely drop them from the table space, track the commit transaction, and respond back cleanly with an empty payload status `204 No Content`.

* **Concepts Used:** Database Removal, `db.delete()`, status code `204_NO_CONTENT`
* **File:** `5_Delete_User.py`

### 6. Relational Table Mapping & User Posts
Expanded the application database logic by designing a nested child model (`Post`) tied explicitly back to a specific parent account through a relative `ForeignKey` attribute mapping. Created an interconnected routing path `GET /users/{user_id}/posts` to easily query and list all sub-post child collections owned by that precise user tracking ID.

* **Concepts Used:** One-to-Many Relationships, `ForeignKey`, `relationship()`, Cross-Table Filtering
* **File:** `6_Post_Model.py`

---

## Folder Structure 📂

```text
Week 2/
└── Day 3/
    ├── 1_Create_User_Model.py
    ├── 2_Get_DB_Using_Yeild.py
    ├── 3_Fetch_Usres_From_DB.py
    ├── 4_Get_User_using_Skip_Limit.py
    ├── 5_Delete_User.py
    ├── 6_Post_Model.py
    ├── app.db
    └── README.md