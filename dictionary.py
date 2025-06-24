dicionario = []

while True:
    print(
        "\n======= DICIONÁRIO EM INGLÊS ======="
        )
    try:
        opcao = int(input(
            "1. Adicionar palavra\n"
            "2. Ver lista de palavras\n"
            "3. Filtrar por letra inicial\n"
            "4. Sair\n"
            "Escolha uma opção: "
        ))

        if opcao == 1:
            valor = input(
                "Digite a palavra que você quer adicionar: "
                ).strip()
            tipo = input(
                "Digite o tipo da palavra (substantivo, verbo, etc.): "
                ).strip()
            traducao = input(
                "Digite a tradução da palavra: "
                ).strip()
            
            letra_inicial = valor[0].lower()

            nova_palavra = {
                "nome": valor,
                "tipo": tipo,
                "traducao": traducao,
                "letra": letra_inicial
            }

            dicionario.append(nova_palavra)
            print(
                f"Palavra '{valor}' adicionada com sucesso!"
                )

        elif opcao == 2:
            if not dicionario:
                print(
                    "O dicionário está vazio."
                    )
            else:
                for chave, valor in enumerate(dicionario, 1):
                    print(
                        f"{chave}. Nome: {valor['nome']}, Tipo: {valor['tipo']}, Tradução: {valor['traducao']}, Letra: {valor['letra']}"
                        )

        elif opcao == 3:
            letra = input(
                "Digite uma letra para filtrar as palavras: "
                ).lower()
            encontrados = [p for p in dicionario if p['letra'] == letra]

            if encontrados:
                for valor in encontrados:
                    print(
                        f"Nome: {valor['nome']}, Tipo: {valor['tipo']}, Tradução: {valor['traducao']}"
                        )
            else:
                print(
                    "Nenhuma palavra encontrada com essa letra."
                    )

        elif opcao == 4:
            print(
                "Saindo do programa..."
                )
            break

        else:
            print(
                "Opção inválida. Escolha entre 1-4."
                )

    except ValueError:
        print(
            "Por favor, digite um número válido."
            )
