package pacote2;
import pacote1.Documento;
import pacote1.Carta;

public class Telegrama extends Documento {
    private String assinatura;

    Telegrama( String nome, String data, String assinatura ){
        super(nome, data);
        this.assinatura = assinatura;
    }
    
    public void mostrar(){
        super.mostrar();
        System.out.println("Assinatura: " + this.assinatura);
    }

    public String getData(){
        return this.data;
    }

    public void mostrar2(){
        Carta carta = new Carta( "Gabryel", "2024/08/02", "Nenhum");
        Telegrama tele_sena =  new Telegrama("Emylle;", "2024/08/02", "Gabryel");

        // System.out.println("Data da carta: " + carta.data);
        // System.out.println("Data do telegrama: " + tele_sena.data);

        /*
        Tópico 10:
                Não é possível consultar de forma direta o atributo "data" da instância
        da classe Carta, pois está "protegido", portanto incapaz de ser consultado dessa 
        forma. Para solucionar, criei, na classe Carta um método público chamado "getData()" 
        capaz de retornar o seu dado "data". Fiz o mesmo para a classe "Telegrama" por 
        questões de boas práticas.
        */

        System.out.println("Data da carta: " + carta.getData());
        System.out.println("Data do telegrama: " + tele_sena.getData());

    }
}
