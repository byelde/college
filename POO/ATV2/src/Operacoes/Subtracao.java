package Operacoes;

public class Subtracao implements Operacao {

    public Subtracao(){
        super.setSimbolo('-');
    }

    @Override
    public void calcular( float num1, float num2 ){
        System.out.print( num1-num2 + "\n\n" );
    }
}
