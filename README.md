# Backend Analítico - AsiaMarket

Backend analítico desarrollado con Flask, MongoDB y SQL Server para el análisis de datos de ventas de AsiaMarket.

## ✅ Implementación de Filtros Dinámicos Completada

**Endpoint actualizado:** `GET /analytics/sales-total`

### Parámetros opcionales:
- `year` (int): Filtra ventas por año (1-9999)
- `month` (int): Filtra ventas por mes (1-12)

### Ejemplos de uso:
```
/analytics/sales-total                    → Total histórico
/analytics/sales-total?year=2026          → Total del año 2026
/analytics/sales-total?month=10           → Total de octubre (todos los años)
/analytics/sales-total?year=2026&month=10 → Total de octubre 2026
```

### Formato de respuesta:
```json
{
  "indicator": "sales_total",
  "title": "Ventas Totales",
  "chart_type": "card",
  "data": 2855530.0,
  "sources": ["SQL Server"]
}
```

## 📋 Tecnologías

- **Python 3.12+**
- **Flask** - Framework web
- **MongoDB Atlas** - Base de datos NoSQL
- **SQL Server** - Base de datos relacional
- **PyMongo** - Driver de MongoDB para Python
- **pyodbc** - Driver de SQL Server para Python
- **Flask-CORS** - Manejo de CORS
- **Python-dotenv** - Gestión de variables de entorno

## 🏗️ Arquitectura del Proyecto

El proyecto está organizado mediante **arquitectura por capas**:

```
ASE251_T14_BA_ASIAMARKET/
├── .venv/                          # Entorno virtual de Python
├── app/
│   ├── __pycache__/               # Cache de Python
│   ├── config/                    # Configuraciones del sistema
│   │   ├── __init__.py
│   │   └── settings.py
│   ├── database/                  # Gestión de conexiones a BD
│   │   ├── __init__.py
│   │   ├── mongodb.py            # Conexión a MongoDB
│   │   └── sqlserver.py          # Conexión a SQL Server (futuro)
│   ├── models/                    # Modelos de datos
│   │   ├── __init__.py
│   │   └── sales.py
│   ├── repositories/              # Capa de acceso a datos
│   │   ├── mongodb/
│   │   │   ├── __init__.py
│   │   │   └── sales_repository.py
│   │   ├── sqlserver/
│   │   │   ├── __init__.py
│   │   │   └── sales_repository.py
│   │   └── __init__.py
│   ├── routes/                    # Endpoints de la API
│   │   ├── __init__.py
│   │   ├── status.py
│   │   └── sales_analytics.py
│   ├── schemas/                   # Validación de datos
│   │   ├── __init__.py
│   │   └── sales_schema.py
│   ├── services/                  # Lógica de negocio
│   │   ├── analytics/
│   │   │   ├── __init__.py
│   │   │   └── sales_service.py
│   │   └── __init__.py
│   ├── static/                    # Archivos estáticos
│   ├── __init__.py
│   └── main.py                    # Punto de entrada
├── tests/                         # Pruebas unitarias
│   └── __init__.py
├── .env                           # Variables de entorno (NO SUBIR A GIT)
├── .gitignore                     # Archivos ignorados por Git
├── README.md                      # Este archivo
└── requirements.txt               # Dependencias del proyecto
```

## 📦 Responsabilidad de Cada Capa

- **Routes**: Recibe solicitudes HTTP y expone los endpoints de la API
- **Services**: Contiene la lógica del negocio, procesamiento de datos e indicadores
- **Repositories**: Gestiona consultas y operaciones con MongoDB
- **Models**: Define la estructura de los datos del sistema
- **Database**: Administra la conexión con MongoDB
- **Schemas**: Organiza y valida la estructura de los datos de entrada y salida
- **Static**: Almacenamiento de archivos de documentación y recursos auxiliares
- **Config**: Centraliza configuraciones y variables del sistema

## 🚀 Instalación y Configuración

### 1. Clonar el repositorio o descargar el proyecto

```bash
cd ASE251_T14_BA_ASIAMARKET
```

### 2. Crear y activar el entorno virtual

**Windows PowerShell:**
```powershell
python -m venv .venv
.venv\Scripts\activate
```

Cuando el entorno esté activo verás:
```
(.venv) PS C:\...\ASE251_T14_BA_ASIAMARKET>
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar variables de entorno

Crea un archivo `.env` en la raíz del proyecto:

```env
# SQL Server (REQUERIDO para filtros dinámicos)
SQL_SERVER=tu-servidor.database.windows.net
SQL_DATABASE=tu-base-de-datos
SQL_USERNAME=tu-usuario
SQL_PASSWORD=tu-password
SQL_DRIVER={ODBC Driver 17 for SQL Server}

# MongoDB (opcional)
MONGO_URI=mongodb+srv://usuario:password@cluster.mongodb.net/?appName=cluster-asiamarket
MONGO_DATABASE=asiamarket_analytics
```

### 5. Ejecutar el proyecto

```bash
python -m app.main
```

El servidor estará disponible en: `http://127.0.0.1:5000/`

