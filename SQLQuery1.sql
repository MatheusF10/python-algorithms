create table Produtos(
ID_Produto Int Primary Key identity Not Null,
Nome_produto varchar(50) Not Null, 
Quantidade_estoque Int Not Null,
Valor_Compra Decimal (6,2) Not Null,
Valor_venda Decimal (6,2) Not Null,
)