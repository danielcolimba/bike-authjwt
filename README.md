# Bike Auth Service

The **Bike Auth Service** is an authentication microservice for the cloud_project, responsible for managing user registration, login, and token-based authentication for bike-related applications.

## Technologies & Dependencies

- **JWT (jsonwebtoken)**: For token-based authentication
- **bcrypt**: For password hashing

## Setup Instructions

1. **Clone the repository**
    ```bash
    git clone <repository-url>
    cd bike-auth
    ```

2. **Install dependencies**
    ```bash
    npm install
    ```

3. **Configure environment variables**
    - Create a `.env` file in the root directory.
    - Add the following variables:
      ```
      JWT_SECRET=<your-jwt-secret>
      PORT=3000
      ```

4. **Start the service**
    ```bash
    npm start
    ```

The service will be available at `http://localhost:3001`.

## Usage

- Register a new user: `POST /register`
- Login: `POST /login`
- Protected routes require a valid JWT token in the `Authorization` header.
