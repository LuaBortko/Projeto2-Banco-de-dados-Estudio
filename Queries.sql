--Listar todos os filmes com nome, gênero e ano de lançamento.
--Mostrar todos os atores que participaram de um determinado filme.
--Contar quantos filmes cada ator participou.
--Listar todos os filmes dirigidos por um diretor específico.
--Mostrar os filmes com duração superior a determinado tempo.
--Contar a quantidade de filmes por gênero.
--Mostrar os roteiristas que escreveram mais de um filme.
--Apresentar a quantidade de filmes lançados por ano.
--Listar os atores do sexo feminino com menos de 30 anos.
--Listar todos os filmes de um determinado gênero lançados em um intervalo de anos.
SELECT f.nome AS filme
FROM filme f
WHERE cast(f.ano_lancamento as int) <= 2020 AND cast(f.ano_lancamento as int) >= 2010 and f.genero = 'Documentário'
