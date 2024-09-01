package Operacoes;

public class Multiplicacao extends Operacao {

    public Multiplicacao(){
        super.setSimbolo('*');
    }

    @Override
    public void calcular( float num1, float num2 ){
        System.out.print( num1*num2 + "\n\n" );
    }
}
