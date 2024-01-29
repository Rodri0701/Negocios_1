create database Modelo;
use Modelo;
create table Category( 
id int auto_increment primary key,
nombre varchar (45) 
);

create table Product(
id_product int auto_increment primary key,
model varchar(45),
category_id int,
foreign key (category_id) references Category (id)
);


