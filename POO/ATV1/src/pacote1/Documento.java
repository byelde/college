package pacote1;

public class Documento {
    String nome;
    protected String data;

    public Documento( String nome, String data ){
        this.nome = nome;
        this.data = data;
    }

    public Documento( String data ){
        this.nome = "NULL";
    }

    protected void setNome( String nome ){
        this.nome = nome;
    }

    protected void mostrar(){
        System.out.println("Nome: " + this.nome);
        System.out.println("Data: " + this.data);
    }
        
}
