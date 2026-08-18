# PriorityPulse_Agent
Proyecto de agente de IA con el objetivo de llevar una agenda automática con orden de prioridades y urgencia.

# Descripcion del problema a tratar

Actualmente, los estudiantes universitarios y jóvenes profesionales con múltiples responsabilidades
tienen dificultad para consolidar y priorizar sus pendientes diarios porque la información sobre sus
compromisos llega de forma totalmente dispersa a través de correos electrónicos, aulas virtuales y
diversas notificaciones de aplicaciones móviles. Esto genera el olvido no intencionado de entregas
académicas, fechas de pago de recibos de servicios e impuestos, y citas importantes, derivando en
sanciones, recargos económicos, pérdida de asignaturas y un elevado nivel de estrés.

- Usuario principal: Estudiantes universitarios y
profesionales activos que gestionan múltiples
canales de comunicación digital y sufren de
sobrecarga informativa. *(Se evita "todo el
mundo")*.
- Objetivo del usuario: Mantener una lista única,
organizativa y priorizada automáticamente según
urgencia e importancia para cumplir con sus
obligaciones a tiempo.
- Entradas del usuario: Autorizaciones de acceso a
APIS de notificación/correo, preferencias
personales de priorización y confirmaciones o
reajustes manuales.
- Salidas esperadas del agente: Dashboard/lista
unificada organizada por prioridades (Alta, Media,
Baja), resúmenes claros de la tarea con fecha límite
y alertas preventivas.
Información necesaria: Texto/cuerpo de correos
entrantes, avisos de APPs (bancarias, académicas,
calendario), fechas límite explícitas, montos de
pago e historial de interacción.

# Decisiones, Límites y Control
- Decisiones que podría tomar: Clasificar nivel de
prioridad, agrupar notificaciones duplicadas sobre
un mismo evento y estimar fechas de vencimiento.
- Acciones permitidas: Leer notificaciones/correos
entrantes, estructurar la lista de alertas, sugerir
orden de ejecución y enviar recordatorios.
- Supervisión humana: El usuario valida las tareas
creadas, puede reordenar prioridades manualmente
y confirma cualquier acción externa.
