# Site pessoal
Site pessoal com os principais pesquisas, projetos e aulas ministradas.


# Como rodar

- Instalar gem e jekyll (mac brew install jekyll)

- No terminal rodar

`./run.sh`

docker compose build --no-cache

# Edição do seu material

- Todo o conteúdo é editado em markdown na pasta `./_pages/`
- a pagina inicial está em`index.md`
- A configuração do site é realizado no arquivo `_config.yml` na raiz do projeto. No arquivo, tem como mudar o skin (cores) da pagina na linha `minimal_mistakes_skin    : "air"`. Nela, coloca tb as informações gerais de perfil (nome, filiação, etc)
- O menu é definido no arquivo `./data/navigation.yml`
- As imagens são armazenadas em `./images/`, já a foto de perfil fica armazenada em `./lost+found/`
- Os projetos de pesquisa estão definidos como blog, e o texto de cada projeto está disponível em `./_posts/`
- Para vincular um arquivo markdown a algum menu específico, alterar a variável `permalink: ` no arquivo markdown. No inicio de cada arquivo, tem a definição de diversos metadados da pagina, como titulo, caminho, resumo, imagem, etc.. para ver o conjunto de variáveis que podem ser definidas, ir em `./_layout_/single.html`. Nessa pagina tem  template de cada tipo de pagina html possivel (o tipo é uma das variaveis definidas no markdown)

Essa é a edição mínima para ter uma pagina pessoal completa. Em seguida é só testar e subir:

- Testar localmente a pagina
- commitar no github que já vai ter o gitpage
- Comprar dominio (opcional) - sugestão [GoDaddy](https://www.godaddy.com/pt-br)
- Mudar o dominio (se quiser) do github pages [tutorial aqui](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site)


