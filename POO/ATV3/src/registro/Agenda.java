package registro;

import java.util.ArrayList;

public class Agenda {
    private ArrayList<Pessoa> pessoas = new ArrayList<Pessoa>();

    private boolean jaExiste( Pessoa pessoa ){
        for ( Pessoa element : this.pessoas ){
            if ( element.getEmail().equals(pessoa.getEmail())) {
                return true;
            }
        }
        return false;
    }

    public void inserirPessoa( Pessoa nova_pessoa ){
        if(jaExiste(nova_pessoa)){
            removerPessoa(nova_pessoa);
        }
        pessoas.add(nova_pessoa);
    }

    public void removerPessoa( Pessoa pessoa_alvo ){
        pessoas.removeIf( pessoa -> ( pessoa.getEmail().equals( pessoa_alvo.getEmail() ) ) );
    }

    public void imprimirPessoas(){
        System.out.print("{\n");
        for( Pessoa pessoa : pessoas ){
            System.out.println("    Nome: " + pessoa.getNome() + ", Telefone: " + pessoa.getTelefone() + ", Email: " + pessoa.getEmail() + ";");
        }
        System.out.println("}");
    }

}
