# 🚀 FastAPI & Docker Starter Project

[![Python 3.13](https://img.shields.io/badge/Python-3.13-blue.svg)](https://www.python.org/downloads/release/python-3130/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115.0-green.svg)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)](https://www.docker.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![REST API](https://img.shields.io/badge/API-RESTful-orange.svg)](https://restfulapi.net/)

Whether you are building AI Agents or SPA websites, APIs are useful for getting data or acting as a channel to communicate with your AI Agent. I have not seen many examples showing header and data sanitization. Even though there are many agentic coding systems that 
can be used, I wanted a starter FASTAPI implementation that addressed the following topics:

- Sanitizing headers and data
- Handling validation erors gracefully
- Deploying the application within a container
- Reading environment variables
- Separation of domains via routers

I will remove the welcome and docs endpoints for production deployment.

## 📋 Table of Contents

- [💡 About The Project](#-about-the-project)
- [✨ Key Features](#-key-features)
- [💻 Technologies Used](#-technologies-used)
- [🛠️ Installation & Setup](#-installation--setup)
- [▶️ Running Locally](#-running-locally)
- [🧪 Testing](#-testing)
- [🔐 Security Features](#-security-features)
- [🚀 Deployment](#-deployment)
- [📊 API Documentation](#-api-documentation)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)

## 💡 About The Project

This project demonstrates APIs with FastAPI and the use of Docker for container builds.

**🎯 Problem Solved:** Modern web applications require robust APIs with proper security measures, data validation, and scalable architecture. This system provides a complete solution for blog and author management with production-ready features.

**🔑 Key Learning Outcomes:**
- **Advanced Data Validation** using Pydantic models with custom field validators
- **Security Implementation** with XSS protection, SQL injection prevention, and input sanitization
- **Docker Containerization** with multi-environment support (development/production)
- **RESTful API Design** following industry best practices
- **Configuration Management** using environment variables and Pydantic Settings

## ✨ Key Features

- **🔐 Advanced Security**: XSS protection, SQL injection prevention, input sanitization
- **📊 RESTful API**: Complete CRUD operations for blogs and authors
- **📝 Data Validation**: Pydantic models with custom validators and field constraints
- **🐳 Docker Ready**: Development and production configurations
- **📚 Auto Documentation**: Interactive API documentation with Swagger UI
- **⚙️ Environment Configuration**: Flexible settings management
- **🚀 Production Ready**: Gunicorn server configuration for deployment
- **🔍 Input Sanitization**: Bleach-powered HTML tag removal and content cleaning

## 💻 Technologies Used

### Backend Core
- **Python 3.13** - Latest Python version with performance improvements
- **FastAPI** - Modern, fast web framework for building APIs
- **Pydantic** - Data validation using Python type annotations
- **Pydantic Settings** - Environment-based configuration management

### Security & Data Processing
- **Bleach** - HTML sanitization for XSS protection
- **Regular Expressions** - Advanced input validation and cleaning

### Server & Deployment
- **Uvicorn** - ASGI server for development
- **Gunicorn** - WSGI HTTP server for production deployment
- **Docker** - Containerization platform
- **Docker Compose** - Multi-container application management

### Development Tools
- **Git** - Version control system
- **Environment Variables** - Secure configuration management

## 🛠️ Installation & Setup

### Prerequisites

- **Python 3.13+** (match your Dockerfile Python version)
- **Docker Desktop** (for Windows users) or **Docker Engine**
- **Git** for version control

⚠️ **Important**: Ensure your local Python version matches the Docker image version (Python 3.13.9) to avoid compatibility issues.

### Step-by-Step Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/fastapi-blog-system.git
cd fastapi-blog-system
```

2. **Create virtual environment** (optional but recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Environment Setup**
Create environment files for different deployments:

**.env.development**
```env
APP_NAME="FastAPI Blog Dev"
DEBUG=true
VERSION="1.0.0-dev"
DEFAULT_RATE_LIMIT="100/minute"
PROXY_IP="127.0.0.1"
```

**.env.production**
```env
APP_NAME="FastAPI Blog Production"
DEBUG=false
VERSION="1.0.0"
DEFAULT_RATE_LIMIT="1000/minute"
PROXY_IP="your-nginx-ip-here"
```

## ▶️ Running Locally

### Development Mode (with auto-reload)
```bash
# Windows/Linux/Mac
uvicorn main:app --reload --port=8000 --host=0.0.0.0
```

### Production Mode (Linux only)
```bash
gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app --bind 0.0.0.0:8000
```

### Docker Deployment

**Development Environment:**
```bash
docker compose -f docker-compose.dev.yaml up --build
```

**Production Environment:**
```bash
docker compose -f docker-compose.prod.yaml up --build
```

### Verify Installation

Once running, access these endpoints:
- **API Documentation**: http://localhost:8000/api/v1/docs
- **Health Check**: http://localhost:8000/api/v1/welcome
- **OpenAPI Schema**: http://localhost:8000/api/v1/openapi.json

## 🧪 Testing

### Run Tests
```bash
# Install testing dependencies (add to requirements.txt if needed)
pip install pytest pytest-asyncio httpx

# Run all tests
pytest

# Run with coverage
pytest --cov=.
```

### Manual API Testing
```bash
# Test welcome endpoint
curl http://localhost:8000/api/v1/welcome

# Test blog endpoints
curl http://localhost:8000/api/v1/blog/
curl http://localhost:8000/api/v1/blog/1

# Test author endpoints
curl http://localhost:8000/api/v1/author/
curl http://localhost:8000/api/v1/author/1
```

## 🔐 Security Features

### XSS Protection
- **HTML Sanitization**: All user inputs are processed through Bleach
- **Content Security**: Script tags and dangerous HTML elements are stripped
- **Field Validation**: Custom validators ensure data integrity

### SQL Injection Prevention
- **Input Cleaning**: Removal of SQL meta-characters (`;`, `'`, `"`, `` ` ``, `--`, `/*`, `*/`)
- **Parameterized Queries**: FastAPI's built-in protection mechanisms
- **Strict String Validation**: Special validation for sensitive fields

### Data Validation
- **Pydantic Models**: Type-safe data structures with automatic validation
- **Field Constraints**: Min/max length enforcement with truncation
- **Custom Validators**: Business logic validation at the model level

## 🚀 Deployment

### Docker Best Practices

1. **Version Matching**: Ensure your local Python version matches Dockerfile version
2. **Environment Variables**: Use appropriate `.env` files for each environment
3. **Port Configuration**: Default port 8000, configurable via environment

### Production Deployment Checklist

- [ ] Update `PROXY_IP` in production environment file
- [ ] Set `DEBUG=false` for production
- [ ] Use production Docker Compose file
- [ ] Configure proper rate limiting
- [ ] Set up reverse proxy (Nginx/Apache)
- [ ] Enable HTTPS/SSL certificates
- [ ] Configure monitoring and logging

## 📊 API Documentation

### Available Endpoints

**Blog Management:**
- `GET /api/v1/blog/` - List all blogs
- `GET /api/v1/blog/{blog_id}` - Get specific blog
- `POST /api/v1/blog/blog` - Create new blog

**Author Management:**
- `GET /api/v1/author/` - List all authors
- `GET /api/v1/author/{author_id}` - Get specific author
- `POST /api/v1/author/author` - Create new author

**System:**
- `GET /api/v1/welcome` - Health check and welcome message
- `GET /api/v1/docs` - Interactive API documentation
- `GET /api/v1/openapi.json` - OpenAPI schema

### Data Models

**BlogData Model:**
```json
{
  "title": "string (1-200 chars)",
  "description": "string (max 1000 chars, sanitized)",
  "content": "string (max 100000 chars, sanitized)",
  "tags": "string (1-100 chars)",
  "author": "string (1-100 chars)"
}
```

**AuthorData Model:**
```json
{
  "firstname": "string (1-20 chars)",
  "lastname": "string (1-20 chars)",
  "description": "string (max 1000 chars, sanitized)",
  "email": "string (max 100 chars)",
  "website": "string (max 100 chars)"
}
```

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Contribution Guidelines

- Follow PEP 8 style guidelines
- Add unit tests for new features
- Update documentation as needed
- Ensure all tests pass before submitting PR

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**⭐ Star this repository if you found it helpful!**

**🔧 Built with ❤️ using FastAPI and modern Python practices**