package Principal;
import Operacoes.*;

import java.util.Scanner;

public class Principal {
    
    static float num1, num2;
    static char opcao = '-';
    static Scanner scan = new Scanner(System.in);
    static Operacao operacao;

    static void inserirValores(){
        System.out.print("Digite o 1º valor: ");
        num1 = scan.nextFloat();
        
        System.out.print("Digite o 2º valor: ");
        num2 = scan.nextFloat();
    }

    static void limparTela(){
        System.out.print("\033[H\033[2J"); 
    }

    static void menu(){
        System.out.println("================ MENU ================");
        System.out.println("Digite A para realizar a adição;\n"+
                            "Digite S para realizar a subtração;\n"+
                            "Digite M para realizar a multiplicação;\n"+
                            "Digite D para realizar a divisão;\n"+
                            "Digite 0 (zero) para SAIR;\n");
        System.out.print("                            Opção: ");
    }

    public static void main( String[] args ) throws InterruptedException{

        while( opcao != '0' ){
            
            limparTela();
            menu();
            opcao = Character.toUpperCase(scan.next().charAt(0));

            limparTela();
            if( opcao == '0' ){
                System.out.println("Até mais!");
                break;
            }
            
            System.out.print("Opção selecionada: ");

            if( opcao == 'A' ){
                System.out.println("ADIÇÃO\n");
                operacao = new Adicao();

            } else if ( opcao == 'S' ) {
                System.out.println("SUBTRAÇÃO\n");
                operacao = new Subtracao();

            } else if ( opcao == 'M' ) {
                System.out.println("MULTIPLICAÇÃO\n");
                operacao = new Multiplicacao();

            } else if ( opcao == 'D') {
                System.out.println("DIVISÃO\n");
                operacao = new Divisao();
                
            } else {
                limparTela();
                System.out.println("Opção \"" + opcao + "\" é inválida. Tente novamente.\n");
                Thread.sleep(1500);  
            
                continue;
            }
            
            inserirValores();
            System.out.print("\n" + num1 + " " + operacao.getSimbolo() + " " + num2 + " = ");

            operacao.calcular(num1, num2);

            System.out.println("Pressione ENTER para continuar.");
            scan.nextLine();
            scan.nextLine();

        }
        scan.close();;
    }
}
