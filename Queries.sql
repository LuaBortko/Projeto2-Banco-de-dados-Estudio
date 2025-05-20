--Listar todos os filmes com nome, gênero e ano de lançamento.
SELECT nome, genero, ano_lancamento
FROM filme
--Mostrar todos os atores que participaram de um determinado filme.
--Contar quantos filmes cada ator participou.
--Listar todos os filmes dirigidos por um diretor específico.
--Mostrar os filmes com duração superior a determinado tempo.
SELECT f.nome AS filme
FROM filme f
WHERE cast(f.tempo as int) >= 200
--Contar a quantidade de filmes por gênero.
--Mostrar os roteiristas que escreveram mais de um filme.
SELECT r.id AS id_roteirista, r.nome AS nome, count(f.id_roteirista) AS qtde_filmes
FROM roteirista r 
INNER JOIN filme f
  ON f.id_roteirista = r.id
GROUP BY r.id
HAVING count(id_roteirista) > 1
--Apresentar a quantidade de filmes lançados por ano.
--Listar os atores do sexo feminino com menos de 30 anos.
SELECT nome, sexo, idade
FROM ator
WHERE sexo = 'feminino' AND cast(idade as int) < 30 
--Listar todos os filmes de um determinado gênero lançados em um intervalo de anos.
SELECT f.nome AS filme
FROM filme f
WHERE cast(f.ano_lancamento as int) <= 2020 AND cast(f.ano_lancamento as int) >= 2010 and f.genero = 'Documentário'
