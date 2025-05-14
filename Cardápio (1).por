programa {

  inclua biblioteca Matematica

  funcao inicio() {
    inteiro paoFrances = 0 , paoDoce = 0 , paoForma = 0 , paoRecheado = 0 
    real pFrances = 0, pFrancesArr, pDoce = 0, pDoceArr, pForma = 0, pFormaArr, pRecheado = 0, pRecheadoArr, somaTotal, somaTotalArr
    inteiro numero, quantidade

    escreva("====== Cardapio ======\n")
    escreva("======================\n")
    escreva("1 - Pão Francês\n")
    escreva("2 - Pão Doce\n")
    escreva("3 - Pão de Forma\n")
    escreva("4 - Pão Recheado\n")
    escreva("5 - Finalizar Pedido\n")
    escreva("======================\n")

    faca {

    escreva("Escolha o numero do cardápio: ")
    leia(numero)

      escolha (numero) {

        caso 1:
        escreva("Selecione a quantidade de Pão Francês: ")
        leia(quantidade)
        paoFrances = paoFrances + quantidade
        pFrances = paoFrances * 1.2
        pare

        caso 2:
        escreva("Selecione a quantidade de Pão Doce: ")
        leia(quantidade)
        paoDoce = paoDoce + quantidade
        pDoce = paoDoce * 1.4
        pare

        caso 3:
        escreva("Selecione a quantidade de Pão de Forma: ")
        leia(quantidade)
        paoForma = paoForma + quantidade
        pForma = paoForma * 2.5
        pare

        caso 4:
        escreva("Selecione a quantidade de Pão Recheado: ")
        leia(quantidade)
        paoRecheado = paoRecheado + quantidade
        pRecheado = paoRecheado * 3.9
        pare        

        }

      }

      enquanto (numero != 5)

        somaTotal = pFrances + pDoce + pForma + pRecheado
        somaTotal = Matematica.arredondar (somaTotal, 2)
        pFrancesArr = Matematica.arredondar (pFrances, 2)
        pDoceArr = Matematica.arredondar (pDoce, 2)
        pFormaArr = Matematica.arredondar (pForma, 2)
        pRecheadoArr = Matematica.arredondar (pRecheado, 2)

        escreva("======= Nota fiscal =======\n")

        se (paoFrances > 0) {
        escreva("1 - Pão Francês = " , paoFrances , " Und " , pFrancesArr , " R$.\n")
        }

        se (paoDoce > 0) {
        escreva("2 - Pão Doce = " , paoDoce , " Und " , pDoceArr , " R$.\n")
        }

        se (paoForma > 0 ) {
        escreva("3 - Pão de Forma = " , paoForma , " Und " , pFormaArr , " R$.\n")
        }

        se (paoRecheado > 0) {
        escreva("4 - Pão Recheado = " , paoRecheado , " Und " , pRecheadoArr , " R$.\n")
        }

        escreva("===========================\n")
        escreva("Valor total: " , somaTotal , " R$.\n")
        escreva("===========================\n")

  }
}