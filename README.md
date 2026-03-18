# Decentralized Voting System on Ethereum

## Overview
The Decentralized Voting System on Ethereum is a cutting-edge application designed to revolutionize the electoral process by leveraging blockchain technology. This system addresses the critical need for transparent, secure, and tamper-proof voting mechanisms, ensuring that each vote is recorded immutably on the Ethereum blockchain. The application is ideal for governments, organizations, and communities aiming to enhance the integrity and trustworthiness of their elections. With its user-friendly interface, the system caters to voters, administrators, and candidates, making it accessible and easy to use for all stakeholders involved.

## Features
- **User Authentication**: Provides a secure login system for both voters and administrators, ensuring that only authorized users can access the system.
- **Candidate Management**: An admin interface that allows for the management of candidate details and election parameters, streamlining the setup of elections.
- **Voting Interface**: An intuitive voting page where users can cast their votes securely and confidently.
- **Real-time Results**: A dynamic results page that displays live vote counts and election outcomes, offering transparency throughout the voting process.
- **Blockchain Integration**: Utilizes the Ethereum blockchain to securely and immutably record votes, preventing any form of tampering or fraud.
- **Responsive Design**: A mobile-friendly interface that ensures easy access and usability across various devices.
- **Data Security**: Implements secure password hashing and token-based authentication to protect user data and maintain privacy.

## Tech Stack
| Component    | Technology  |
|--------------|-------------|
| Backend      | FastAPI     |
| Frontend     | HTML, CSS, JavaScript |
| Database     | SQLite      |
| Blockchain   | Ethereum    |
| Server       | Uvicorn     |
| ORM          | SQLAlchemy  |

## Architecture
The Decentralized Voting System is built on a client-server architecture. The FastAPI backend serves HTML templates to the frontend and handles API requests. The database models define the structure for users, candidates, and votes, with data flow managed through SQLAlchemy ORM. API endpoints facilitate seamless interactions between the client and server, ensuring a smooth voting experience.

```
+-----------------+
|   Frontend UI   |
| (HTML/CSS/JS)   |
+--------+--------+
         |
         v
+-----------------+
|     FastAPI     |
|   (Backend)     |
+--------+--------+
         |
         v
+-----------------+
|    SQLite DB    |
|   (Data Store)  |
+-----------------+
```

## Getting Started

### Prerequisites
- Python 3.11+
- pip (Python package manager)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/decentralized-voting-system-on-ethereum.git
   cd decentralized-voting-system-on-ethereum
   ```
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application
1. Start the FastAPI server:
   ```bash
   uvicorn app:app --reload
   ```
2. Open your browser and visit:
   ```
   http://localhost:8000
   ```

## API Endpoints
| Method | Path             | Description                        |
|--------|------------------|------------------------------------|
| GET    | `/`              | Home page                          |
| GET    | `/vote`          | Voting page                        |
| GET    | `/results`       | Election results page              |
| GET    | `/login`         | Login page                         |
| GET    | `/admin`         | Admin dashboard                    |
| GET    | `/api/candidates`| Fetch list of candidates           |
| POST   | `/api/vote`      | Cast a vote                        |
| GET    | `/api/results`   | Get voting results                 |
| POST   | `/api/login`     | User login                         |

## Project Structure
```
.
├── Dockerfile                  # Docker configuration file
├── app.py                      # Main application file
├── requirements.txt            # Python dependencies
├── start.sh                    # Shell script to start the app
├── static
│   ├── css
│   │   └── style.css           # Stylesheet for the application
│   └── js
│       └── main.js             # JavaScript for frontend interactions
└── templates
    ├── admin.html              # Admin dashboard template
    ├── index.html              # Home page template
    ├── login.html              # Login page template
    ├── results.html            # Results page template
    └── vote.html               # Voting page template
```

## Screenshots
*Screenshots of the application interface will be added here.*

## Docker Deployment
1. Build the Docker image:
   ```bash
   docker build -t voting-system .
   ```
2. Run the Docker container:
   ```bash
   docker run -d -p 8000:8000 voting-system
   ```

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Open a Pull Request

## License
This project is licensed under the MIT License.

---
Built with Python and FastAPI.
