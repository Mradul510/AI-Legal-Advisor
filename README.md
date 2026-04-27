# ⚖️ LAwBOTie – AI Legal Advisor

> An AI-powered legal advisory platform combining a **Next.js** frontend, a **Spring Boot** REST API, and a **Python NLP** service to provide intelligent legal assistance.

---

## 📁 Project Structure

```
LAwBOTie/
├── AI-Legal-Advisor/          # Next.js 14 frontend (TypeScript)
├── ai-legal-advisor-backend/  # Spring Boot 4 REST API (Java 21)
│   └── ai-legal-advisor-backend/
│       └── src/main/resources/
│           ├── application.properties          ← 🚫 NOT committed (secrets)
│           └── application.properties.example  ← ✅ Use this as a template
└── ai-service/                # Python FastAPI NLP service
```

---

## 🚀 Getting Started

### Prerequisites

| Tool | Version |
|------|---------|
| Node.js | 18+ |
| Java (JDK) | 21 |
| Maven | 3.9+ |
| MySQL | 8+ |
| Python | 3.10+ |

---

### 1️⃣ Clone the repository

```bash
git clone https://github.com/<your-username>/LAwBOTie.git
cd LAwBOTie
```

---

### 2️⃣ Configure environment variables

#### 🗄️ Backend (Spring Boot)

```bash
cd ai-legal-advisor-backend/ai-legal-advisor-backend/src/main/resources

# Copy the example template
copy application.properties.example application.properties
```

Open `application.properties` and set your values (or export them as environment variables):

| Variable | Description | Example |
|---|---|---|
| `DB_URL` | MySQL JDBC connection string | `jdbc:mysql://localhost:3306/lawy_bot` |
| `DB_USERNAME` | MySQL username | `root` |
| `DB_PASSWORD` | MySQL password | `your_password` |
| `JWT_SECRET` | Random secret key (≥32 chars) | `generate-a-strong-random-key` |
| `JWT_EXPIRATION` | Token TTL in milliseconds | `86400000` (24 h) |
| `AI_SERVICE_URL` | URL of the Python AI service | `http://localhost:8000` |
| `PORT` | Server port | `8080` |

> **Security tip:** On Linux/Mac export variables in your shell; on Windows use System Properties → Environment Variables.

#### 🌐 Frontend (Next.js)

```bash
cd AI-Legal-Advisor

# Copy the example template
copy .env.example .env.local
```

| Variable | Description | Default |
|---|---|---|
| `NEXT_PUBLIC_API_URL` | Spring Boot API base URL | `http://localhost:8080` |

---

### 3️⃣ Set up the MySQL database

```sql
CREATE DATABASE lawy_bot CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

Spring Boot will auto-create tables on first run (`spring.jpa.hibernate.ddl-auto=update`).

---

### 4️⃣ Run the services

#### 🐍 Python AI Service

```bash
cd ai-service
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Mac / Linux

pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

#### ☕ Spring Boot Backend

```bash
cd ai-legal-advisor-backend/ai-legal-advisor-backend
./mvnw spring-boot:run       # Mac / Linux
mvnw.cmd spring-boot:run     # Windows
```

The API will be available at **http://localhost:8080**

#### ⚛️ Next.js Frontend

```bash
cd AI-Legal-Advisor
npm install          # or: pnpm install
npm run dev
```

Open **http://localhost:3000** in your browser.

---

## 🔐 Security

- **Database credentials**, **JWT secret**, and **API keys** are never stored in the repository.
- All secrets are loaded from environment variables at runtime using Spring Boot's `${ENV_VAR:default}` syntax.
- The `application.properties` file is listed in `.gitignore`; use `application.properties.example` as a reference.
- Frontend secrets live in `.env.local` (also git-ignored); use `.env.example` as a reference.

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | Next.js 14, TypeScript, Tailwind CSS |
| Backend | Spring Boot 4, Java 21, Spring Security, JWT |
| Database | MySQL 8, Spring Data JPA / Hibernate |
| AI Service | Python, FastAPI, custom NLP engine |
| Auth | JWT (JSON Web Tokens) |

---

## 📜 API Endpoints

> Base URL: `http://localhost:8080`

| Method | Path | Description |
|--------|------|-------------|
| POST | `/api/auth/register` | Register a new user |
| POST | `/api/auth/login` | Login and receive JWT |
| POST | `/api/chat` | Send a legal query to the AI |
| GET | `/api/chat/history` | Get conversation history |

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/my-feature`
3. Copy the config templates (`.env.example`, `application.properties.example`) and fill in your local values
4. Commit your changes: `git commit -m "feat: add my feature"`
5. Push and open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** – see [LICENSE](LICENSE) for details.

---

<p align="center">Built with ❤️ for accessible legal assistance</p>
