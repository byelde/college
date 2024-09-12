package br.ufal.carro.principal;

import br.ufal.carro.Carro;
import br.ufal.carro.MotorDiesel;
import br.ufal.carro.MotorFlex;
import br.ufal.carro.Tanque;

public class PrincipalCarro {
	public static void main(String[] args) {

		Carro camario = new Carro(
			"Camaro", 
			"Amarelo", 
			new MotorFlex(), 
			new Tanque(60)
		);


		Carro doidoram = new Carro(
			"Ram", 
			"Branco", 
			new MotorDiesel(), 
			new Tanque(60)
		);

	// Teste primeira questão: 
		camario.acelerar(0);
		// O que acontece se acelerar-mos um carro sem combustível?
		// RESPOSTA: Nada acontece, pois o carro só acelera proporcionalmente ao combustível presente nele

	// Teste segunda questão:
		camario.abastecer(10);
		doidoram.abastecer(10);

		camario.acelerar(10);
		doidoram.acelerar(10);

		// Velocidade do carro com motor flex (Camario): 100
		// Velocidade do carro com motor diesel (doidoram): 68
		

		System.out.println("Velocidade do " + camario.getModelo() + ": " + camario.getVelocidade());
		System.out.println("Velocidade do " + doidoram.getModelo() + ": " + doidoram.getVelocidade());

	};


}
