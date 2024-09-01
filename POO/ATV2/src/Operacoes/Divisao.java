package Operacoes;

public class Divisao extends Operacao {

    public Divisao(){
        super.setSimbolo('/');
    }

    @Override
    public void calcular( float num1, float num2 ){
        if( num2 != 0 ){
            System.out.print( num1/num2 + "\n\n" );
        } else {
            System.out.print("DIVISÃO IMPOSSÍVEL.\n\n");
        }
    }
}
