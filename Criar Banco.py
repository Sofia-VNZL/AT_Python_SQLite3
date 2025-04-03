.open mercado-at.db
.mode table

drop table if exists clientes;
drop table if exists produto;
drop table if exists compra; 
drop table if exists item; 

CREATE TABLE cliente (
  id_cliente integrer primary key autoincrement,
  nome char(50) not null,
)

CREATE TABLE produto (
  id_produto integrer primary key autoincrement,
  nome char(50) not null,
  quantidade int not null,
  preco real not null
);

CREATE TABLE compra(
  id_compra integrer primary key autoincrement,
  data_compra chat(30) not null,
  id_cliente int not null,
  foreign key (id_cliente) references cliente(id_cliente)
);

CREATE TABLE item (
  id_item integrer primary key autoincrement,
  quantidade int not null,
  id_compra int not null,
  id_produto int not null,
  foreign key (id_compra) references compra(id_compra),
  foreign key (id_produto) references produto(id_produto)
)
