 Somador On/Off  

## 📌 Introdução  
Este código implementa um **somador condicionado**, que analisa um texto caratere por caratere e soma apenas os números encontrados quando o estado está **ligado**. O estado pode ser alterado pelas palavras `"on"` e `"off"`, mesmo que seus caracteres estejam divididos entre várias linhas.  

## 🎯 Objetivo  
O objetivo do código é:  
- **Ler um texto** e identificar números.  
- **Manter um somador**, que só adiciona valores quando o estado está ligado.  
- **Detectar "on" e "off" mesmo que estejam fragmentados ao longo de diferentes linhas**.  
- **Exibir a soma imediatamente após `=`**.  
- **Exibir a soma final no final do texto**.  

## 🔍 Funcionamento  
1. **Leitura caractere a caractere**, preservando a estrutura do texto original.  
2. **Uso de um buffer deslizante** para identificar `"on"` e `"off"` mesmo que espalhados.  
3. **Acumulador condicional**, que adiciona números ao total apenas quando o estado está ativado.  
4. **Inserção da soma imediatamente após cada `=`**.  
5. **Exibição da soma final no fim do texto**. 

## ⚠️ Problema Identificado  
Existe uma limitação no funcionamento atual: **se os caracteres de "on" ou "off" estiverem totalmente separados em linhas diferentes, o buffer não consegue identificá-los corretamente**. Isso acontece porque o buffer reseta a cada nova linha, dificultando a detecção de padrões distribuídos entre múltiplas quebras de linha. 

## ⚡ Destaques Técnicos   
- **Processamento eficiente** sem expressões regulares.  
- **Preservação do formato original do texto**, sem alterar espaçamentos ou remoção de números.  
