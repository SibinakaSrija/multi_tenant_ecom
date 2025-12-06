Multi-Tenant E-Commerce Django Project
Project Overview

This is a multi-tenant e-commerce backend built with Django and Django REST Framework (DRF).

Multiple vendors (tenants) can host their stores on a shared platform.

Each tenant manages their own products, orders, and customers independently.

The backend uses tenant middleware to ensure data isolation.

Project Setup

Clone the repository

git clone <your-github-repo-url>
cd multi_tenant_ecom


Create and activate a virtual environment

python -m venv venv
# Linux / Mac
source venv/bin/activate
# Windows
venv\Scripts\activate


Install dependencies

pip install -r requirements.txt


Apply migrations

python manage.py makemigrations
python manage.py migrate


Create a superuser

python manage.py createsuperuser


Run the development server

python manage.py runserver

Multi-Tenancy

Each vendor/store is a tenant.

Tenants are identified via X-Tenant-Domain HTTP header or subdomain.

Middleware (TenantMiddleware) sets request.tenant for all API views.

All product and order queries are filtered by tenant, ensuring data isolation.

Roles & Permissions
Role	Permissions
Owner	Full access to their store (products, orders)
Staff	Manage products and orders within their tenant
Customer	Can view and place orders; only sees their own orders
API Endpoints
Products API
Method	URL	Description	Permissions
GET	/products/	List all products (public)	Public
GET	/products/{id}/	Get product details	Public
POST	/products/	Create a product	Owner / Staff
PUT	/products/{id}/	Update a product	Owner / Staff
DELETE	/products/{id}/	Delete a product	Owner / Staff
Orders API
Method	URL	Description	Permissions
POST	/orders/place/	Place a new order (tenant-specific)	Authenticated
GET	/orders/	List orders: customers see only theirs, vendors see all	Authenticated
Tenant + User Role Flow
                   ┌───────────────────────────────┐
                   │       Incoming Request         │
                   │   (with X-Tenant-Domain header │
                   │       or subdomain)           │
                   └─────────────┬─────────────────┘
                                 │
                                 ▼
                   ┌───────────────────────────────┐
                   │      TenantMiddleware          │
                   │  request.tenant = Vendor       │
                   │   (if tenant exists)           │
                   └─────────────┬─────────────────┘
                                 │
        ┌────────────────────────┴────────────────────────┐
        ▼                                                 ▼
 ┌───────────────┐                               ┌────────────────┐
 │   Products API│                               │   Orders API   │
 └───────────────┘                               └────────────────┘
        │                                                 │
        ▼                                                 ▼
┌─────────────────────────┐                       ┌─────────────────────────┐
│GET /products/           │                       │POST /orders/place/      │
│GET /products/{id}/      │                       │GET /orders/             │
│Tenant filter applied    │                       │Tenant filter applied    │
│Permissions:             │                       │Permissions:             │
│  Public for list/detail │                       │  Authenticated users    │
│  Owner/Staff for create │                       │Role-based filtering:    │
│  update/delete          │                       │  Customer: own orders   │
│                         │                       │  Owner/Staff: all orders│
└─────────────────────────┘                       └─────────────────────────┘

GitHub Submission Instructions
# Initialize git (if not done already)
git init

# Add all files
git add .

# Commit changes
git commit -m "Final Day 3 submission"

# Add GitHub remote (replace URL)
git remote add origin https://github.com/yourusername/multi_tenant_ecom.git

# Rename branch to main
git branch -M main

# Push to GitHub
git push -u origin main


✅ After pushing, your project is submission-ready.

This README covers:

Project setup

Multi-tenancy explanation

Products & Orders API endpoints

Role-based permissions

Tenant + User Role flow diagram

GitHub submission instructions
