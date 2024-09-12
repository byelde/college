package br.ufal.carro;

public class Carro {

	private String modelo;
	private String cor;
	private int velocidade;
	private Tanque tanque;
	private Motor motor;

	public Carro(String modelo, String cor, Motor motor, Tanque tanque) {
		this.modelo = modelo;
		this.cor = cor;
		this.motor = motor;
		this.velocidade = 0;
		this.tanque = tanque;
	}


	public void ligar() {
		if( !motor.isLigado() ){
			motor.ligar();
		}

		System.out.println("VRUM, VRUM! (Esquentando o motor do " + this.modelo + ")");
	}


	public void desligar() {
		if( motor.isLigado() ){
			this.freiar();
		};
		motor.desligar();
		System.out.println("Brrum... (Descansando o " + this.modelo + " por hoje)");
	}


	public void acelerar(int quantCombustivel) {

		if( this.tanque.getQuantidadePresente() <= 0 ){
			System.out.println("Ta ruim, leve o " + this.modelo + " no posto.");
			return;
		}

		if( tanque.getQuantidadePresente() < quantCombustivel ){
			quantCombustivel = tanque.getQuantidadePresente();
		};

		this.motor.acelerar(this, quantCombustivel);
		System.out.println("Niiiiiiiiiiiiiiiiiiiiiiii (Segura o " + this.modelo + "!)");
		tanque.usarCombustivel(quantCombustivel);

		if( tanque.getQuantidadePresente() <= 0 ){
			this.desligar();
		}

	}


	public void freiar() {
		this.setVelocidade(0);
	}


	protected void setVelocidade(int velocidade) {
		this.velocidade = velocidade;
	}


	public int getVelocidade() {
		return this.velocidade;
	}


	public void abastecer( int quantidade ){
		System.out.println( String.format( "Bota " + quantidade + ", meu patrão.") );
		tanque.abastecer(quantidade);
	}
	

	public String getModelo(){
		return this.modelo;
	};

	
	public String getCor(){
		return this.cor;
	}
}
