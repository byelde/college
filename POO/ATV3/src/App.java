import registro.Pessoa;
import registro.Agenda;

public class App {
    public static void main(String[] args) throws Exception {
        Agenda agenda = new Agenda();
        agenda.inserirPessoa( new Pessoa("Eduardo", "82 9.9962-9433", "eduardopiratinha@gmail.com", "123456") );
        agenda.inserirPessoa( new Pessoa("Frederico", "82 9.9962-9435", "frederico.mola.lisa@gmail.com", "1234567") );
        agenda.inserirPessoa( new Pessoa("Kenny", "82 9.9962-0000", "kenny&nandja@gmail.com", "1234567") );
        agenda.inserirPessoa( new Pessoa("Lajota", "82 9.9923-1324", "danilogentilli@gmail.com", "1234567") );
        agenda.inserirPessoa( new Pessoa("Juninho Pancada", "89 9.8862-1200", "pelota@gmail.com", "1234567") );

        agenda.imprimirPessoas();
        agenda.removerPessoa( new Pessoa("Frederico", "82 9.9962-9435", "frederico.mola.lisa@gmail.com", "1234567") );
        agenda.imprimirPessoas();
    }
}
