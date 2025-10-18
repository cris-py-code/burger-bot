# 🍔 Automatización de Pedidos - BurgerBot

> *Proyecto para automatizar pedidos, cobros y gestión de transacciones en una hamburguesería con menú reducido y alta rotación.*

---

## 📌 Descripción del Proyecto

Este proyecto tiene como objetivo **automatizar el proceso de toma de pedidos, cálculo de cobros, almacenamiento de transacciones y cálculo ágil de vuelto** en una hamburguesería que ofrece un menú limitado pero popular. La idea es reducir errores humanos, agilizar el servicio y mejorar la experiencia tanto del personal como del cliente.

El sistema será implementado mediante una **aplicación intuitiva** (web o móvil) que permita al personal o al cliente mismo realizar pedidos de forma rápida y precisa.

---

## Ejecutar el proyecto en consola
python -m src.cli.main


## 🍽️ Menú Disponible

Actualmente, el comercio ofrece **3 combos fijos y 1 postre**, con los siguientes precios en USD:

### 🔸 Combos

- **Combo Simple**  
  *Hamburguesa simple + Bebida + Fritas*  
  → **$5.00**

- **Combo Doble**  
  *Hamburguesa doble + Bebida + Fritas*  
  → **$6.00**

- **Combo Triple**  
  *Hamburguesa triple + Bebida + Fritas*  
  → **$7.00**

### 🍦 Postre

- **McFlurby**  
  *Helado de dulce de leche*  
  → **$2.00**

---

## 🎯 Objetivos del Sistema

1. **Automatizar pedidos**  
   Permitir selección rápida de combos y postres, con confirmación visual e inmediata.

2. **Calcular cobros automáticos**  
   Sumar el total del pedido según los ítems seleccionados, sin necesidad de cálculos manuales.

3. **Almacenar transacciones**  
   Registrar cada pedido con fecha, hora, ítems, total y monto recibido (para auditoría y estadísticas).

4. **Agilizar el vuelto**  
   Al ingresar el monto pagado por el cliente, el sistema debe calcular y mostrar el vuelto de forma instantánea.

5. **Interfaz simple y rápida**  
   Diseñada para uso en mostrador o self-service, ideal para entornos de alta rotación.

---

## 🧩 Funcionalidades Esperadas

- Selección de combos y postres mediante botones o touch.
- Visualización en tiempo real del total acumulado.
- Campo para ingresar monto recibido.
- Mostrar vuelto automáticamente.
- Botón de “Confirmar Pedido” que registra la transacción.
- Historial de pedidos del día (opcional: exportar o imprimir ticket).

---

## 💡 Notas Adicionales

- No se requiere personalización de ingredientes (menú fijo).
- No se manejan descuentos ni promociones por ahora.
- El sistema puede evolucionar para incluir delivery, estadísticas diarias o integración con caja registradora.

---

## 👥 Stakeholders

- **Dueño del local**: busca eficiencia, reducción de errores y registro de ventas.
- **Personal de mostrador**: necesita una interfaz rápida y sin complicaciones.
- **Clientes**: se benefician con tiempos de espera reducidos y precisión en cobros.

---

## 🚀 Próximos Pasos

- Definir plataforma (web, móvil, tablet, etc.).
- Diseñar interfaz de usuario (UI/UX).
- Definir formato de almacenamiento de transacciones (local, nube, CSV, base de datos, etc.).
- Validar con usuarios reales en entorno de prueba.

---
