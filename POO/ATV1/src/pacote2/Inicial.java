package pacote2;
import pacote1.Carta;

public class Inicial {
    public static void main(String[] args) {
        System.out.println("Iniciou");
        Carta cartinha = new Carta("Gabryel", "2024/08/02", "Nenhum");
        // System.out.println( cartinha.nome);
        // System.out.println( cartinha.data);
        // System.out.println( cartinha.anexo);
        /*
        Tópico 12:
            Ocorreu um erro de visibilidade no atributos da instancia de Carta,
        pois os atributos de Carta têm a visibilidade protected (data) e de pacote
        (nome e anexo), portanto invisíveis para o arquivo Inicial.java. Para
        evitar o erro, bastou usar o método público mostra() já existente na classe
        Carta.
        */
        cartinha.mostrar();
    }
}
