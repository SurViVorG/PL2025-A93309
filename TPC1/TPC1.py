import sys
import io

def somador_on_off(texto):
    ligado = True  # O somador começa ligado
    soma = 0
    resultado = []
    palavra_atual = ""
    buffer = ""  # Para capturar fragmentos de "on" e "off" ao longo de várias linhas
    linha_atual = ""  # Para armazenar a linha atual

    for caractere in texto:
        linha_atual += caractere  # Adiciona o caractere à linha atual
        buffer += caractere.lower()  # Adiciona ao buffer sem cortar caracteres

        # Detecta "on" e "off" mesmo quando espalhados
        if "off" in buffer:
            ligado = False
            buffer = ""  # Reset do buffer após detectar "off"
        elif "on" in buffer:
            ligado = True
            buffer = ""  # Reset do buffer após detectar "on"

        if caractere.isdigit():
            palavra_atual += caractere  # Construindo número
        else:
            if palavra_atual:
                if ligado:
                    soma += int(palavra_atual)  # Soma o número se estiver ligado
                palavra_atual = ""  # Reset do número atual

            if caractere == "=":
                resultado.append(linha_atual.strip())  # Adiciona a linha até o "="
                resultado.append(f">> {soma}")  # Adiciona a soma logo abaixo do "="
                linha_atual = ""  # Reseta a linha para continuar a leitura

        # Se encontrar uma quebra de linha, adiciona a linha ao resultado
        if caractere == "\n":
            if linha_atual.strip():  # Evita adicionar linhas vazias
                resultado.append(linha_atual.strip())
            linha_atual = ""  # Reseta para próxima linha

    # Adiciona a última linha se não estiver vazia
    if linha_atual.strip():
        resultado.append(linha_atual.strip())

    # Adiciona a soma final ao final do texto
    resultado.append(f">> {soma}")

    return resultado

if __name__ == "__main__":
    entrada_simulada = """Hoje, 7 de Fevereiro de 2025, o professor de Processamento de Linguagens
deu-nos
este trabalho para fazer.=
E deu-nos 7= dias para o fazer... 
Cada trabalho destes vale 0.25 valores da nota final!"""

    sys.stdin = io.StringIO(entrada_simulada)

    entrada = sys.stdin.read()
    saida = somador_on_off(entrada)

    for linha in saida:
        print(linha)
