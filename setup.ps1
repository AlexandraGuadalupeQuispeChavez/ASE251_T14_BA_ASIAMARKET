# Script de configuración automatizada para AsiaMarket Backend
# Ejecutar con: .\setup.ps1

Write-Host "======================================" -ForegroundColor Cyan
Write-Host "CONFIGURACIÓN ASIAMARKET BACKEND" -ForegroundColor Cyan
Write-Host "======================================" -ForegroundColor Cyan
Write-Host ""

# Paso 1: Verificar Docker
Write-Host "[1/5] Verificando Docker..." -ForegroundColor Yellow
if (Get-Command docker -ErrorAction SilentlyContinue) {
    Write-Host "✅ Docker instalado" -ForegroundColor Green
} else {
    Write-Host "❌ Docker no encontrado. Instala Docker Desktop desde: https://www.docker.com/products/docker-desktop" -ForegroundColor Red
    exit 1
}

# Paso 2: Levantar SQL Server
Write-Host ""
Write-Host "[2/5] Iniciando SQL Server (Docker)..." -ForegroundColor Yellow
docker-compose up -d

Write-Host "⏳ Esperando 35 segundos para que SQL Server inicie..." -ForegroundColor Yellow
Start-Sleep -Seconds 35

# Verificar que el contenedor está corriendo
$container = docker ps --filter "name=asiamarket_sqlserver" --format "{{.Names}}"
if ($container -eq "asiamarket_sqlserver") {
    Write-Host "✅ SQL Server corriendo" -ForegroundColor Green
} else {
    Write-Host "❌ Error: SQL Server no está corriendo" -ForegroundColor Red
    Write-Host "Intenta manualmente: docker-compose up -d" -ForegroundColor Yellow
    exit 1
}

# Paso 3: Configurar base de datos
Write-Host ""
Write-Host "[3/5] Configurando base de datos..." -ForegroundColor Yellow

# Copiar script SQL al contenedor
docker cp setup_database.sql asiamarket_sqlserver:/setup_database.sql

# Ejecutar script
docker exec asiamarket_sqlserver /opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P "AsiaMarket2024!" -i /setup_database.sql

if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ Base de datos configurada" -ForegroundColor Green
} else {
    Write-Host "⚠️  Revisa los logs: docker logs asiamarket_sqlserver" -ForegroundColor Yellow
}

# Paso 4: Instalar dependencias Python
Write-Host ""
Write-Host "[4/5] Instalando dependencias Python..." -ForegroundColor Yellow
pip install -r requirements.txt

if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ Dependencias instaladas" -ForegroundColor Green
} else {
    Write-Host "❌ Error instalando dependencias" -ForegroundColor Red
    exit 1
}

# Paso 5: Resumen
Write-Host ""
Write-Host "======================================" -ForegroundColor Cyan
Write-Host "✅ CONFIGURACIÓN COMPLETA" -ForegroundColor Green
Write-Host "======================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "📋 CREDENCIALES SQL SERVER:" -ForegroundColor Yellow
Write-Host "   Host: localhost,1433"
Write-Host "   Database: asiamarket_analytics"
Write-Host "   User: sa"
Write-Host "   Password: AsiaMarket2024!"
Write-Host ""
Write-Host "🚀 SIGUIENTE PASO:" -ForegroundColor Yellow
Write-Host "   python -m app.main"
Write-Host ""
Write-Host "📖 Swagger UI:" -ForegroundColor Yellow
Write-Host "   http://127.0.0.1:5000/docs/"
Write-Host ""
Write-Host "🧪 PRUEBAS RÁPIDAS:" -ForegroundColor Yellow
Write-Host "   /analytics/sales-total"
Write-Host "   /analytics/sales-total?year=2026"
Write-Host "   /analytics/sales-total?month=10"
Write-Host "   /analytics/sales-total?year=2026&month=10"
Write-Host ""
