use Modelo; -- Se usa la base de datos llamada modelo
insert into Category (nombre) values ("Tecnología"); -- Se inserta el primer registro en la tabla

-- Se inserta un registro en la otra tabla

insert into Product (model, category_id) values ("HP intel core i5", 1);

SELECT Product.id_product, Product.model, Category.nombre from  Product as Product join Category as Category on Product.category_id = Category.id;