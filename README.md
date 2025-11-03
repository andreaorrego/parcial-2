GESTIÓN DE PRODUCTOS - PROYECTO PYTHON

Este proyecto corresponde al desarrollo de un sistema de gestión de productos, clientes y facturas en Python. Consiste en una aplicación de línea de comandos que permite registrar y 
consultar productos, generar facturas y asociarlas a clientes, con el fin de facilitar el manejo de inventario y procesos de facturación de manera sencilla y práctica.

FUNCIONALIDADES

- Registro de productos con propiedades como: nombre, dosis y concentración.
- Registro de clientes con información personal (nombre, cédula).
- Creación de facturas asociadas a clientes y productos, con cálculo de cantidades y totales.
- Visualización de las facturas generadas.
- Posibilidad de realizar pruebas unitarias para validar el correcto funcionamiento del sistema.

ARQUITECTURA DEL PROYECTO

El sistema se desarrolló bajo un enfoque modular: 

- Model/cliente.py → Definición de la clase Cliente y sus métodos.
- Model/producto.py → Definición de la clase Producto y sus atributos.
- Model/factura.py → Definición de la clase Factura y métodos para agregar productos y mostrar facturas.
- Model/antibiotico.py → Definición de la clase Antibiótico y sus atributos.
- tests/ → Pruebas unitarias para validar las funcionalidades.

EJECUCIÓN

Clona este repositorio: https://github.com/andreaorrego/parcial-2.git


EVIDENCIAS

- Registro de productos y clientes a través de la consola.
- Generación de facturas con detalle de productos y cantidades.
- Resultados validados mediante pruebas unitarias.
- Repositorio con control de versiones y trazabilidad en GitHub.

CONCLUSIONES

- Se cumplieron los requerimientos funcionales y de arquitectura del sistema.
- La modularización facilita la comprensión y mantenimiento del código.
- El proyecto refuerza conceptos de programación orientada a objetos en Python.
- Se generó una herramienta práctica para la gestión de inventario y facturación en entornos educativos o de pequeña escala.
