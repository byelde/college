package registro;

public class Pessoa {

    private String nome;
    private String telefone;
    private String email;
    private String senha;

    public Pessoa( String nome, String telefone, String email, String senha ){
        this.nome = nome;
        this.telefone = telefone;
        this.email = email;
        this.senha = senha;
    }

    public String getNome(){
        return this.nome;
    }

    public String getTelefone(){
        return this.telefone;
    }

    public String getEmail(){
        return this.email;
    }

    public Boolean validarSenha( String senha ){
        return this.senha.equals(senha);
    }

}