package br.ufal.carro;

public class MotorFlex implements Motor {

	public boolean ligado;
	public int aceleracao;

	public MotorFlex() {
		this.ligado = false;
		this.aceleracao = 0;
	}

	
	public void ligar(){
		this.ligado = true;
	};
	

	public void desligar(){
		this.ligado = false;
	};


	public boolean isLigado(){
		return this.ligado;
	};

	
	public void setAceleracao(int aceleracao){
		this.aceleracao = aceleracao;
	};
	

	public int getAceleracao(){
		return this.aceleracao;
	};


	public void acelerar(Carro c, int quantCombustivel) {
		this.setAceleracao(quantCombustivel*500);
		c.setVelocidade( this.getAceleracao()/50 );
	}

}
