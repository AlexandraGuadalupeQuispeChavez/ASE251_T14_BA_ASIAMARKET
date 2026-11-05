-- Script de configuración de base de datos para AsiaMarket
USE master;
GO

-- Crear base de datos si no existe
IF NOT EXISTS (SELECT name FROM sys.databases WHERE name = 'asiamarket_analytics')
BEGIN
    CREATE DATABASE asiamarket_analytics;
END
GO

USE asiamarket_analytics;
GO

-- Crear tabla sales
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'sales')
BEGIN
    CREATE TABLE sales (
        sale_id INT PRIMARY KEY IDENTITY(1,1),
        sale_date DATE NOT NULL,
        product_name NVARCHAR(100),
        category NVARCHAR(50),
        customer_name NVARCHAR(100),
        quantity INT,
        unit_price DECIMAL(10,2),
        total_amount DECIMAL(10,2),
        payment_method NVARCHAR(50),
        region NVARCHAR(50),
        created_at DATETIME DEFAULT GETDATE()
    );
END
GO

-- Insertar datos de prueba
IF NOT EXISTS (SELECT * FROM sales)
BEGIN
    -- Datos de 2024
    INSERT INTO sales (sale_date, product_name, category, customer_name, quantity, unit_price, total_amount, payment_method, region)
    VALUES 
    ('2024-01-15', 'Laptop HP', 'Tecnología', 'Juan Pérez', 2, 2500.00, 5000.00, 'Tarjeta', 'Lima'),
    ('2024-01-20', 'Mouse Logitech', 'Tecnología', 'María García', 5, 45.00, 225.00, 'Efectivo', 'Lima'),
    ('2024-02-10', 'Teclado Mecánico', 'Tecnología', 'Carlos Ruiz', 3, 150.00, 450.00, 'Tarjeta', 'Arequipa'),
    ('2024-02-25', 'Monitor Samsung 27"', 'Tecnología', 'Ana Torres', 1, 800.00, 800.00, 'Transferencia', 'Lima'),
    ('2024-03-05', 'Auriculares Sony', 'Audio', 'Luis Mendoza', 4, 120.00, 480.00, 'Tarjeta', 'Cusco'),
    ('2024-03-18', 'Webcam Logitech', 'Tecnología', 'Rosa Flores', 2, 180.00, 360.00, 'Efectivo', 'Lima'),
    ('2024-04-12', 'Tablet Samsung', 'Tecnología', 'Pedro Castro', 1, 1200.00, 1200.00, 'Tarjeta', 'Trujillo'),
    ('2024-04-28', 'Impresora HP', 'Oficina', 'Julia Vega', 1, 650.00, 650.00, 'Transferencia', 'Lima'),
    ('2024-05-08', 'Router TP-Link', 'Redes', 'Miguel Ríos', 3, 95.00, 285.00, 'Efectivo', 'Lima'),
    ('2024-05-22', 'Disco Duro 1TB', 'Almacenamiento', 'Sandra López', 2, 220.00, 440.00, 'Tarjeta', 'Arequipa'),
    
    -- Datos de 2025
    ('2025-01-10', 'Laptop Dell', 'Tecnología', 'Roberto Salas', 1, 3200.00, 3200.00, 'Tarjeta', 'Lima'),
    ('2025-01-25', 'Mouse Inalámbrico', 'Tecnología', 'Carmen Díaz', 8, 35.00, 280.00, 'Efectivo', 'Lima'),
    ('2025-02-14', 'Teclado RGB', 'Tecnología', 'Fernando Soto', 2, 180.00, 360.00, 'Tarjeta', 'Cusco'),
    ('2025-02-28', 'Monitor LG 32"', 'Tecnología', 'Patricia Ramos', 1, 1100.00, 1100.00, 'Transferencia', 'Lima'),
    ('2025-03-12', 'Auriculares Gamer', 'Audio', 'Diego Paredes', 3, 250.00, 750.00, 'Tarjeta', 'Trujillo'),
    ('2025-03-30', 'Cámara Web 4K', 'Tecnología', 'Lucía Morales', 1, 420.00, 420.00, 'Efectivo', 'Lima'),
    ('2025-04-15', 'iPad Pro', 'Tecnología', 'Andrés Campos', 1, 4500.00, 4500.00, 'Tarjeta', 'Lima'),
    ('2025-04-29', 'Impresora Multifuncional', 'Oficina', 'Sofía Cruz', 1, 890.00, 890.00, 'Transferencia', 'Arequipa'),
    ('2025-05-10', 'Switch de Red', 'Redes', 'Raúl Herrera', 2, 145.00, 290.00, 'Efectivo', 'Lima'),
    ('2025-05-28', 'SSD 500GB', 'Almacenamiento', 'Mónica Vargas', 4, 280.00, 1120.00, 'Tarjeta', 'Cusco'),
    
    -- Datos de 2026
    ('2026-01-08', 'MacBook Pro', 'Tecnología', 'Gabriel Rojas', 1, 7500.00, 7500.00, 'Tarjeta', 'Lima'),
    ('2026-01-22', 'Mouse Gaming', 'Tecnología', 'Valeria Núñez', 6, 85.00, 510.00, 'Efectivo', 'Lima'),
    ('2026-02-05', 'Teclado Inalámbrico', 'Tecnología', 'Héctor Silva', 3, 125.00, 375.00, 'Tarjeta', 'Trujillo'),
    ('2026-02-18', 'Monitor Curvo 34"', 'Tecnología', 'Isabella Reyes', 1, 1850.00, 1850.00, 'Transferencia', 'Lima'),
    ('2026-03-08', 'Auriculares Bluetooth', 'Audio', 'Sebastián Ortiz', 5, 180.00, 900.00, 'Tarjeta', 'Arequipa'),
    ('2026-03-25', 'Webcam Pro', 'Tecnología', 'Daniela Medina', 2, 320.00, 640.00, 'Efectivo', 'Lima'),
    ('2026-04-10', 'Surface Pro', 'Tecnología', 'Nicolás Guzmán', 1, 5200.00, 5200.00, 'Tarjeta', 'Lima'),
    ('2026-04-24', 'Impresora Láser', 'Oficina', 'Camila Romero', 1, 1200.00, 1200.00, 'Transferencia', 'Cusco'),
    ('2026-05-15', 'Router Mesh', 'Redes', 'Emilio Figueroa', 1, 380.00, 380.00, 'Efectivo', 'Lima'),
    ('2026-05-30', 'Disco Duro Externo 2TB', 'Almacenamiento', 'Victoria Peña', 3, 350.00, 1050.00, 'Tarjeta', 'Trujillo'),
    
    -- Datos adicionales octubre 2026
    ('2026-10-05', 'Laptop Lenovo', 'Tecnología', 'Alejandro Paz', 2, 2800.00, 5600.00, 'Tarjeta', 'Lima'),
    ('2026-10-12', 'Mouse Pad RGB', 'Accesorios', 'Mariana Castro', 10, 25.00, 250.00, 'Efectivo', 'Lima'),
    ('2026-10-18', 'Teclado Compacto', 'Tecnología', 'Ricardo Villanueva', 4, 95.00, 380.00, 'Tarjeta', 'Arequipa'),
    ('2026-10-22', 'Monitor 4K', 'Tecnología', 'Elena Jiménez', 1, 2200.00, 2200.00, 'Transferencia', 'Lima'),
    ('2026-10-28', 'Auriculares Noise Cancelling', 'Audio', 'Francisco Luna', 2, 450.00, 900.00, 'Tarjeta', 'Cusco');
END
GO

-- Crear índices para mejorar el rendimiento
CREATE NONCLUSTERED INDEX IX_sales_sale_date ON sales(sale_date);
CREATE NONCLUSTERED INDEX IX_sales_category ON sales(category);
CREATE NONCLUSTERED INDEX IX_sales_region ON sales(region);
GO

-- Verificar datos insertados
SELECT 
    YEAR(sale_date) as Año,
    MONTH(sale_date) as Mes,
    COUNT(*) as Total_Ventas,
    SUM(total_amount) as Monto_Total
FROM sales
GROUP BY YEAR(sale_date), MONTH(sale_date)
ORDER BY Año, Mes;
GO

PRINT 'Base de datos configurada exitosamente!';
GO
