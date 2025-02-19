Students Management System
Requirements
Core Functionalities
● Student Management: Create and retrieve students
● Course Management: Create and retrieve courses
● Enrollment Management: Enroll students in courses and fetch enrolled courses for a student
Technical Requirements
a) API Development
● Use FastAPI for backend development.
● Implement proper request validation using Pydantic models.
● Use async endpoints where applicable.
● Return appropriate HTTP status codes for different responses.
b) Database Integration
● Use PostgreSQL (or SQLite for simplicity).
● Implement ORM using SQLAlchemy with async support.
● Use Alembic for database migrations.
c) Authentication & Authorization
● Implement JWT-based authentication.
● Require authentication for modifying data (Create, Update, Delete).
● Allow only authenticated users to access student and course details.
d) Error Handling & Logging
● Implement custom error handling for validation and business logic errors.
● Log API requests and responses using Python logging.
e) Testing
● Write unit tests using pytest.
● Use TestClient from FastAPI for testing API endpoints.
● Implement database testing with an in-memory SQLite instance.
f) Documentation & API Testing
● Utilize FastAPI's built-in Swagger UI and ReDoc for API documentation.
● Ensure that API documentation is accessible at /docs.
