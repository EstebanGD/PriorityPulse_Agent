# API Contract — PriorityPulse

## 1. Descripción

Este documento define el contrato de comunicación entre el workflow de
PriorityPulse y el agente encargado de analizar los mensajes recibidos.

El contrato establece:

- La estructura de la solicitud enviada al agente.
- La estructura de la respuesta generada por el agente.
- Los campos obligatorios y sus tipos.
- Los valores permitidos para determinados campos.

En esta primera versión se utiliza un mock para simular la respuesta del
agente de IA.

---

## 2. Request — `agent_request.json`

### Descripción

El request contiene la información necesaria para que el agente analice
un mensaje y determine si contiene un compromiso, tarea, entrega, pago,
cita u otra actividad relevante.

### Estructura

```json
{
  "source": "gmail",
  "sender": "profesor@universidad.edu",
  "subject": "Entrega informe de Ingeniería de Software",
  "message": "Hola Pepito, recuerda que el informe de Ingeniería de Software debe entregarse el viernes antes de las 11:59 PM."
}