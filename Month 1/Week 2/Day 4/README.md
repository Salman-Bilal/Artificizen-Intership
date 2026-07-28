# Day 04 – Authentication, Security & Role-Based Access Control 🔐

## Overview 📝
This folder contains my solutions and practice exercises completed during Day 04 of Week 02 of the internship training plan. The focus of this day was implementing secure authentication and authorization protocols in FastAPI. This includes password hashing using `passlib`, OAuth2 specifications, token generation via JSON Web Tokens (JWT), protecting routes using custom dependencies, and enforcing Role-Based Access Control (RBAC).

---

## Topics Covered 📚

### Password Security & Hashing
* Setting up safe hashing mechanics: `pip install "passlib[bcrypt]"`
* Initializing hashing configurations using `CryptContext`
* Implementing safe operations for plaintext conversions with `.hash()` and `.verify()`

### OAuth2 Password Flow
* Utilizing FastAPI's built-in security utilities: `OAuth2PasswordBearer` and `OAuth2PasswordRequestForm`
* Parsing OAuth2 compliant form data fields securely from request payloads

### JSON Web Tokens (JWT)
* Setting up token encryption utilities: `pip install "python-jose[cryptography]"`
* Compiling payload parameters and generating claims with `jwt.encode()` and decoding them with `jwt.decode()`
* Tracking lifespan limits using the `exp` claim and Python’s `timedelta`

### Protected Routes & Dependency Injection
* Creating a robust `get_current_user` dependency to capture and validate `Authorization: Bearer <token>` headers
* Raising structured `HTTP 401 Unauthorized` credentials exceptions when token decoding fails

### Role-Based Access Control (RBAC)
* Extending user payload schemas to support dedicated authorization scopes (e.g., `role`)
* Implementing route guards using custom dependencies (`require_admin`) to raise `HTTP 403 Forbidden` errors for unauthorized operations

### Environment Configuration
* Handling sensitive parameters outside of source code using `python-dotenv`
* Externalizing secrets like `SECRET_KEY` and token signing `ALGORITHM` safely

---

## Practice Questions Implemented 🛠️

### 1. Password Hashing Utility
Created standalone functions `hash_password()` and `verify_password()` using Passlib's bcrypt context. Verified password verification and mathematical hashing integrity in isolation before integration.

* **Concepts Used:** `CryptContext`, `pwd_context.hash()`, `pwd_context.verify()`
* **File:** `1_Hash_&_Verify_Password_Using_Passlib.py`

### 2. Secure User Registration Endpoint
Developed a `POST /auth/register` API route that parses registration requests, hashes raw user passwords, and registers new active user accounts into the database.

* **Concepts Used:** Registration Schema, Password Security, Database Persistence
* **File:** `2_Post_User_&_Hash_Password.py`

### 3. OAuth2 Token Generation (Login Flow)
Implemented the official `POST /auth/token` endpoint utilizing FastAPI's standard `OAuth2PasswordRequestForm`. It verifies database credentials against stored password hashes and returns a valid, signed JWT access token.

* **Concepts Used:** `OAuth2PasswordRequestForm`, JWT Signatures, Expire Time Windows
* **File:** `3_OAuth_Password_Request_Using_JWT.py`

### 4. JWT Extraction & Current User Dependency
Wrote the critical security dependency `get_current_user`. This reads the incoming Bearer token from headers, decrypts the claims, validates authenticity, and returns the authenticated user context object.

* **Concepts Used:** `OAuth2PasswordBearer`, Token Decoding, JWT Claims, Context Injection
* **File:** `4_Get_Current_User_Using_JWT.py`

### 5. Securing User Endpoints
Applied the `get_current_user` guard to a newly defined `GET /users/me` endpoint. This locks the resource down so that only authenticated account sessions can query their own user profile data.

* **Concepts Used:** Route Protection, Current User State Retrieval, FastAPI Dependencies
* **File:** `5_Protect_Get_User.py`

### 6. Role-Based Access Guards (Admin Privilege)
Extended the database schemas by appending a user `role` column. Designed a `require_admin` dependency that blocks access to highly sensitive routes (such as `DELETE /users/{id}`) unless the authenticated user profile matches the Admin permission group.

* **Concepts Used:** RBAC (Role-Based Access Control), Guard Dependencies, `HTTP 403 Forbidden` Exception
* **File:** `6_require_admin_dependancy.py`

---

## Folder Structure 📂

```text
Week 2/
└── Day 4/
    ├── 1_Hash_&_Verify_Password_Using_Passlib.py
    ├── 2_Post_User_&_Hash_Password.py
    ├── 3_OAuth_Password_Request_Using_JWT.py
    ├── 4_Get_Current_User_Using_JWT.py
    ├── 5_Protect_Get_User.py
    ├── 6_require_admin_dependancy.py
    ├── app.db
    └── README.md