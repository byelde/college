package pacote2;
import pacote1.Carta;

public class Inicial {
    public static void main(String[] args) {
        System.out.println("Iniciou");
        /*
        Tópico 12:
            Ocorreu um erro de tipo, pois a classe "Carta", inicialmente, não 
        está visível para o arquivo "Inicial.java" por estarem em pacotes 
        diferentes. Para corrigir isso, bastou apenas importar a classe "Carta"
        do pacote "pacote1".
         */
        Carta cartinha = new Carta("Gabryel", "2024/08/02", "Nenhum");
        cartinha.mostrar();
    }
}
