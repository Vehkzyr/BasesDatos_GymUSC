# BASE DE DATOS GYM USC

La USC, debido al incremento de usuarios en la actividad de acondicionamiento físico en sala, quiere renovar su base de datos. El objetivo será hacer, en python una interfaz gráfica o página web en la cual puedas acceder, y actualizar con los permisos necesarios la base de datos del gimnasio.

## En el gimnasio tenemos lo siguiente: 

Usuarios: vamos a tener usuarios que reservan hora en el gimnasio. Se diferencian entre sí por un código asociado tanto a su DNI como al correo de la USC, a un nombre (nombre y apellidos), número de reservas activas así como el número de reservas totales y el estado de su cuota (bool pagado). También se podrá ver que dia y a que hora tiene reservado. Es usuario todo aquel que lleve al día su cuota mensual o anual.

Personal: el personal se divide en tres grupos: Administración, Limpieza y Monitores. Todos están diferenciados entre sí por su código de trabajador de la USC, un correo de trabajo, DNI, nombre y apellidos, su horario de trabajo y el tiempo trabajado en la USC. En el caso de la administración tendrán que tener recogido su puesto de trabajo y en el caso de los monitores tendrá que recogerse de que actividad son monitores (pueden ser de varias actividades).

Reservas: La tabla de reservas tendría como atributos los datos del usuario que realiza la reserva, como su código de usuario (asociado al DNI y correo de la USC), nombre completo, número de reservas activas y totales, estado de la cuota, así como la fecha y hora de la reserva. Además, también se podría incluir información adicional en la tabla de reservas, como el nombre de la actividad que se reserva, el tipo de reserva (por ejemplo, reserva de una sesión de entrenamiento personal o de una clase grupal), y cualquier otra información relevante para la gestión de las reservas en el gimnasio.

Actividades: : Esta tabla contendría información detallada sobre las diferentes actividades ofrecidas en el gimnasio, como el nombre de la actividad, una descripción breve, el tipo de actividad (por ejemplo, entrenamiento en grupo, entrenamiento personal, yoga, pilates, etc.), el horario de las sesiones, la duración de cada sesión, y cualquier otro detalle relevante.

Pagos: Esta tabla contendría información sobre los pagos realizados por los usuarios, como la fecha del pago, el monto abonado, el número de factura, y cualquier otro detalle relevante.

Instalaciones: Esta tabla contiene la lista de instalaciones contenidas en el gimnasio, con un codigo, un nombre y un horario de apertura, asi como un numero de plazas totales y reservadas