### 6. Probar con Swagger UI

Abre: `http://127.0.0.1:5000/docs/`

## 🧪 Pruebas del Endpoint

### Casos exitosos (HTTP 200):
1. Sin filtros: `/analytics/sales-total`
2. Por año: `/analytics/sales-total?year=2026`
3. Por mes: `/analytics/sales-total?month=10`
4. Año y mes: `/analytics/sales-total?year=2026&month=10`

### Casos de validación (HTTP 400):
5. Mes inválido: `/analytics/sales-total?month=15`
6. Año inválido: `/analytics/sales-total?year=abc`
7. Ambos inválidos: `/analytics/sales-total?year=abc&month=15`

### 5. Configurar MongoDB Atlas

#### a) Crear proyecto en MongoDB Atlas

1. Ingresa a [MongoDB Atlas](https://www.mongodb.com/)
2. Crea un nuevo proyecto: `ASE251_T20_BA_ASIAMARKET`
3. Crea un cluster:
   - **Nombre**: `cluster-asiamarket`
   - **Provider**: AWS
   - **Región**: São Paulo (sa-east-1)
   - **Tier**: M0 (Free)

#### b) Configurar acceso

1. Copia el **username** y **password** que te proporciona MongoDB
2. Descarga el archivo `.env` que genera MongoDB
3. Copia la **URI de conexión**

#### c) Crear base de datos y colecciones

En MongoDB Atlas, crea:
- **Base de datos**: `asiamarket_analytics`
- **Colecciones**:
  - `sales`
  - `products`
  - `categories`
  - `customers`

#### d) Cargar datos de prueba

1. Descarga [MongoDB Compass](https://www.mongodb.com/products/tools/compass)
2. Conecta usando la URI de conexión
3. Importa los archivos JSON en cada colección:
   - `sales.json` → sales (700 registros)
   - `products.json` → products (80 registros)
   - `customers.json` → customers (500 registros)
   - `categories.json` → categories (12 registros)

### 6. Configurar variables de entorno

Edita el archivo `.env` en la raíz del proyecto con tus credenciales de MongoDB Atlas:

```env
# Ejemplo de configuración
MONGO_URI=mongodb+srv://angietechacona_db_user:TuPassword123@cluster-asiamarket.tfu9hvh.mongodb.net/?appName=cluster-asiamarket
MONGO_DATABASE=asiamarket_analytics
```

**IMPORTANTE**: 
- Reemplaza `angietechacona_db_user` con tu username de MongoDB
- Reemplaza `TuPassword123` con tu password de MongoDB
- Reemplaza `tfu9hvh` con el ID de tu cluster
- Asegúrate de copiar la URI completa sin comillas
- **NO subas el archivo `.env` a Git** (ya está en `.gitignore`)

## ▶️ Ejecutar el Proyecto

### Inicio Rápido (3 pasos):

```bash
# 1. Levantar SQL Server
docker-compose up -d

# 2. Esperar 30 segundos y configurar BD (ver INICIO_RAPIDO.md)

# 3. Ejecutar backend
python -m app.main
```

**Ver instrucciones completas en:** `INICIO_RAPIDO.md`

### Credenciales configuradas:

**SQL Server (Docker local):**
- Host: `localhost,1433`
- Database: `asiamarket_analytics`
- User: `sa`
- Password: `AsiaMarket2024!`

**MongoDB Atlas:**
- User: `alexandraquispe_db_user`
- Password: `q3GmLi9MvuDfcRGo`

El servidor se iniciará en: `http://127.0.0.1:5000/`

### Verificar que funciona

Abre tu navegador y visita: `http://127.0.0.1:5000/`

Deberías ver:
```json
{
  "estado": "Operativo",
  "servicio": "Backend Analítico",
  "mensaje": "API funcionando correctamente 🚀"
}
```

En la terminal deberías ver:
```
✅ CONEXIÓN EXITOSA CON MONGODB
Base de datos: asiamarket_analytics
Colecciones disponibles:
 - customers
 - sales
 - categories
 - products
```

## 🧪 Verificar Instalación

```bash
# Ver paquetes instalados
pip list

# Verificar estructura
tree /F  # Windows CMD
```

## 📝 Próximos Pasos

1. ✅ Estructura del proyecto creada
2. ✅ Entorno virtual configurado
3. ✅ Dependencias instaladas
4. ✅ Conexión a MongoDB establecida
5. ✅ Datos de prueba cargados
6. 🔄 Implementar repositorios
7. 🔄 Implementar servicios
8. 🔄 Crear endpoints analíticos
9. 🔄 Documentar API con Swagger

## 🔒 Seguridad

- **NUNCA** subas el archivo `.env` a Git
- Mantén tus credenciales de MongoDB seguras
- Usa variables de entorno para datos sensibles

## 👥 Equipo

**Proyecto**: ASE251_T14_BA_ASIAMARKET  
**Sistema**: Backend Analítico para AsiaMarket

---

**Nota**: Este README será actualizado conforme avance el desarrollo del proyecto.
