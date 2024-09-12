package Operacoes;

public class Adicao implements Operacao {

    public Adicao(){
        super.setSimbolo('+');
    }

    @Override
    public void calcular( float num1, float num2 ){
        System.out.print( num1+num2 + "\n\n" );
    }
}
