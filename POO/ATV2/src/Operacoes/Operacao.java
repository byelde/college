package Operacoes;

public class Operacao {    

    private char simbolo = '?';

    public void calcular( float num1, float num2 ){
        System.out.println("Operação matemática entre " + num1 + " e " + num2);
    }

    public char getSimbolo(){
        return simbolo;
    }

    protected void setSimbolo( char simbolo){
        this.simbolo = simbolo;
    }
}
