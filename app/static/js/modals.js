// Función para abrir el modal con la imagen seleccionada
function openModal(imageUrl, productName) {
    const modal = document.getElementById("imageModal");
    const modalImg = document.getElementById("modalImage");
    const modalProductName = document.getElementById("modalProductName");

    modalImg.src = imageUrl;
    modalProductName.textContent = productName;

    modal.style.display = "block";
}

function closeModal() {
    const modal = document.getElementById("imageModal");
    modal.style.display = "none";
}
// Función para abrir el modal con la imagen seleccionada


// ---------


// funcion paera abrir el modal de confirmación de eliminación de producto

function openDeleteModal(productId) {
    const modal = document.getElementById("deleteModal");
    const deleteForm = document.getElementById("deleteForm");

    deleteForm.action = "/producto/delete/" + productId;    
    
    modal.style.display = "block";
}

function closeDeleteModal() {
    const modal = document.getElementById("deleteModal");
    modal.style.display = "none";
}
// funcion paera abrir el modal de confirmación de eliminación de producto


// ---------


// funcion paera abrir el modal de confirmación de eliminación de categoria
{function openDeleteModalCategoria(categoriaId) {

    const modal = document.getElementById("deleteModalCategoria");
    const deleteFormCategoria = document.getElementById("deleteFormCategoria");

    deleteFormCategoria.action = "/categoria/delete/" + categoriaId;    
    
    modal.style.display = "block";
}

function closeDeleteModalCategoria() {
    const modal = document.getElementById("deleteModalCategoria");
    modal.style.display = "none";
}}
// funcion paera abrir el modal de confirmación de eliminación de categoria


// ---------


// funcion paera abrir el modal de editar de producto
function openEditModal(productoId, nombre, precio, cantidad, categoria_id, imagen) {
    
    const modal = document.getElementById("editModalProducto");
    const editForm = document.getElementById("editFormProducto");

    document.getElementById("edit_nombre").value = nombre;
    document.getElementById("edit_precio").value = precio;
    document.getElementById("edit_cantidad").value = cantidad;
    document.getElementById("edit_categoria_id").value = categoria_id;
    
    if (imagen) {
        document.getElementById("imagen_actual").src = "/static/images/" + imagen;
        document.getElementById("imagen_actual").style.display = "block";
    } else {
        document.getElementById("imagen_actual").style.display = "none";
    }

    editForm.action = "/producto/edit/" + productoId;

    modal.style.display = "block";
}

function closeEditModalProducto() {
    const modal = document.getElementById("editModalProducto");
    modal.style.display = "none";
}
// funcion paera abrir el modal de editar de producto


// ---------


// funcion paera abrir el modal de editar de categoria
function openEditModalCategoria(categoriaId, nombre, imagen) {
    
    const modal = document.getElementById("editModalCategoria");
    const editForm = document.getElementById("editFormCategoria");

    document.getElementById("edit_categoria_nombre").value = nombre;

    if (imagen) {
        document.getElementById("imagen_actual").src = "/static/images/" + imagen;
        document.getElementById("imagen_actual").style.display = "block";
    } else {
        document.getElementById("imagen_actual").style.display = "none";
    }

    editForm.action = "/categoria/edit/" + categoriaId;

    modal.style.display = "block";
}

function closeEditModalCategoria() {
    const modal = document.getElementById("editModalCategoria");
    modal.style.display = "none";
}
// funcion paera abrir el modal de editar de categoria


// ---------


// funcion paera abrir el modal de mostrar productos asociados
function openCategoryProductsModal(categoriaId) {
    fetch('/categoria/productos/' + categoriaId)
        .then(response => response.json())
        .then(data => {
            const tableBody = document.querySelector('#productosTable tbody');
            tableBody.innerHTML = '';  

            if (data.length === 0) {
                tableBody.innerHTML = '<tr><td colspan="4">No hay productos asociados a esta categoría.</td></tr>';
            } else {

                data.forEach(producto => {
                    const row = document.createElement('tr');
                    row.innerHTML = `
                        <td>${producto.nombre}</td>
                        <td>$${producto.precio.toFixed(3)}</td>
                        <td>${producto.cantidad}</td>
                        <td>
                            <button class="btn-1" onclick="openModal('/static/images/${producto.imagen}', '{{ producto.nombre }}')" >Imagen</button>
                        </td>
                    `;
                    tableBody.appendChild(row);
                });
            }

            const modal = document.getElementById('categoryProductsModal');
            modal.style.display = 'block';
        })
        .catch(error => console.error('Error al obtener los productos:', error));
}

function closeCategoryProductsModal() {
    const modal = document.getElementById('categoryProductsModal');
    modal.style.display = 'none';
}
// funcion paera abrir el modal de mostrar productos asociados



// ---------



// funcion paera abrir el modal de editar direccion del cliente
function openEditModalDireccion(direccionId, departamento, municipio, calle, informacionAdicional, barrio, destinatario) {
    const modal = document.getElementById("editModalDireccion");
    const editForm = document.getElementById("editFormDireccion");

    document.getElementById("edit_departamento").value = departamento;
    document.getElementById("edit_municipio").value = municipio;
    document.getElementById("edit_calle").value = calle;
    document.getElementById("edit_informacion_adicional").value = informacionAdicional;
    document.getElementById("edit_barrio").value = barrio;
    document.getElementById("edit_destinatario").value = destinatario;

    editForm.action = "/direccion_cliente/edit/" + direccionId;

    modal.style.display = "block";
}

function closeEditModalDireccion() {
    const modal = document.getElementById("editModalDireccion");
    modal.style.display = "none";
}
// funcion paera abrir el modal de editar direccion del cliente



// ---------



// funcion paera abrir el modal de editar el metodo de pago
function openEditModalPago(id, tipo, numero_tarjeta, nombre_tarjeta, fecha_vencimiento, codigo_seguridad) {
    const modal = document.getElementById("editModalPago");
    const editForm = document.getElementById("editFormPago");

    document.getElementById("edit_tipo").value = tipo;
    document.getElementById("edit_numero_tarjeta").value = numero_tarjeta;
    document.getElementById("edit_nombre_tarjeta").value = nombre_tarjeta;
    document.getElementById("edit_fecha_vencimiento").value = fecha_vencimiento;
    document.getElementById("edit_codigo_seguridad").value = codigo_seguridad;

    editForm.action = "/metodo_pago/edit/" + id;

    modal.style.display = "block";
}

function closeEditModalPago() {
    const modal = document.getElementById("editModalPago");
    modal.style.display = "none";
}
// funcion paera abrir el modal de editar el metodo de pago
